# Question: https://www.hackerrank.com/challenges/designer-door-mat/problem

'''
Used center() to align the design at center
Other similar functions are
ljust() - For left justification
rjust() - For right justification
'''

n, m = map(int, input().split())

# To print top portion of mat
for i in range(1, ((n-1)//2)+1):
    pattern = ".|."*(2*i-1)
    print(pattern.center(m,"-"))

# To print middle portion of mat
print("WELCOME".center(m,"-"))

# To print bottom portion of mat
for i in range(((n-1)//2), 0, -1):
    pattern = ".|."*(2*i-1)
    print(pattern.center(m,"-"))