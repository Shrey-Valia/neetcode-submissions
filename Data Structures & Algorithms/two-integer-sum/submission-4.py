class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Target -  num[i] = new_num
        #check if new_num is in nums
        output = []
        for i in nums:
            diffrence = target - i
            index = nums.index(i)
            nums.remove(i)
            if diffrence in nums:
                print(nums)
                output.append(index)
                output.append(nums.index(diffrence)+1)
                return output
            nums.insert(index,i)
            # elif diffrence in nums:
            #     output.append(index)
            #     nums.remove(i)
            #     output.append(nums.index(diffrence)+1)
            #     return output