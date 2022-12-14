s = '123456789'

i = 0
while i<len(s):
    j = i + 1
    count = 1
    if j < len(s):
        while s[j] == s[i]:
            count += 1
            if j+1 < len(s):
                j += 1
            else:
                break
    if s[i-1] == s[i]:
        pass
    else:
        print(tuple([count, int(s[i])]), end = ' ')
    # print(i)
    i = j