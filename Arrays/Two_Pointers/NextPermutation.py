from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if self.is_lexicographically_sorted(nums):
            print("It is in order...")
            pnt1 = None
            for i in range(len(nums)):
                if nums[i - 1] < nums[i]:
                    pnt1 = i - 1

            diff = None
            # to_swap = None
            swap_pointer = None
            for j in range(pnt1 + 1, len(nums)):
                if nums[pnt1] < nums[j]:
                    if diff is None:
                        diff = nums[j] - nums[pnt1]
                        # to_swap = nums[j]
                        swap_pointer = j
                    else:
                        if diff > (nums[j] - nums[pnt1]):
                            # to_swap = nums[j]
                            diff = nums[j] - nums[pnt1]
                            swap_pointer = j

            # Swap elements
            temp = nums[pnt1]
            nums[pnt1] = nums[swap_pointer]
            nums[swap_pointer] = temp

            # reverse a subsection of a list
            nums[pnt1 + 1 : len(nums)] = nums[pnt1 + 1 : len(nums)][::-1]
            return nums

        else:
            # reverse a subsection of a list
            nums = nums[::-1]
            return nums

    def is_lexicographically_sorted(self, nums: List[int]) -> bool:
        return nums == sorted(nums)


nums = [3, 2, 1]
obj = Solution()
print(obj.nextPermutation(nums))
