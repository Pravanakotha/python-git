def isPalindrome(s):
    return s==s[::-1]
s= "pravana"
ans=isPalindrome(s)
if ans:
    print("yes Palindrome")
else:
    print("No Palindrome")