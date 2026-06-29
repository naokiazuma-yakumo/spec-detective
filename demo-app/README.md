# demo-app — the target

A small, **deliberately-vulnerable** Health Records API (all data **synthetic**) plus its OpenAPI spec. This is the system the detective probes. We own it, so it never goes down mid-judging (the biggest disqualification risk is a dead live URL) and it stays small to build.

The spec describes the *建前* (how it claims to behave); the implementation hides the *本音* (how it really behaves). **The guarantees are written as prose promises in `openapi.yaml`'s `description` fields — the JSON Schemas are intentionally permissive**, so a schema-conformance fuzzer can't tell whether the promises hold. That's the gap the agent targets.

## Planted gaps

| # | the spec's prose promise | the implementation's reality | class |
|---|---|---|---|
| V1 | passwords must be ≥8 chars; empty is rejected (400) | empty password is accepted | API2 broken auth |
| V2 | `GET /records/{id}` returns the record only if you own it; else 403 | shifting the id returns **another user's record** | API1 BOLA / IDOR |
| V3 | after `DELETE`, `GET /records/{id}` returns 404 | record is soft-deleted but still readable (200) | API3 excessive data exposure |
| V4 | *(not documented at all)* | `GET /admin/export` exists and dumps **all** records, unauthenticated | API9 improper inventory |
| V5 | only `email` and `password` are read on signup; `role` is ignored | sending `role: "admin"` in the body escalates | API6 mass assignment |
| V6 *(optional)* | only the owner may delete; others get 403 | another user's `DELETE` succeeds | API5 broken function-level auth |

> Headline target: human review missed **N** holes → the agent found them in 90s, **M** of which are security (N=5, 2 Critical).

## Stack

- **FastAPI (Python)** — same runtime as the agent; OpenAPI-native.
- **Cloud Run** for deployment.
- `openapi.yaml` — the contract the agent reads (the prose promises live here). **Done** ✅

> TODO: implement the FastAPI endpoints + the planted gaps (V1–V5, V6 optional), seed two synthetic users with records (so IDOR is demonstrable), add the undocumented `/admin/export`, Dockerfile for Cloud Run.
