# Input the number of students
n = int(input("Enter the number of students: "))

# Input marks for each student
marks = []
print("Enter the marks scored by each student (-1 for absent):")
for i in range(n):
    mark = int(input(f"Student {i + 1}: "))
    marks.append(mark)

# Remove absentees (-1) for calculations
valid_marks = [mark for mark in marks if mark != -1]

# Calculate average
if valid_marks:
    average = sum(valid_marks) / len(valid_marks)
else:
    average = 0

# Find highest and lowest marks
if valid_marks:
    highest = max(valid_marks)
    lowest = min(valid_marks)
else:
    highest = lowest = 0

# Count absentees
absent_count = marks.count(-1)

# Find marks with the highest frequency
if valid_marks:
    frequency = {}
    for mark in valid_marks:
        if mark in frequency:
            frequency[mark] += 1
        else:
            frequency[mark] = 1
    max_frequency = max(frequency.values())
    most_frequent_marks = [mark for mark, freq in frequency.items() if freq == max_frequency]
else:
    most_frequent_marks = []
    max_frequency = 0

# Display results
print("\nResults:")
print(f"Average score of the class: {average:.2f}")
print(f"Highest score: {highest}")
print(f"Lowest score: {lowest}")
print(f"Count of students absent: {absent_count}")
if most_frequent_marks:
    print(f"Marks with highest frequency: {most_frequent_marks} (Frequency: {max_frequency})")
else:
    print("No valid marks to determine frequency.")
