#Define a is_palindrome function will take the input as a string and returns true else false

#palindrome means which will return the same string when u read from backside

def is_palindrome( str1):
    reverse = str1[-1::-1]
    if str1 == reverse:
        return True
    return False

def is_palindrome(str1):
    return str1 == str1[::-1]

print(is_palindrome("kamak"))
print(is_palindrome("kamal"))