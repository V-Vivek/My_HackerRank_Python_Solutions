# Question : https://www.hackerrank.com/challenges/list-comprehensions/problem

if __name__ == '__main__':
	x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # Note that space sepearted multiple list comprehesions are used to get the coordinates
    result = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
	
print(result)
