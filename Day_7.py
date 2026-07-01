'''Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

You may assume that each input has exactly one solution, and you may not use the same element twice.

Return the answer in any order.

Example 1

Input

nums = [2, 7, 11, 15]
target = 9

Output
[0, 1]'''
def twoSum(nums, target):
    seen = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in seen:
            return [seen[complement], i]

        seen[nums[i]] = i


# Example
nums = [2, 7, 11, 15]
target = 9

print(twoSum(nums, target))
