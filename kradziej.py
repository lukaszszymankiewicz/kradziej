from utils import (
    make_folder,
    determine_extension,
    get_sheet_page_name,
    get_url_content,
    get_score_image_name,
    create_soup,
    get_song_title_from_soup,
    get_first_sheet_page_image_url_from_soup,
    save_svg_image_to_png,
    save_png_image,
    get_number_of_pages_from_soup,
)


def get_scores_from_url(url: str):
    page_content = get_url_content(url)
    soup = create_soup(page_content)

    song_title = get_song_title_from_soup(soup)

    base_image_url = get_first_sheet_page_image_url_from_soup(soup)

    image_extension = determine_extension(base_image_url)
    number_of_pages = get_number_of_pages_from_soup(soup)

    make_folder(song_title)

    for page_number in range(number_of_pages):
        score_url = get_sheet_page_name(base_image_url, page_number)
        image = get_url_content(score_url)
        path = get_score_image_name(song_title, page_number)

        if image_extension == "svg":
            save_svg_image_to_png(image, path)

        elif image_extension == "png":
            save_png_image(image, path)
