#!/usr/bin/env python3


def main():
    with open('css_value_keywords.txt', encoding='UTF-8') as keyword_file:
        file_as_string = keyword_file.read()

    # Split on newlines
    keyword_list = file_as_string.split()

    # Filter duplicates and sort the list
    unique_keywords = list(set(keyword_list))
    unique_keywords.sort()

    # Write out the unique list of keywords with one keyword on each line
    with open('unique_keywords.txt', mode='w', encoding='UTF-8') as out_file:
        for word in unique_keywords:
            out_file.write(word + '\n')


if __name__ == '__main__':
    main()
