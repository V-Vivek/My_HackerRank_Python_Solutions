# Question : https://www.hackerrank.com/challenges/nested-list/problem
if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    scores = list({x[1] for x in records}) # To extract unique scores
    scores.sort() # To sort scores
    second_lowest = scores[1] 
    names = [x[0] for x in records if x[1] == second_lowest] # Extract student names with second_lowest score
    names.sort() # Sort names alphabetically
    for name in names:
        print(name)
