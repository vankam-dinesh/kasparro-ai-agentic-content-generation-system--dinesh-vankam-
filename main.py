from pathlib import Path
from orchestrator.dag_orchestrator import PageAssemblyOrchestrator


def main() -> None:
    project_root = Path(__file__).resolve().parent
    orchestrator = PageAssemblyOrchestrator(project_root=project_root)
    orchestrator.run()
    print("Pages generated in the 'output' directory.")


if __name__ == "__main__":
    main()
