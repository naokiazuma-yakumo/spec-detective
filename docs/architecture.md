# Architecture

spec-detective runs entirely on **Google Cloud** (Cloud Run + Gemini, optionally Google ADK) with **no external dependencies** — so it survives the two-round live judging.

## System / deployment view

```mermaid
flowchart LR
    user([Human reviewer])

    subgraph GC["Google Cloud"]
        subgraph UI["Web UI — Cloud Run"]
            web["React / Next<br/>spec ↔ reality evidence<br/>severity list · Approve/Dismiss"]
        end

        subgraph AG["Detective Agent — Cloud Run"]
            agent["Gemini + Google ADK (Python)<br/>hypothesis → probe → interpret → dig<br/>tools: spec-reader, HTTP-probe"]
        end

        subgraph TG["Demo target — Cloud Run"]
            api["Health Records API (FastAPI)<br/>deliberately vulnerable · synthetic data"]
            spec[["openapi.yaml<br/>promises in prose"]]
        end

        gemini["Gemini API<br/>(reasoning head)"]
    end

    user -->|1 . start a run| web
    web -->|2 . trigger| agent
    agent -->|reads promises| spec
    agent <-->|reasoning| gemini
    agent -->|3 . real HTTP probes| api
    api -->|responses = evidence| agent
    agent -->|4 . findings<br/>spec_promise ↔ evidence · severity| web
    web -->|5 . approve / dismiss| user

    classDef gcp fill:#e8f0fe,stroke:#4285f4,color:#1a1a1a;
    class web,agent,api,spec,gemini gcp;
```

## Agent loop (why it must be an agent)

```mermaid
sequenceDiagram
    participant S as openapi.yaml (spec)
    participant A as Detective Agent (Gemini/ADK)
    participant T as Demo target (FastAPI)

    A->>S: read natural-language promises
    Note over A: "empty passwords are rejected" — looks like a lie
    loop until confident
        A->>A: 1. hypothesize where reality diverges
        A->>T: 2. probe — fire a real HTTP request
        T-->>A: response (the evidence)
        A->>A: 3. interpret: promise upheld or broken?
        A->>A: 4. dig — decide the next probe (adapt)
    end
    A-->>A: finding { spec_promise, spec_ref, probe, response, verdict, severity }
```

The loop is **adaptive against a system whose behavior it cannot predict** — it forms its own hypotheses from the spec's prose, probes, reads the reaction, and chooses the next move. That is the "AI エージェントである必然性" (judging axis ①): a fixed test suite cannot do this.

## Components

| component | tech | role |
|---|---|---|
| Web UI | React / Next, Cloud Run | shows spec (建前) ↔ reality (本音) evidence, severity-ranked; human Approve/Dismiss (HITL) |
| Detective Agent | Python, **Gemini API + Google ADK**, Cloud Run | the hypothesis→probe→interpret→dig loop; tools = spec-reader + HTTP-probe |
| Demo target | **FastAPI**, Cloud Run | a deliberately-vulnerable Health Records API (synthetic data) + `openapi.yaml` whose prose promises it secretly breaks |
| Reasoning | **Gemini API** | hypothesis generation, response interpretation, next-move decisions |

## Why this stack (judging axis ⑤)

- **All Google Cloud, zero external dependencies** → nothing third-party can break during the live-judging windows (7/13–17, 7/21–24).
- **Self-owned target** → the demo app can't go down on us; structurally avoids the biggest disqualification risk (a dead live URL).
- **ADK** makes the agent's multi-step autonomy legible (execution trace) — reinforcing axis ① and giving the UI/video something concrete to show.
- **Fallback**: if ADK costs too much time, the same loop runs on plain Gemini function-calling and still meets the required "Google Cloud AI" criterion.

> The required ProtoPedia "システム構成（システムアーキテクチャ図）" upload is exported from the system/deployment diagram above.
