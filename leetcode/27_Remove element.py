''' 
1. 주어진 정수 배열 nums ,정수 val 

nums에서 값이 val과 같은 요소를 “제거”하여야 하며, 
결과적으로 nums 배열의 맨 앞에 val과 같지 않은 요소들이 연속적으로 위치

- 배열의 순서는 변경될 수 있다 
- 	nums 배열의 길이는 문제 해결 후에도 고정되며, 남은 요소 뒤에 나머지 요소는 중요하지 않는다
- 최종적으로, val이 아닌 요소의 개수를 반환  (	반환값은 nums 배열 내에서 val이 아닌 값의 개수 (k))

시간 복잡도 O(n)
'''
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p1 = 0
        for p2 in range(len(nums)):
            if nums[p2] != val:
                nums[p1] = nums[p2]
                p1 += 1
        return p1


nums = [3, 2, 2, 3]
val = 3

solution = Solution()
k = solution.removeElement(nums, val)
print(k)
print(nums[:k])
