if __name__ == '__main__':
    n = int(input())
    student_marks = dict()
    for _ in range(n):
        user_input = input().split() # split() converts space seperated string to list items
        name = user_input.pop(0) # Pop the name of student from list & save it
        marks = list(map(float, user_input)) # Convert the remaining items of list to float type
        student_marks[name] = marks # Insert the data in dictionary
    query_name = input()
    
    avg = sum(student_marks.get(query_name)) / 3
    print("%.2f" % avg) # Precision handling for 2 decimal places
