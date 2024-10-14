
def get_book(path):
    with open(path, 'r') as f:
        data = f.read()
    return data

def get_word_count(book):
    words = book.split()
    return len(words)

def get_letter_count(book):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    return {char: book.lower().count(char) for char in chars}

def main():
    path = 'books/frankenstein.txt'
    book = get_book(path)
    word_count = get_word_count(book)
    letter_count = get_letter_count(book)
    
    print(f'--- Begin report of {path} ---')
    print(f'{word_count} words found in the document')
    print()
    for char in sorted(letter_count, key=letter_count.get)[::-1]:
        print(f"The letter '{char}' character was found {letter_count[char]} times")
    print('--- End report ---')

if __name__ == '__main__':
    main()