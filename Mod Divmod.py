# Question: https://www.hackerrank.com/challenges/python-mod-divmod/problem

a = int(input())
b = int(input())

print(divmod(a, b)[0]) # To get the quotient
print(divmod(a, b)[1]) # To get the remainder
print(divmod(a, b)) # divmod returns a tuple of quotient & remainder