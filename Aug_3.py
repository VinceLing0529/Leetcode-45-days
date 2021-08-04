#309. Best Time to Buy and Sell Stock with Cooldown


def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    if not n: 
        return 0
    
    s0, s1, s2 = [0] * n, [0] * n, [0] * n 
    
    s0[0] = 0
    s1[0] = -prices[0] 
    s2[0] = 0 
    
    for i in range(1, n):
        s0[i] = max(s0[i-1], s2[i-1])
        s1[i] = max(s1[i-1], s0[i-1] - prices[i])
        s2[i] = s1[i-1] + prices[i]
    
    return max(s0[-1], s2[-1])

#142. Linked List Cycle II
def detectCycle(self, head):
    li = []
    while True:
        li.append(head)
        if head == None or head.next ==None:
            return None
        head = head.next
        if head in li:
            return 
            
def detectCycle(self, head):
    slow = head
    fast = head 
    while fast and fast.next:

        slow = slow.next
        fast = fast.next.next
        if slow == fast :
            break
    while slow and slow.next:
        if head == slow:
            return head
        slow = slow.next
        head = head.next

    return None
    
def addTwoNumbers(self, l1, l2):
    total = l1.val + l2.val
    rem = total // 10
    whole = total % 10
    new_head = ListNode(whole)
    t = new_head
    l1 = l1.next
    l2 = l2.next
    
    while l1 != None or l2 != None:
        if l2 == None:
            total = l1.val + rem
            l1 = l1.next
        elif l1 == None:
            total = l2.val + rem
            l2 = l2.next
        else:
            total = l1.val + l2.val + rem
            l1 = l1.next
            l2 = l2.next
            
        rem = total // 10
        whole = total % 10  
            
        t.next = ListNode(whole)
        t = t.next
    if rem:
        t.next = ListNode(rem)
    return new_head
