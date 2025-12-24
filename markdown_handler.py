from pathlib import Path
import os

def create_markdown_files(quotes : dict, markdown_path : str):
    if not Path(markdown_path).exists():
        os.mkdir(markdown_path) 
    for key in quotes:
        if not Path(f"{markdown_path}/key.md").exists():
            with open(f"{markdown_path}{key}.md", "w") as f:
                f.write(f"# {key}\n- Author: {quotes[key]["author"]}\n---\n")

def write_markdown(quotes : dict, markdown_path : str):
    for key in quotes:
        with open(f"{markdown_path}/{key}.md", "a") as f:
            for nested_key in quotes[key]:
                if isinstance(quotes[key][nested_key], dict):
                    f.write(f"> {nested_key}\n- Page {quotes[key][nested_key]['page_number']}\n- Date Added: {quotes[key][nested_key]['date_added']}\n---\n")