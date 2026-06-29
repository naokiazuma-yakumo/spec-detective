"""Generate the ProtoPedia architecture image with official Google Cloud icons.

Renders `docs/architecture.png` using the `diagrams` library (which needs Graphviz).

Setup:
    brew install graphviz          # provides the `dot` binary
    pip install diagrams
Run from the repo root:
    python docs/architecture_diagram.py
"""

from diagrams import Diagram, Cluster, Edge
from diagrams.gcp.compute import Run
from diagrams.gcp.ml import AIPlatform
from diagrams.onprem.client import Users

graph_attr = {"fontsize": "18", "bgcolor": "white", "pad": "0.4", "splines": "spline"}

with Diagram(
    "spec-detective — architecture (Google Cloud)",
    filename="docs/architecture",
    outformat="png",
    show=False,
    direction="LR",
    graph_attr=graph_attr,
):
    reviewer = Users("Human reviewer\n(HITL)")

    with Cluster("Google Cloud"):
        gemini = AIPlatform("Gemini\n(Vertex AI) — reasoning")

        with Cluster("Cloud Run"):
            web = Run("Web UI\nReact / Next")
            agent = Run("Detective Agent\nGemini + ADK")
            target = Run("Health Records API\nFastAPI (vulnerable, synthetic)")

    reviewer >> Edge(label="1. start a run") >> web
    web >> Edge(label="2. trigger") >> agent
    agent >> Edge(label="reads openapi.yaml\n(prose promises)") >> target
    agent >> Edge(label="reasoning", style="dashed") >> gemini
    agent >> Edge(label="3. real HTTP probes") >> target
    target >> Edge(label="responses = evidence") >> agent
    agent >> Edge(label="4. findings\n(promise <-> evidence, severity)") >> web
    web >> Edge(label="5. approve / dismiss") >> reviewer
