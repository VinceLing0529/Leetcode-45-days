#203. Remove Linked List Elements
def removeElements(self, head, val):
    while head and head.val == val:
        head = head.next
    curr = head
    while curr and curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
#(time On)
#Space  o1
#83. Remove Duplicates from Sorted List


def deleteDuplicates(self, head):
    if head == None or head.next == None:
        return head
    while head and head.next and head.next.val == head.val:
        head = head.next
    curr = head
    while curr and curr.next:
        if curr.next.val == curr.val:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head

#(time On)
#Space  o1

def reverseList(self, head):
    prev = None        
    while head:
        temp = head.next
        head.next = prev
        prev = head
        head = temp
    return prev
#(time On)
#Space  o1