# spec-detective

> Individual hackathon entry — 個人事業（屋号：八雲）として開発・公開
> Built for the **DevOps × AI Agent Hackathon 2026** (Findy / Google Cloud Japan).

**An AI agent that probes your live API to expose where the spec (建前) and reality (本音) disagree.**

仕様書（こう動くと書いてある＝建前）と、実際に動くシステム（本当はこう動く＝本音）の食い違い＝バグ・セキュリティ穴を、AIエージェントが**実物を操作して**暴く探偵。

## Why

Code review, linters and static analysis only read the *text* of your code — they never run it. The holes that only surface when the system is actually running are, by definition, invisible to them. spec-detective fires real requests at the running system and watches how it behaves.

- Spec: *「空パスワードは弾く」* → fire an empty password at the real API → **it goes through**.
- Spec: *「他人のデータは見えない」* → shift the ID by one → **someone else's record comes back** (IDOR).
- Spec: *「削除すると消える」* → hit the API directly → **it's still there** (soft-delete leak).

The angle that sets this apart from a generic DAST / AI pentester: it audits **the contradiction against the written specification**, not just "is this endpoint exploitable".

## Why an agent (not just a test suite)

Running a fixed set of tests a human wrote is just automated testing — no agent needed. spec-detective works like a detective:

1. reads the spec and guesses where reality probably **lies** (hypothesis)
2. fires real HTTP requests at the system (probe)
3. reads what comes back and decides where to **dig next** (adapt)
4. holds the evidence (request / response) and reports "here's a hole", severity-ranked

This *hypothesis → probe → observe → next-move* loop, run against a system whose behavior it can't predict, is why it has to be an agent. **Gemini is the reasoning head.**

## Human-in-the-loop

It never attacks, mutates or fixes automatically. It presents evidence; a human judges and approves.

## Stack

- **Google Cloud Run** — hosts both the target demo app and the agent
- **Gemini API** — the agent's reasoning (Google ADK optional, for multi-step autonomy)
- No external dependencies — entirely on Google Cloud, so it survives the two-round live judging

## Layout

| dir | what |
|---|---|
| `demo-app/` | a deliberately-vulnerable target: a small REST API + its OpenAPI spec |
| `agent/` | the detective: hypothesis → probe → interpret → dig loop (Gemini) |
| `web/` | UI: spec vs reality evidence, side by side, severity-ranked |
| `docs/` | concept writeup (feeds the ProtoPedia entry) |

## Status

🚧 **WIP** — building toward submission (deadline 2026-07-10 23:59 JST).

## License

MIT — see [LICENSE](./LICENSE). IP belongs to the author per the hackathon rules.
