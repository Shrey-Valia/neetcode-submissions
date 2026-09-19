class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num,0)+1

        ranked = sorted(count.items(), key=lambda pair: pair[1])
        output = []
        for pair in ranked[-k:]:
            output.append(pair[0])
        return output