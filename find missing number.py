""" Find missing number form the list """

nums = [1, 2, 3, 5, 6]   # Missing 4

n = 6  # Maximum number

expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

missing = expected_sum - actual_sum

print("Missing number:", missing)
