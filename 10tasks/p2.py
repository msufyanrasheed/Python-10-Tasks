word = "Programming"

print(word[::-1])

first_three = word[:3]
last_three = word[-3:]
print(first_three, last_three)

print(word.count('m'))

def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("level"))
print(is_palindrome("python"))
