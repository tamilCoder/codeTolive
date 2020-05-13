def maxSubArray(nums)
        if not nums: #Checking the corner cases
            return 0
        currsum = maxsum = nums[0]              #Initializing with 1st element
        for i in nums[ 1 :] :                   # running from 1 to length
            if currsum > 0 :                    # checking if currsum is positive
                currsum += i
                
            else:
                currsum = i
            maxsum=max(maxsum,currsum)          # keeping track of maximum sum
     
        return maxsum
        
 maxSubArray([3,-3,2,0,-1,2,-4,2,1])
