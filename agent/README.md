# agent — the detective

The reasoning loop. Reads the OpenAPI spec, decides where the running system probably lies, and proves it by firing real requests.

```
spec (openapi.yaml)
      │
      ▼
1. hypothesize   ── "this claim looks like a lie" (Gemini reads the spec)
2. probe         ── fire a real HTTP request at the live demo-app
3. interpret     ── compare response vs what the spec promised
4. dig           ── suspicious? decide the next probe (adapt)  ←─┐
      │                                                          │
      └──────────────── loop until confident ───────────────────┘
      ▼
findings: { claim, request, response, why-it's-a-hole, severity }
```

- **Gemini API** = the reasoning head (hypothesis generation + response interpretation + next-move).
- **Google ADK** (optional, if time allows) = multi-step autonomy / tool orchestration to make the loop visibly self-driving.
- Output = severity-ranked findings with the raw request/response as evidence, handed to the UI. **No auto-attack / auto-fix** — a human approves (HITL).

> TODO: define the findings schema, the probe toolset (HTTP client as a tool), the hypothesis + interpretation prompts, and the loop controller.
