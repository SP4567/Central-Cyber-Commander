from llm.load_model import load_llm
from llm.model import CyberLLM
from ingestion.log_parse import parse_log
from rag.embedder import Embedder
from rag.vector_store import VectorStore
from rag.retriever import Retriever
from agent.commander import CyberCommander
from agent.severity import calculate_severity
from agent.actions import suggest_actions
from ui.cli import show_report
from rag.build_vector_db import build_vector_db
from reports.report_writer import save_report
import yaml

# Load config
config = yaml.safe_load(open("config/config.yaml"))

# Load LLM
model, tokenizer = load_llm(config["model"]["name"])
llm = CyberLLM(model, tokenizer)

# Setup RAG
embedder = Embedder(config["rag"]["embedding_model"])

store = build_vector_db()
retriever = Retriever(embedder, store)

# Commander
commander = CyberCommander(llm, retriever)

# Simulated log
log = "Multiple SYN packets detected from 45.83.193.10 indicating possible port scan"
event = parse_log(log)

analysis = commander.analyze(event)
severity = calculate_severity(event, analysis)
actions = suggest_actions(severity)

show_report(event, analysis, severity, actions)

report_path = save_report(
    event=event,
    analysis=analysis,
    severity=severity,
    actions=actions
)
print(f"[+] Report saved to {report_path}")
