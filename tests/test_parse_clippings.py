import pytest
import random
import datetime
from parse_clippings import *

class TestPraseClippings:
    def setup_method(self):
        self.extract = \
"""
﻿Python 3 Object-Oriented Programming, Third Edition (Dusty Phillips)\n
- Your Highlight on page 32 | location 483-484 | Added on Saturday, 10 February 2024 10:22:57\n

Usually, we don't need to be overly concerned with data types at the design stage,\n
""" 
        
    def test_retrieve_clippings_from_file(self):
        data = retrieve_clippings_from_file("clippings_example.txt")
        with open("clippings_example.txt", "r") as f:
            assert data == f.read()

    def test_remove_non_ascii_characters(self):
        test_data_ascii = [
            ''.join(
                chr(random.randint(32, 126))
                for _ in range(random.randint(5, 20))
            )
            for _ in range(40)
        ]
        test_data_unicode = [
            ''.join(
                chr(random.randint(0x0100, 0xFFFF))
                for _ in range(random.randint(5, 20))
            )
            for _ in range(40)
        ]
        for ascii_str in test_data_ascii:
            assert remove_non_ascii_characters(ascii_str) == ascii_str
        for unicode_str in test_data_unicode:
            result = remove_non_ascii_characters(unicode_str)
            assert all(ord(c) < 128 for c in result)
    
    def test_get_book_name_and_author(self):
        book_name, author = get_book_name_and_author(self.extract)
        assert book_name == "Python 3 Object-Oriented Programming, Third Edition"
        assert author == "Dusty Phillips"
    
    def test_get_page(self):
        page_num = get_page(self.extract)
        assert page_num == 32
    
    def test_get_date(self):
        expected_ret = datetime(2024, 2, 10, 10, 22, 57)
        ret = get_date(self.extract)
        assert ret == expected_ret
    
    def test_get_extract_quote_metadata(self):
        page, date, quote = get_extract_quote_metadata(self.extract)
        assert page == 32
        assert date == datetime(2024, 2, 10, 10, 22, 57)