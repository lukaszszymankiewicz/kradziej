import re

from bs4 import BeautifulSoup

import json


SCORE_SHEET_REGEX = r"https://musescore.com/static/musescore/scoredata.*score_0"


def create_soup(page_content):
    return BeautifulSoup(page_content, "html.parser")


def get_song_title_from_soup(soup):
    song_title = _find_title_in_soup(soup)
    song_title_cleaned = _delete_nonalphanumeric_chars(song_title)
    return song_title_cleaned


def get_first_sheet_page_image_url_from_soup(soup):
    image_clue = _find_image_clue_in_soup(soup)
    image_url = _clean_url(image_clue)
    return image_url


def get_number_of_pages_from_soup(soup):
    data_content = soup.find(name="div", class_="js-store")["data-content"]
    data = json.loads(data_content)
    return data["store"]["jmuse_settings"]["score_player"]["json"]["metadata"]["pages"]


def _find_title_in_soup(soup):
    return soup.find(name="meta", property="og:title")["content"]


def _find_image_clue_in_soup(soup):
    return soup.find("link", {"href": re.compile(SCORE_SHEET_REGEX)})["href"]


def _delete_nonalphanumeric_chars(title: str) -> str:
    return "".join(c for c in title if c.isalnum())


def _clean_url(url: str) -> str:
    if "@" in url:
        return url.split("@")[0]
    elif "?" in url:
        return url.split("?")[0]
    else:
        return url
