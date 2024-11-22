#!/opt/homebrew/bin/python3

def main():
    count = 0
    with open('books/frankenstein.txt') as f:
        contents = f.read().split()
    return len(contents)
    


print(main())
