def isCircularSentence(sentence):
    listSentences = list(sentence.split(' '))
    res = 1
    if(len(listSentences) == 1 and listSentences[0][-1] != listSentences[0][0]):
        return False
    else:
        for i in range(len(listSentences)-1):
            if(listSentences[i][-1] == listSentences[i+1][0]):
                pass
            elif(i == (len(listSentences)-2) and sentence[-1] == sentence[0]):
                print("hii")
                pass
            else:
                res = 0
                break
            
    return bool(res)

print(isCircularSentence("Leetcode eisc cool"))
