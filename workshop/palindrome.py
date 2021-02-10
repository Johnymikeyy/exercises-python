word = input("please enter a word: ")
def palindrome(word):
    if word == word[::-1]:
        return "this is palindrome"
    else:
        return "this is not a palindrome word"
palindrome(word)