def timeConversion(s):
    res = s
    if ("PM" in res):
        res = res.replace("PM", "")
        if("12" not in res):
            res = res.replace(res[:2], str(12+int(res[:2])))
    else:
        res = res.replace("AM", "")
        if ("12" in res):
            res = res.replace(res[:2], "00")
    return res

print(timeConversion("12:45:54PM"))
