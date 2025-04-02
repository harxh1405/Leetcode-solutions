class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j = 0,0
        sorted = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                sorted.append(nums1[i])
                i+=1
            else:
                sorted.append(nums2[j])
                j+=1
        sorted.extend(nums1[i:m])
        sorted.extend(nums2[j:])
        nums1[:] = sorted
        

        