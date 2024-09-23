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

def sort(dict):
    char_list = []
    for char, count in dict.items():
        char_list.append((char,count))
    char_list.sort(key=lambda x: x[1], reverse=True)
    for char, count in char_list:
        return char_list
    
def main():
    print("--- Begin report of books/frankenstein.txt ---")
    text = read_file()

    count = word_count(text)
    print(f"{count} words found in the document")

    
    count_char = char_count(text)
    sorted_chars = sort(count_char) 

    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")
    
main()   

