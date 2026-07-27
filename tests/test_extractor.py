import pytest
from argparse import ArgumentParser
from pathlib import Path
from extractor import setup_argparse, get_single_book_quotes, type_txt_path, write_json, parse_clippings
import tempfile
import os
import sys
import json

class TestExtractor:
    def test_markdown_single_mode_with_book_argument(self):
        with tempfile.NamedTemporaryFile(suffix=".txt", delete=False, mode="w") as tmp:
            tmp.write("test content")
            tmp_path = tmp.name
        try:
            sys.argv = ["extractor.py", "-i", tmp_path, "-m", "markdown_single", "-o", "Markdown/", "-b", "Python 3 Object-Oriented Programming, Third Edition"]
            args = setup_argparse()
            assert args.mode == "markdown_single"
            assert args.book == "python 3 object-oriented programming, third edition"
            assert args.output == "Markdown/"
        finally:
            os.unlink(tmp_path)
    def test_json_correct_output(self):
        try:
            sys.argv = ["extractor.py", "-i", "tests/test_clipping.txt", "-m", "json", "-o", "tests/test_json_correct_output.json"]
            args = setup_argparse()
            quotes = parse_clippings(args)
            write_json(quotes, args.output)
            with open("tests/assert_test_json_correct_output.json") as expected_file, open("tests/test_json_correct_output.json") as actual_file:
                assert json.load(expected_file) == json.load(actual_file)
            
        finally:
            os.unlink("tests/test_json_correct_output.json")