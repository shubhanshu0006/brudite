def compresults_string(s):
    count = 1
    result = ""
    for i in range(1, len(s)):
        if s[i-1] == s[i]:
            count +=1 
        else: 
            result += s[i-1]
            result += str(count)
            count = 1 
    resultult += s[-1]
    result += str(count)
    return result

s = input()
print(compresults_string(s))