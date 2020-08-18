FIRST_PAGE_NAME = "score_0"
PAGE_NAME = "score_"
EXTENSION = ".png"
SEPARATOR = "/"


def get_sheet_page_name(url: str, page_number: int) -> str:
    page_name = _create_sheet_page_name(page_number)
    return url.replace(FIRST_PAGE_NAME, page_name)


def get_score_image_name(title: str, page_number) -> str:
    return title + SEPARATOR + PAGE_NAME + str(page_number) + EXTENSION


def _create_sheet_page_name(page_number: int) -> str:
    return PAGE_NAME + str(page_number)
