"""Tests."""
from benchkit.markdown import format_markdown

def test_table():
    r = [{"name":"sort","times":[0.1,0.11,0.09],"passed":True}]
    md = format_markdown(r)
    assert "sort" in md and "| Name |" in md

def test_regression():
    r = [{"name":"slow","times":[1.0],"passed":False}]
    assert "REGRESSION" in format_markdown(r)
