class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # temp = k
        # # avg = -999
        # avglst = []
        # len1 = len(nums)
        # if k == len1 or len1 == 1:
        #     return sum(nums)/k
        # else:
        #     for i in range(0, len1-k+1):
        #         sub = nums[i:temp]
        #         avglst.append(sum(sub)/k)
        #         # if tempAvg > avg:
        #         #     avg = tempAvg
        #         temp = temp+1
        #     return max(avglst)

        length = len(nums)
        if length == 1:
            return nums[0]
        
        start = 0
        end = k
        avg = 0
        for i in range(k):
            avg += nums[i]/k
        maxAvg = avg
        while end<length:
            avg = avg - nums[start]/k
            avg = avg + nums[end]/k
            maxAvg = max(avg, maxAvg)
            start+=1
            end+=1
        return maxAvg
        
        