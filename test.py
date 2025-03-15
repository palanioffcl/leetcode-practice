def canConstruct(ransomNote, magazine):
    res = False
    for i in ransomNote:
        if(i in magazine and len(magazine.split(i)) >= len(ransomNote.split(i))):
            res = True
        else:
            res = False
            break
    return res

print(canConstruct("fihjjjjei","hjibagacbhadfaefdjaeaebgi"))
