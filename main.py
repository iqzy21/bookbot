def read_file():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
    word_count(file_contents)
    char_count(file_contents)
    return (file_contents)

def word_count(text):
    words = text.split()
    return (len(words))

def char_count(text):
    letters = {}
    lowered_text = text.lower()

    for char in lowered_text:
        if char.isalpha():
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
    sort(letters)
    return(letters)

