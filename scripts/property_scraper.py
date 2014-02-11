#!/usr/bin/env python3


import lxml.html
import requests


def main():
    page = requests.get('https://developer.mozilla.org/en-US/docs/Web/CSS/Reference')
    if page.status_code != 200:
        print('error: received status code {} when connecting to MDN '
              'page'.format(page.status_code))
        return

    # Convert raw HTML code to an lxml HTML tree object.
    tree = lxml.html.fromstring(page.text)

    # Every link under .index is a CSS property.
    links = tree.xpath('//div[@class="index"]//a')

    # Get the anchor text from every link and make a big string with
    # each property separated by newlines.
    properties = '\n'.join([link.text_content() for link in links])

    # Write the properties to a file.
    with open('scraped_properties.txt', mode='w', encoding='UTF-8') as out_file:
        out_file.write(properties)


if __name__ == '__main__':
    main()
