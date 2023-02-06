from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n  = len(nums)
        i = 0
        j = len(nums) -1
        out  = [0] * n

        for p in range(len(out)-1,-1, -1):

            if abs(nums[i]) < abs(nums[j]):
                out[p] = abs(nums[j])**2
                j -= 1
            elif abs(nums[i]) > abs(nums[j]):
                out[p] = abs(nums[i])**2
                i += 1
            else:
                out[p] = abs(nums[i])**2
                i+=1
        return out

obj = Solution()
output = obj.sortedSquares([-10, -5, 1, 2,4, 7])
print(output)
