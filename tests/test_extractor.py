import pytest
from argparse import ArgumentParser
from pathlib import Path
from extractor import setup_argparse, get_single_book_quotes, type_txt_path
import tempfile
import os
import sys

class TestExtractor:
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