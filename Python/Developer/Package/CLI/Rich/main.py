import json
import time
import rich
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table
from rich import progress
from rich.console import Console

console = Console()

rich.print("[bold magenta]Hello[/bold magenta] [underline cyan]Rich[/underline cyan]!")

md = Markdown("""
# Rich Markdown Rendering

**Rich** supports _Markdown_ to display styled text in the terminal.

## Features
- Headings
- **Bold** and *Italic*
- Links: [Rich Documentation](https://rich.readthedocs.io/)
- Code blocks and inline `code`

## Code Example
```python
from rich.console import Console
console = Console()
console.print("Hello, Rich!")""")
console.print(md, markup=True)

table = Table(title="Sample Table")
table.add_column("Name", style="cyan", justify="left")
table.add_column("Age", style="magenta", justify="right")
table.add_column("Country", style="green", justify="center")
table.add_row("Alice", "30", "USA")
table.add_row("Bob", "25", "UK")
table.add_row("Charlie", "35", "Canada")
console.print(table)

for step in progress.track(range(10), description="Processing..."):
    time.sleep(0.5)

data = {"name": "Alice", "age": 30, "country": "USA"}
console = Console()
console.print_json(json.dumps(data))
