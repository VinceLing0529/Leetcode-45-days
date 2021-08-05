#19. Remove Nth Node From End of List
def removeNthFromEnd(self, head, n):
    dummy = ListNode(0,head)
    left = dummy
    right = head
    while n > 0 and right:
        right = right.next
        n-=1
    while right:
        left = left.next
        right = right.next
    left.next = left.next.next
    return dummy.next
#148. Sort List

def sortList(self, head: ListNode) -> ListNode:
    l1 = head
    ans = list()
    
    while l1:
        ans.append(l1.val)
        l1 = l1.next
        
    ans = sorted(ans)
    l1 = head
    for i in range(len(ans)):
        l1.val = ans[i]
        l1 = l1.next
        
    return head
#143. Reorder List

def reorderList(self, head):
    slow ,fast= head,head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    second = slow.next
    slow.next = prev =None
    while second :
        temp = second.next
        second.next = prev
        prev = second
        second =temp
    first,second = head,prev
    while second:
        tmp1 ,tmp2 = first.next,second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2