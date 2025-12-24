from argparse import ArgumentParser, ArgumentTypeError
from pathlib import Path
from datetime import datetime
import json
from parse_clippings import *
from markdown_handler import *
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

def write_json(quotes : dict, output : str):
    with open(output, "w") as f:
        json_dump = json.dump(quotes, f, ensure_ascii=False, indent=4)

def get_single_book_quotes(quotes : dict, book_name : str):
    """Gets all quotes from a single book. Discards every other book.

    Args:
        quotes (dict): Dictionary of all quotes from My Clippings.txt
        book_name (str): The book to get the quotes from.

    Returns:
        _type_: _description_
    """
    quotes_copy = quotes.copy()
    for key in quotes:
        if str(key).lower() != book_name:
            quotes_copy.pop(key)
    if not quotes_copy:
        print(f"extractor: error: book {book_name} doesn't have any highlights.")
    return quotes_copy

def main():
    args = setup_argparse()
    quotes : dict = parse_clippings(args) # Does the magic to My Clippings.txt
    if args.mode == "json":
        write_json(quotes, args.output)

    elif args.mode == "markdown":
        if not Path(args.output).is_dir():
            print("extractor: error: output path must be a directory")
            return
        create_markdown_files(quotes, args.output)
        write_markdown(quotes, args.output)

    elif args.mode == "markdown_single":
        if not args.book:
            print("extractor: error: The following argument must be specified if markdown_single is set: -b/--book")
            return
        if Path(args.output).is_dir() or Path(args.output).suffix != ".md":
            print("extractor: error: output path must be a file ending in .md")

        quotes_copy = get_single_book_quotes(quotes, args.book)
        write_markdown_single(quotes_copy, args.output)

    elif args.mode == "print_books":
        for key in quotes:
            print(key)
        

if __name__ == "__main__":
    main()