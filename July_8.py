#1.Merge Two Sorted Lists
def mergeTwoLists(self, l1, l2):
    head = ListNode()
    curr = head
    while l1  and l2:
        if l1.val < l2.val:
            curr.next = l1
            curr = curr.next
            l1 = l1.next
        else:
            curr.next = l2
            curr = curr.next
            l2 = l2.next
    if l1 is not None:
        curr.next = l1
        curr = curr.next
        l1 = l1.next
    if l2 is not None:
        curr.next = l2
        curr = curr.next
        l2 = l2.next
    return head.next
#(time On)
#Space  o1
#2.Binary search 
def search(self, nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1
#(time O logn)
#Space  o1
#3. Find Smallest Letter Greater Than Target
def nextGreatestLetter(self, letters, target):
    if target >= letters[-1] or target < letters[0]:
        return letters[0]
    
    l, r = 0, len(letters) - 1
    while l <= r:
        pivot = (l+r)//2
        if target >= letters[pivot]:
            l = pivot + 1
        elif target < letters[pivot]:
            r = pivot - 1

    if letters[r] <= target:
        return letters[r+1]
    else:
        return letters[r]
#(time O logn)
#Space  o1