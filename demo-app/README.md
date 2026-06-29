# demo-app — the target

A small, **deliberately-vulnerable** REST API plus its OpenAPI spec. This is the system the detective probes. We own it, so it never goes down mid-judging (the biggest disqualification risk is a dead live URL) and it stays small to build.

The spec describes the *建前* (how it claims to behave); the implementation hides the *本音* (how it really behaves). Planted gaps:

| spec says | reality | class |
|---|---|---|
| empty passwords are rejected | empty password is accepted | input-validation bypass |
| you only see your own data | shifting the ID returns another user's record | IDOR / broken object-level auth |
| deleting removes the record | the record is still reachable via the API | soft-delete leak |
| (spec lists endpoints A, B, C) | an undocumented endpoint D exists and is reachable | hidden / shadow endpoint |

- **Spec**: `openapi.yaml` is the contract the agent reads.
- **Deploy**: Cloud Run.

> TODO: pick the stack (FastAPI / Express), implement the endpoints + the planted gaps, write `openapi.yaml`, Dockerfile for Cloud Run.
