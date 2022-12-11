def check_palindrome(word):
    word = word.lower()
    for i in range(len(word)):
        if word[i] != word[-i-1]:
            return False
    return True

print(check_palindrome("Kobyłałybok"))