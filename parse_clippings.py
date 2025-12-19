import re
from datetime import datetime
import argparse

def retrieve_clippings_from_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

def remove_non_ascii_characters(string : str):
    return ''.join(i for i in string if ord(i) < 128)

def get_book_name_and_author(extract : str):
    """Retrieves book name and author from an extract.

    Args:
        extract (str): A single extract WITHOUT .split

    Returns:
        2-tuple: book_name, author in a tuple format.
    """
    extract = remove_non_ascii_characters(extract)
    # Try both formats: "Book Title (Author)" and "Book Title - Author"
    match = re.search(r"(.+?)\s*\((.+?)\)", extract)
    if match:
        return match.group(1).strip(), match.group(2).strip()

    match = re.search(r"(.+?)\s*-\s*(.+)", extract)
    if match:
        return match.group(1).strip(), match.group(2).strip()

    return "", ""

def get_page(extract_split : str):
    """Get page number of a specific extract.

    Args:
        extract_split (str): extract after running .split(\n) on it

    Returns:
        int: page number
    """
    try:
        return int(re.findall(r"page\s+(\d+)", extract_split)[0])
    except:
        return -1

def get_date(extract_split : str):
    """Finds the date from the provided extract and returns it in datetime format

    Args:
        extract_split (str): Extract after running .split("\n")

    Returns:
        datetime: Datetime in the format YYYY-mm-dd HH:mm:ss
    """
    try:
        date_raw = re.findall(r"Added on\s+([A-Za-z]+,\s+\d{1,2}\s+[A-Za-z]+\s+\d{4}\s+\d{2}:\d{2}:\d{2})", extract_split)[0]
        date_dt = datetime.strptime(date_raw, "%A, %d %B %Y %X")
        return date_dt
    except:
        return datetime(2020, 1, 1)

def get_extract_quote_metadata(extract : str): 
    """Gets the Page date and quote from the provided Kindle extract.

    Args:
        extract (str): A single extract from My Clippings.txt

    Returns:
        3-tuple: Containing (page, date, quote)
    """
    extract = extract.split("\n")
    page = get_page(extract[2])
    date =  get_date(extract[2])
    quote = extract[4]
    return (page, date, quote)

def parse_clippings(args : argparse.Namespace):
    """Parses Kindle's My Clippings.txt into a dictionary of the form:
    {
        "Book Title" : {
            "quote1" : {
                "page_number" : int,
                "date_added" : datetime
            },
            "quote2: : ...
        },
        ...
    }
    
    
    Args:
        args (argparse.Namespace): Parsed Arguments from argparse

    Returns:
        dict: Dictionary JSON with output Quotes
    """

    full_extracts = retrieve_clippings_from_file(args.input).split("==========")
    full_extracts.pop()

    quotes = { }
    for extract in full_extracts:

        book_name, book_author = get_book_name_and_author(extract)
        page, date, quote = get_extract_quote_metadata(extract)

        if book_name not in quotes.keys():
            quotes[book_name] = {
                "author" : book_author, 
                quote : {
                    "page_number" : page,
                    "date_added" : date.strftime("%Y-%m-%d %X"),
                }
            }
        else:
            quotes[book_name][quote] = {
                "page_number" : page,
                "date_added" : date.strftime("%Y-%m-%d %X")
            }
    return quotes