nums = [10, 20, 30, 50, 60]   # Missing 4

n = 6  # Maximum number

expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)

missing = expected_sum - actual_sum

print("Missing number:", missing)
