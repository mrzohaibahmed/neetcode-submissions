class Solution:
    def majorityElement(self, nums):
        count ={}
        n=len(nums)
        half =n/2
        for num in nums:
            count[num]=count.get(num,0)+1
            if count[num]>half:
                return num
        return -1