s = '122344556'

i = 0
while i < len(s):
    j = i + 1
    count = 1
    while j < len(s):
        if s[j] == s[i]:
            count += 1
            j += 1
        else:
            break
    print(tuple([count, int(s[i])]), end = ' ')
    i = j