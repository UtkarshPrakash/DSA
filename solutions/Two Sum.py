class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        mem = []
        mem.extend(nums)
        l=0
        r=n-1
        nums.sort()
        while(l<r):
            add = nums[l]+nums[r]
            if add==target:
                i = nums[l]
                j = nums[r]
                break
            if add>target:
                r -= 1
            else:
                l += 1
        a = mem.index(i)
        b = mem.index(j)
        if a==b:
            b = mem.index(j, a+1)
        return [a, b]