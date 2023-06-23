class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        outnums=[]
        for i in range(n):
            outnums.append(nums[i])
            outnums.append(nums[n+i])
        return outnums