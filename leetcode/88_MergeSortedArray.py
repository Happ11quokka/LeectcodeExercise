''' 
1. 주어진 두 배열 
- nums1: 크기가 m + n; 처음 m개의 요소만 유효값(정렬된), 
나머지 n개의 요소는 병합을 위한 빈 공간이며 0으로 채워진다 
- nums2: 크기가 n인 배열, 모든 요소가 주어진 상태이고 , 정렬됨 
2. 제약 조건: 
- 병합 결과는 nums1 배열에 저장되어야 하고, 배열 길이는 m+n, 정렬이 되어야 한다

*** 이런걸 역순 병합 이라고 한다 - 뒤에서 부터 
        시간 복잡도는 O(m+n)
'''

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # init pointer - tuple init method
        p1, p2, p = m - 1, n - 1, m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

solution = Solution()
solution.merge(nums1, m, nums2, n)
print(nums1)
