def task1(arr):
    return sum(x ** 2 for x in arr)

def task2(arr):
    avg = sum(arr) / len(arr)
    return sum(x for x in arr if x >= avg)

def task3(arr):
    return sorted(arr, key=lambda x: (-arr.count(x), x))

def task4(arr):
    n = len(arr) + 1
    total_sum = n * (n + 1) // 2
    return total_sum - sum(arr)

def task5(nums):
    num_set = set(nums)
    max_length = 0
    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            max_length = max(max_length, current_length)
    return max_length

def task6(nums, k):
    k %= len(nums)
    return nums[-k:] + nums[:-k]

def task7(nums):
    result = []
    left_product = 1
    for num in nums:
        result.append(left_product)
        left_product *= num
    right_product = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] *= right_product
        right_product *= nums[i]
    return result

def task8(nums):
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

def task9(matrix):
    if not matrix:
        return []
    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result

def task10(points, k):
    return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]

print(task1([1, 2, 3]))
print(task2([1, 2, 3, 4, 10]))
print(task3([4, 6, 2, 6, 4, 4, 6]))
print(task4([1, 2, 4, 5]))
print(task5([100, 4, 200, 1, 3, 2]))
print(task6([1, 2, 3, 4, 5], 2))
print(task7([1, 2, 3, 4]))
print(task8([-2,1,-3,4,-1,2,1,-5,4]))
print(task9([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(task10([(1, 2), (1, 1), (3, 4)], 2))
