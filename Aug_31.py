#75. Sort Colors

    def sortColors(self, a: List[int]) -> None:
        runner = 0
        left_partition = 0
        right_partition = len(a) - 1
        while runner <= right_partition:
            if a[runner] == 0:
                a[runner], a[left_partition] = a[left_partition], a[runner]
                runner += 1
                left_partition += 1
            elif a[runner] == 1:
                runner += 1
            else:
                a[runner], a[right_partition] = a[right_partition], a[runner]
                right_partition -= 1
        return a
#11. Container With Most Water
def maxArea(self, height: List[int]) -> int:
    res = 0
    left = 0
    right = len(height) -1
    while left < right:
        area = (right - left) * min(height[left],height[right])
        res = max(res,area)
        if height[left] < height[right]:
            left +=1
        else:
            right -=1
    return res