def isPalindrome(s):
    return s==s[::-1]
s= "pravana"
ans=isPalindrome(s)
if ans:
    print("yes")
else:
    print("no")