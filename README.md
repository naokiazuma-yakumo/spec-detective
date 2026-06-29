# spec-detective

> Individual hackathon entry — 個人事業（屋号：八雲）として開発・公開
> Built for the **DevOps × AI Agent Hackathon 2026** (Findy / Google Cloud Japan).

**An AI agent that probes your live API to expose where the spec (建前) and reality (本音) disagree.**

仕様書（建前）と、実際に動くシステム（本音）の食い違い＝バグ・セキュリティ穴を、AIエージェントが**実物にHTTPを撃って**暴く「セキュリティ探偵」。コードレビューや静的解析は"文字"を読むだけで、動かして初めて出る穴は見つけられない。spec-detective は仕様の**自然言語の約束**（例：「空パスワードは弾く」「他人のデータは見えない」）を正解（オラクル）に据え、その約束破りを実物操作で証拠付きに暴く。

Not *"is it exploitable?"* and not *"does it match the schema?"* — **"is the system lying about its own spec?"**

## Stack

- **Google Cloud Run** — hosts the target app and the agent
- **Gemini API** (＋ Google ADK) — the agent's reasoning
- No external dependencies — entirely on Google Cloud

## Status

🚧 **設計フェーズ。実装はこれから。** 実装の進行に合わせて、コードと**その設計**をこのリポジトリに追加していきます（設計だけの先行ドキュメントは置きません）。

## License

MIT — see [LICENSE](./LICENSE). IP belongs to the author per the hackathon rules.
