#!/usr/bin/env python3


from pprint import pprint   # DEBUG
import lxml.html
import os.path
import random
import requests
import time


def main():
    # Set UA for all requests (be polite to Mozilla).
    headers = {
        'User-Agent': 'css_properties_crawler',
        'From': 'ryanboehning@gmail.com',
        'Accept-Encoding': 'gzip, deflate'
    }

    # Scrape links to CSS property pages from MDN.
    urls = get_property_links(headers)

    # Shuffle the URLs so the scrape is less obvious.
    random.shuffle(urls)

    # Visit the URLs one by one and check if they contain the text
    # '<length>'. If so, append the page title to a list.
    properties = []
    for url in urls:
        try:
            page = requests.get(url, headers=headers)
        except requests.TimeoutError as err:
            print(err)
            print(url)

        if page.status_code == 200:
            css_property = os.path.basename(url)
            if contains_length_tag(html_text=page.text):
                properties.append(css_property)
                print('CSS length property found:', css_property)
            else:
                print('CSS length property not found:', css_property)
        else:
            print('Page not found:', page.url)

        # Wait 5 seconds to avoid spamming the MDN page with requests.
        # This is the recommended delay from the MDN robots.txt file.
        time.sleep(5)

    # Write the list of <length> properties to a file.
    properties.sort()
    properties_text = '\n'.join(properties)

    with open('length_properties.txt', mode='w', encoding='UTF-8') as out_file:
        out_file.write(properties_text)


def get_property_links(headers):
    ref_page = requests.get('https://developer.mozilla.org/en-US/docs/Web/CSS/Reference',
                            headers=headers)
    if ref_page.status_code != 200:
        print('error: received status code {} when connecting to MDN '
              'page'.format(ref_page.status_code))
        return

    # Convert raw HTML code to an lxml HTML tree object.
    tree = lxml.html.fromstring(ref_page.text)

    # Every link under .index is a CSS property.
    a_tags = tree.xpath('//div[@class="index"]//a')

    # Extract URLs from all the anchor tags and combine them with the
    # base URL.
    return ['http://developer.mozilla.org' + a.get('href') for a in a_tags]


def contains_length_tag(html_text):
    '''Extracts the Values section of an MDN CSS Reference Page.

    The Mozilla Developer Network has an exhaustive list of CSS
    properties. Each property has its own page, which contains a Values
    section which contains a definition list (<dl>) of all the possible
    values for that property. This function scans Values for <length>.
    '''
    # Convert the raw HTML from a string to an ElementTree HTML object.
    tree = lxml.html.fromstring(html_text)

    # Select the <dl> elements
    dls = tree.xpath('//*[@id="wikiArticle"]/dl')

    # Loop through the <dl> and search for '<length>'.
    for dl in dls:  # Just in case there are more than one
        for elem in dl.iterdescendants():
            if '<length>' in elem.text_content():
                return True

    return False


if __name__ == '__main__':
    main()
