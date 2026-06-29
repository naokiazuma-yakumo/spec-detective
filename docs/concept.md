# Concept (public)

> Public-safe writeup. Feeds the ProtoPedia entry and the 3-min demo video.
> Keep clean of anything internal — see the internal hub for boundaries.

## One line

仕様書（建前）と実物（本音）の食い違い＝バグ・セキュリティ穴を、AIが**実物にHTTPを撃って**暴く「セキュリティ探偵」。

## The gap it exploits

Static review reads *text*. It never runs the system, so the holes that only appear at runtime are invisible to it. spec-detective runs the system and watches.

## Why it must be an agent (judging axis ①: autonomy)

A fixed test suite is just automated testing. spec-detective forms its own hypotheses about where the spec lies, probes the live system, reads the reaction, and decides the next move — against a system whose behavior it can't predict. That self-driving loop is the agent necessity.

## How it differs from a generic DAST / AI pentester

A DAST asks "is this endpoint exploitable?". spec-detective asks **"does the system contradict its own written specification?"** — the OpenAPI contract is the oracle. The finding isn't just "IDOR here", it's "the spec promised isolation and the running system breaks that promise, here's the proof."

## Demo arc (3 min)

1. Show the demo app + its spec.
2. Agent reads the spec, says *「空パスワードを弾くと書いてある、怪しい」* (hypothesis).
3. Agent fires an empty password at the **real** API → *「通りました」* + the request/response evidence, in red.
4. Agent keeps going: shifts an ID → finds the auth leak.
5. Headline: *human review missed N holes — agent found them in 90s, M security.*
6. Findings presented to a human to approve (the agent doesn't fix anything itself).

## Judging-axis map

| axis | how this hits it |
|---|---|
| ① autonomy necessity (top weight) | hidden-hole hunting can't be done by fixed steps |
| ② story / novelty | 「仕様＝建前／実装＝本音、隙間に穴」; differentiator = audit against the spec |
| ③ intuitive UI | spec vs reality evidence, side by side |
| ④ breakthrough / empathy | a security hole landing in one shot reads to anyone |
| ⑤ tech choice | Cloud Run + Gemini (+ ADK), clean and external-dependency-free |
