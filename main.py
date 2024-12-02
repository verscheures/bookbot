def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letter = {}
    for c in text:
        if c.isalpha() is False:
            continue
        if c.lower() in letter:
            letter[c.lower()] += 1
        else:
            letter[c.lower()] = 1
    return letter


def main():
    filename = "books/frankenstein.txt"
    with open(filename) as f:
        text = f.read()
    print(f"The report of {filename}")
    print(f"There are {count_words(text)} words in the text.")
    letters = count_letters(text)
    for letter, count in letters.items():
        print(f"Letter {letter} appears {count} times in the text.")
    print("End of report.")


main()
