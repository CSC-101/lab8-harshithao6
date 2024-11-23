
#Task 1
#input: list of integers
#output: list of integers
#purpose: to sort everything in groups of 3
def groups_of_3(numbers: list[int]):
    grouped = []
    for i in range(0, len(numbers), 3):
        grouped.append(numbers[i:i + 3])
    return grouped






