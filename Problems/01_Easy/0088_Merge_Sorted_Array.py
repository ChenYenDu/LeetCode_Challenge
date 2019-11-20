class Solution1:
    '''
    1. put nums2 into nums1
    2. sort new nums1 -> bubble sort
    --> Really Slow!!
    '''

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        for i in range(n):
            nums1[m+i] = nums2[i]

        for j in range(len(nums1)):
            for k in range(j+1, len(nums1)):
                if nums1[j] > nums1[k]:
                    temp = nums1[j]
                    nums1[j] = nums1[k]
                    nums1[k] = temp


class Solution2:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        '''
            solution from someone else
        '''
        nums1[m:] = nums2
        nums1.sort()


class Solution3:
    '''
            solution from someone else, which i somehow couldn't figure out.
    '''

    def merge(self, nums1, m, nums2, n):
        while n > 0:
            if m <= 0 or nums2[n-1] >= nums1[m-1]:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            else:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
