# web — the UI

Makes the contradiction obvious at a glance: **spec (建前) vs reality (本音)**, side by side, severity-ranked.

Each finding shows:
- the spec claim it tested ("empty passwords are rejected")
- the actual request the agent fired
- the actual response that came back (the evidence)
- why it's a hole, and a severity rank
- an **Approve / Dismiss** control (human-in-the-loop — nothing acts automatically)

Headline framing: *human review missed N holes → the agent found them in 90s, M of which are security.*

## Language — bilingual (JA + EN)

The UI must support **Japanese and English** (i18n, runtime-switchable). Judges are Japanese, so JA is primary for the demo/video; EN keeps the public product accessible. Build with an i18n setup from the start (e.g. `next-intl` / `react-i18next`) — don't hard-code strings. Findings text from the agent (spec_promise, why, etc.) should also be presentable in both languages.

> TODO: pick the stack, set up i18n (JA default + EN), build the evidence-pair view + severity list + the live "watch the agent probe" view for the 3-min demo video.
