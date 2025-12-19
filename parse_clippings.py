import re
from datetime import datetime
import argparse

def retrieve_clippings_from_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

def remove_non_ascii_characters(string : str):
    return ''.join(i for i in string if ord(i) < 128)

def get_book_name_and_author(extract : str):
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
    try:
        return int(re.findall(r"page\s+(\d+)", extract_split)[0])
    except:
        return -1

def get_date(extract_split : str):
    try:
        date_raw = re.findall(r"Added on\s+([A-Za-z]+,\s+\d{1,2}\s+[A-Za-z]+\s+\d{4}\s+\d{2}:\d{2}:\d{2})", extract_split)[0]
        date_dt = datetime.strptime(date_raw, "%A, %d %B %Y %X")
        return date_dt
    except:
        return datetime(2020, 1, 1)

def get_extract_quote_metadata(extract : str): 
    extract = extract.split("\n")
    page = get_page(extract[2])
    date =  get_date(extract[2])
    quote = extract[4]
    return (page, date, quote)

def parse_clippings(args : argparse.Namespace):

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