s = "uhgxusrtgqitrtpiuqxmpdmyumdputxumlxnrnfwgeuslwdysxhucykkmzfdourroagoan"
s = sorted(s)
for i in range(1,len(s)):
    if(s[i-1] != s[i] and s[i] != s[i+1]):
        #return s[i]
        print(s[i])
    else:
        print("$")
        #return '$'
