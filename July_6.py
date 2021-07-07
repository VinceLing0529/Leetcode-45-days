#1.Linked List Cycle
class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return False
        slow  = head
        fast  = head.next
        while slow != fast:
            if fast is None or fast.next is None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True
#Time O(n)
#Space O(1)

#2.Fast and slow pointer
def middleNode(self, head):
    li = []
    while head is not None:
        li.append(head)
        head= head.next
    return li[len(li)/2]
        
#Time O(n)
#Space O(n)

def middleNode(self, head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
        
#Time O(n)
#Space O(1)

#3.Palindrome Linked List
def isPalindrome(self, head):
    li = []
    while head:
        li.append(head.val)
        head = head.next
    return li == li[::-1]
#Time O(n)
#Space O(n)

def isPalindrome(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None        
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp
        print(prev)
    while prev:
        if prev.val != head.val:
            return False
        prev= prev.next
        head = head.next
    return True
            
#Time O(n)
#Space O(1)