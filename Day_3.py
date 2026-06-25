'''Given an integer array nums and an integer k, return the total number of continuous subarrays whose sum equals k.'''
def subarraySum(nums, k):
    count = 0
    prefix_sum = 0

    # Stores frequency of prefix sums
    prefix_count = {0: 1}

    for num in nums:
        prefix_sum += num

        # Check if there exists a previous prefix sum
        # such that current_sum - previous_sum = k
        if prefix_sum - k in prefix_count:
            count += prefix_count[prefix_sum - k]

        # Update frequency of current prefix sum
        prefix_count[prefix_sum] = prefix_count.get(prefix_sum, 0) + 1

    return count


# Example usage
print(subarraySum([1, 1, 1], 2))  # 2
print(subarraySum([1, 2, 3], 3))  # 2
print(subarraySum([3, 4, 7, 2, -3, 1, 4, 2], 7))  # 4
