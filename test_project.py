import pytest
from main import main

def test_main_empty():
    assert main("") == 0

def test_main_single_line():
    assert main("Hello, World!") == 0

def test_main_multiple_lines():
    assert main("Hello, World!\nThis is a test.") == 0

def test_main_invalid_input():
    with pytest.raises(ValueError):
        main(123)