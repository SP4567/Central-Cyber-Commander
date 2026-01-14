from rich.console import Console
console = Console()

def show_report(event, analysis, severity, actions):
    console.rule("CYBER COMMANDER REPORT")
    console.print("[bold]Event:[/bold]", event)
    console.print("[bold]Analysis:[/bold]", analysis)
    console.print("[bold red]Severity:[/bold red]", severity)
    console.print("[bold]Actions:[/bold]", actions)
