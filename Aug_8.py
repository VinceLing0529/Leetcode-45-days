#92. Reverse Linked List II
def reverseBetween(self, head, left, right):
    if left == right :return head
    curr = head
    prev = None
    for i in range(left-1):
        prev = curr
        curr = curr.next
    he = prev
    tail = curr
    next = None
    for i in range(right-left +1):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    if he is not None:
        he.next = prev
    else:
        head = prev
    tail.next = curr
    return head
#61. Rotate List
def rotateRight(self, head, k):
    size = 0
    x = head
    while x:
        size +=1
        x = x.next
    if size <= 1 or k == 0 or k ==size:
        return head
    prev = None
    curr = head
    mov = size  - (k%size)
    if mov %size == 0 : return head
    for i in range(mov):
        prev = curr
        curr = curr.next
    newHead = curr
    prev.next =None
    
    while curr.next:
        curr = curr.next
    curr.next = head
    return newHead
#24. Swap Nodes in Pairs
def swapPairs(self, head):
    if head == None or head.next == None:
        return head

    recur = head.next.next
    first = head
    head = head.next
    head.next = first
    head.next.next = self.swapPairs(recur)
    return head