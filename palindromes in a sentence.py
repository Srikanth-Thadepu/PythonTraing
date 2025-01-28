import re

def give_input():
    string = input("Enter a string: ")
    return string

def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False

def main():
    palindromes = []
    string = give_input()
    # Split the string into words based on spaces, commas, dots, and question marks
    words = re.split(r'[ ,.?]+', string)
    for word in words:
        if word and is_palindrome(word):  # Check if word is not empty and is a palindrome
            palindromes.append(word)
    print("Palindromes in the string are:", palindromes)

main()
