#Sorting
#time o(nlogn)
# space o(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        return nums
        

#time 0(n)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count0=0
        count1=0
        count2=0
    
        for i in range(0,len(nums)):
            if nums[i]==0:
                count0=count0+1
        
            if nums[i]==1:
                count1=count1+1
                
            if nums[i]==2:
                count2=count2+1
                
        for i in range(0,count0):
            nums[i]=0
        for i in range(count0,count0+count1):
            nums[i]=1
        for i in range((count0+count1),len(nums)):
            nums[i]=2
            
