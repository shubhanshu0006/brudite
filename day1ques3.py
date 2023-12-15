def reverse_groups(s, K):
    if K > 1:
        cnt = 0
        start = 0
        result = ""
        for i in range(len(s)):
            if cnt != K:
                cnt += 1
            if cnt == K:
                result += s[start:i+1][::-1]
                start = i + 1
                cnt = 0
        result += s[start:][::-1]
        return result
    return s

s = input()
k = int(input())
ans = reverse_groups(s, k)
print(ans)