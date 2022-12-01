# Question: https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    n = len(string)
    temp = string
    while(len(temp)>0):
        temp2 = list(temp[:k])
        
        # To check & print only unique charecters
        temp3 = []
        for _ in temp2:
            if _ in temp3:
                continue
            temp3.append(_)
            print(_, end ="")
        print() # print new line
        temp3 = [] # Set temp3 to blamk for next substring
        temp = temp[k:] # splice the string


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)