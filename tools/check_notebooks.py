"""Execute published notebooks from fresh kernels, saving static fallback outputs."""
import nbformat
from nbclient import NotebookClient
from check_content import pages

for path in pages():
    if path.suffix != ".ipynb":
        continue
    notebook = nbformat.read(path, as_version=4)
    # nbclient's default skip tag matches our explicitly documented exercise tag.
    NotebookClient(notebook, timeout=180, kernel_name="python3",
                   skip_cells_with_tag="skip-execution",
                   resources={"metadata": {"path": str(path.parent)}}).execute()
    nbformat.write(notebook, path)
    print(f"Executed {path}")
