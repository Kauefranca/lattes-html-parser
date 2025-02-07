from bs4 import BeautifulSoup
import re

def format_value(value: str) -> str:
    return re.sub(r'\s+', ' ', value)

def select_and_format_text(element: BeautifulSoup, selector: str) -> str:
    value = element.select_one(selector).get_text(strip=True)
    value = format_value(value)

    return value.encode('utf-8', 'ignore').decode('utf-8')

def transform_elm_in_text(element: BeautifulSoup) -> str:
    value = element.get_text(separator=' ', strip=True)
    return format_value(value)