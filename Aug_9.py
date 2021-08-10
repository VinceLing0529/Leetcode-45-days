#373. Find K Pairs with Smallest Sums
def kSmallestPairs(self, nums1, nums2, k):
    if not nums2 or not nums1: return []
    heap = []
    heapq.heapify(heap)
    for i, num1 in enumerate(nums1[:k]):
        for num2 in nums2[:k//(i+1)]:
            heapq.heappush(heap, [num1+num2, num1, num2])
    return [x[1:] for x in heapq.nsmallest(k, heap)]
#378. Kth Smallest Element in a Sorted Matrix
def kthSmallest(self, matrix, k):
    l,r,N  = matrix[0][0], matrix[-1][-1],len(matrix)
    def less_k(m):
        cnt = 0
        for r in range(N):
            x = bisect_right(matrix[r],m)
            print(x)
            cnt+=x
        return cnt
    while l<r:
        mid = (l+r)//2
        if less_k(mid)<k:
            l = mid +1
        else:
            r = mid
    return l 
#328. Odd Even Linked List
def oddEvenList(self, head):
    
    odd = ListNode(0)
    even = ListNode(0)
    oddhead = odd
    evenhead = even
    isOdd = True
    while head:
        if isOdd:
            odd.next = head
            odd = odd.next
        else:
            even.next = head
            even  = even.next
        isOdd = not isOdd
        head = head.next
    even.next = None
    odd.next = evenhead.next
    return oddhead.next