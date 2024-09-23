def read_file():
    book = "books/frankenstein.txt"
    with open(book) as f:
        file_contents = f.read()
    word_count(file_contents)
    char_count(file_contents)
    return (file_contents)