from argparse import ArgumentParser, ArgumentTypeError
from pathlib import Path
from datetime import datetime
import json
from parse_clippings import *
import os

def type_txt_path(value):
    path = Path(value)
    if not path.exists():
        raise ArgumentTypeError("Specified My Clippings.txt does not exist")
    if not path.is_file():
        raise ArgumentTypeError("Specified path is not a file")
    if path.suffix.lower() != ".txt":
        raise ArgumentTypeError("Specified file does not end with .txt")
    return path

def setup_argparse():
   parser = ArgumentParser(
       prog="extractor",
       description="Extracts kindle highlights into markdown format."
    )
   
   parser.add_argument(
       "-i",
       "--input",
       type=type_txt_path,
       help="Kindle's My Clippings.txt location",
       required=True
   )
   
   parser.add_argument(
       "-m",
       "--mode",
       choices=["json", "markdown", "markdown_single", "print_books"],
       required=True,
       help="Output to either json or markdown"
   )
   
   parser.add_argument(
       "-o",
       "--output",
       type=str,
       help="Output file location",
       required=True
   )
   
   parser.add_argument(
       "-b",
       "--book",
       help="Full book title if markdown_single mode is specified",
       type=str.lower
   )

   return parser.parse_args()

def create_markdown_files(quotes : dict, markdown_path : str):
    if not Path(markdown_path).exists():
        os.mkdir(markdown_path) 
    for key in quotes:
        if not Path(f"{markdown_path}/key.md").exists():
            with open(f"{markdown_path}{key}.md", "w") as f:
                f.write(f"# {key}\n- Author: {quotes[key]["author"]}\n---\n")

def write_quotes_to_markdown(quotes : dict, markdown_path : str):
    for key in quotes:
        with open(f"{markdown_path}/{key}.md", "a") as f:
            for nested_key in quotes[key]:
                if isinstance(quotes[key][nested_key], dict):
                    f.write(f"> {nested_key}\n- Page {quotes[key][nested_key]['page_number']}\n- Date Added: {quotes[key][nested_key]['date_added']}\n---\n")

def write_json(quotes : dict, output : str):
    with open(output, "w") as f:
        json_dump = json.dump(quotes, f, ensure_ascii=False, indent=4)

def main():
    global args
    args = setup_argparse()
    quotes = parse_clippings(args) # Does the magic to My Clippings.txt
    if args.mode == "json":
        write_json(quotes, args.output)
        return
    elif args.mode == "markdown":
        create_markdown_files(quotes, args.output)
        write_quotes_to_markdown(quotes, args.output)
        return
    elif args.mode == "markdown_single":
        if not args.book:
            print("extractor: error: The following argument must be specified if markdown_single is set: -b/--book")
            return
        quotes_copy = quotes.copy()
        for key in quotes:
            if str(key).lower() != args.book:
                quotes_copy.pop(key)
        if not quotes_copy:
            print(f"extractor: error: book {args.book} doesn't have any highlights.")
        create_markdown_files(quotes_copy, args.output)
        write_quotes_to_markdown(quotes_copy, args.output)
    elif args.mode == "print_books":
        if not args.book:
            print("extractor: error: The following argument must be specified if print_books is set: -b/--book")
            return
        for key in quotes:
            print(key)
        

if __name__ == "__main__":
    main()