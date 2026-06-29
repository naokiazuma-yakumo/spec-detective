"""日本語版アーキテクチャ図（確認・国内提出用）。docs/architecture.ja.png を生成。

英語版と同じ構成。graphviz が日本語を描けるよう日本語フォントを指定する。
    brew install graphviz && pip install diagrams
    python docs/architecture_diagram_ja.py
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import AIPlatform
from diagrams.onprem.client import Users

# 日本語が描けるフォント（macOS標準）。環境に無ければ "Noto Sans CJK JP" 等へ。
JP_FONT = "Hiragino Sans"

graph_attr = {"fontsize": "18", "bgcolor": "white", "pad": "0.4",
              "splines": "spline", "fontname": JP_FONT}
node_attr = {"fontname": JP_FONT}
edge_attr = {"fontname": JP_FONT}

with Diagram(
    "spec-detective ― アーキテクチャ（Google Cloud）",
    filename="docs/architecture.ja",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
    node_attr=node_attr,
    edge_attr=edge_attr,
):
    reviewer = Users("レビュー担当者\n（人間・HITL）")

    with Cluster("Google Cloud"):
        gemini = AIPlatform("Gemini\n（Vertex AI）推論")

        with Cluster("Cloud Run"):
            web = Run("Web UI\nReact / Next")
            agent = Run("探偵エージェント\nGemini + ADK")
            target = Run("的アプリ：健康記録API\nFastAPI（脆弱・合成データ）")

    reviewer >> Edge(label="1. 実行開始") >> web
    web >> Edge(label="2. トリガー") >> agent
    agent >> Edge(label="仕様(openapi.yaml)を読む\n（散文の約束）") >> target
    agent >> Edge(label="推論", style="dashed") >> gemini
    agent >> Edge(label="3. 実物にHTTPを撃つ") >> target
    target >> Edge(label="レスポンス＝証拠") >> agent
    agent >> Edge(label="4. 発見\n（約束↔証拠・深刻度）") >> web
    web >> Edge(label="5. 承認 / 却下") >> reviewer
