def reverse_groups(s, K):
    if K > 1:
        cnt = 0
        st = 0
        r = ""
        for i in range(len(s)):
            if cnt != K:
                cnt += 1
            if cnt == K:
                r += s[start:i+1][::-1]
                st = i + 1
                cnt = 0
        result += s[st:][::-1]
        return r
    return s

s = input()
k = int(input())
ans = reverse_groups(s, k)
print(ans)
