def task1(a, b, c):
    return (a and b) or c

def task2(x, y):
    return x == y

def task3(a, b):
    return (a and not b) or (not a and b)

def task4(boolean_value):
    return "Hello, World!" if boolean_value else "Goodbye, World!"

def task5(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y and y != z and x != z:
        return "All different"
    else:
        return "Neither"

def task6(boolean_list):
    return sum(boolean_list)

def task7(number):
    binary_representation = bin(number)[2:]
    count_of_ones = binary_representation.count('1')
    return count_of_ones % 2 == 0

def task8(a, b, c):
    return (a + b + c) > 1

def task9(boolean_value):
    return not boolean_value

def task10(condition, if_true, if_false):
    return if_true if condition else if_false

def task11(x, y, z):
    return x or (y and z)

def task12(a, b, c):
    if a < b < c:
        return "Increasing"
    elif a > b > c:
        return "Decreasing"
    else:
        return "Neither"

def task13(boolean_list):
    return [val for val in boolean_list if val]

def task14(bool1, bool2, bool3, integer):
    result = integer
    if bool1:
        result *= 2
    if bool2:
        result *= 3
    if bool3:
        result -= 5
    return result

# Test cases
print("Task 1:", task1(True, False, True))
print("Task 2:", task2(True, True))
print("Task 3:", task3(True, False))
print("Task 4:", task4(True))
print("Task 5:", task5(3, 3, 3))
print("Task 6:", task6([True, False, True, False, True]))
print("Task 7:", task7(3))
print("Task 8:", task8(True, True, False))
print("Task 9:", task9(True))
print("Task 10:", task10(True, "Yes", "No"))
print("Task 11:", task11(True, False, True))
print("Task 12:", task12(1, 2, 3))
print("Task 13:", task13([True, False, True, False]))
print("Task 14:", task14(False, False, True, 10))
