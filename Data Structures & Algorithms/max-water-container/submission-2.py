class Solution:
    def maxArea(self, heights: List[int]) -> int:
        edge_one = 0
        edge_two = len(heights)-1
        area_max =0 
        for i in range(0,len(heights)):
            if heights[edge_one] < heights[edge_two]:
                height = heights[edge_one]
                edge_one += 1
            else:
                height = heights[edge_two]
                edge_two -= 1
            area = (len(heights)-i-1 )*height
            print(area)
            if area_max < area:
                area_max =area
        return area_max
            



        # biggest = max(heights)
        # max_i = heights.index(biggest)
        # print (max_i)
        # area_max = 0
        # for i in range(0,len(heights)):
        #     distance = abs(max_i - i)
        #     area = distance * heights[i]
        #     print(area)

        #     if area > area_max:
        #         area_max = area
        # return area_max
            

        