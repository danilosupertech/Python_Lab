def is_palindrome(s: str) -> bool:
    str_reverse = s[::-1].lower().replace(' ', '')
    return str_reverse == s.lower().replace(' ', '')


print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("hello world"))                 # False
print(is_palindrome("Was it a car or a cat I saw"))  # True
