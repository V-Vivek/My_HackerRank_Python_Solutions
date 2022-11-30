# Question: https://www.hackerrank.com/challenges/text-wrap/problem

def wrap(string, max_width):
    count = max_width
    i = 0
    result = ""
    while(i < len(string)):
        while(count!=0 and i < len(string)):
            result += string[i]
            count-=1
            i+=1
        count=max_width
        result += "\n"
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)