sentence = "hellohello hellohellohello"
searchWord = "ell"
N = len(searchWord)
isFound = 0

if(searchWord not in sentence):
    return -1
    #print(-1)
else:
    sentence = sentence.split(" ")
    for i in range(len(sentence)):
        if(sentence[i][:N] == searchWord):
            isFound = i+1
            break                

if(isFound == 0):
    return -1
else:
    return isFound
