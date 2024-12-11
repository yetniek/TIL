def solution(nums):
    answer = 0
    n = len(nums) // 2
    nums = len(set(nums))
    answer = min(nums, n)
    return answer