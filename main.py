def main():
    with open('books/frankenstein.txt') as file:
        contents = file.read()
        words_count = count_words(contents)
        chars_count = count_chars(contents)
        report = make_report(words_count, chars_count)
        print(report)

def count_words(text):
    words_list = text.split()
    return len(words_list)

def count_chars(text):
    chars = dict()

    for char in text:
        lowercased_char = char.lower()
        if(lowercased_char in chars):
            chars[lowercased_char] += 1
        else: 
            chars[lowercased_char] = 0

    return chars

def make_report(words_count, chars_count):
    report = "--- Begin report of books/frankenstein.txt ---\n"
    report += f"{words_count} words found in the document\n\n"

    for char, count in chars_count.items():
        if(not char.isalpha()): 
            continue
        report += f"The '{char}' character was found {count} times\n"


    report += '--- End report ---'

    return report

main()
