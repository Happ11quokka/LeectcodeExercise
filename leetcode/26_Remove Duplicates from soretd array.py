'''
1. 주어진 정렬된 정수 배열 nums,
이 배별에서 중복된 요소를 제거하여 각 고유 요소가 배열의 처음 부분에 나타나도록
in-place 제자리에서 변경.
2.  중복 제거 후의 배열은 처음 k개의 요소ㅏㄴ다 가 고유한 요소로 채워져 ㅎ
중복을 제거한 후의 배열 크기(고유 요소의 개수)를 k 반환

'''
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 0
        p2 = p1 + 1
        for p2 in range(1, len(nums)):
            if nums[p1] != nums[p2]:
                p1 += 1
                nums[p1] = nums[p2]
        return p1 + 1


nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
solution = Solution()
k = solution.removeDuplicates(nums)

print(k)
print(nums[:k])
