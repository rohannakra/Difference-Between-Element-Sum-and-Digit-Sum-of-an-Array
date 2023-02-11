# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/

def difference_of_sum(nums):
    sum_nums = 0
    digit_sum_nums = 0

    for num in nums: 
        sum_nums += num
        for digit in str(num):
            digit_sum_nums += int(digit)
    
    return abs(sum_nums - digit_sum_nums)

print(difference_of_sum([1, 15, 6, 3]))
print(difference_of_sum([1, 2, 3, 4]))

# -------------------------------------------------------------------------------------------------------

# Accepted LeetCode Solution:

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum_nums = 0
        digit_sum_nums = 0

        for num in nums: 
            sum_nums += num
            for digit in str(num):
                digit_sum_nums += int(digit)
    
        return abs(sum_nums - digit_sum_nums)
