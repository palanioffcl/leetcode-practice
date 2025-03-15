def romanToInt(s):
    letters = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    ans = 0
    for i in s:
        ans += letters[i]
    return ans

print(romanToInt("MCMXCIV"))
