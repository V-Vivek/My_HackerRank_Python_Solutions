def minion_game(string):

    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    vowels_score = 0
    consonants_score = 0
    l = len(string)

    for i in range(l):
        if string[i] in vowels:
            vowels_score += len(string[i:l])
        else:
            consonants_score += len(string[i:l])


    if consonants_score > vowels_score:
        print('Stuart', consonants_score)
    elif consonants_score < vowels_score:
        print('Kevin', vowels_score)
    else:
        print('Draw')
    print(vowels_score)
    print(consonants_score)


if __name__ == '__main__':
    s = input()
    minion_game(s)