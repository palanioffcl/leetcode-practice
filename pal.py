import re

def isPalindrome(s):
    s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    print(s)
    x = ""
    for i in range(len(s)-1, -1, -1):
        x += s[i]    
    return True if x == s else False

print(isPalindrome("0P"))



#AmanaplanacanalPanama
#amanaPlanacanalpanamA
