#######################################################################
# Definition for singly-linked list.
#######################################################################
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def add(data):
    node = head
    while node.next:
        node = node.next
    node.next = ListNode(data)

# 노드 연결
nodeStart = ListNode("head시작")
head = nodeStart
# 노드에 1~9까지 데이터를 순서대로 넣음
for data in range(1,6):
    add(data)

node = head # 연결된 노드들을 출력하기에 앞서 처음 시작한 head부분을 알아야 검색 가능
while node.next: # 노드에 포인터가 가리키는게 없을때까지 반복
    print(node.val)
    node = node.next
print(node.val)
#######################################################################
# 13. 팰린드롬 연결리스트 (리트코드234.) *
# 연결 리스트가 팰린드롬 구조인지 판별하라.
# input = 1->2
# output = false
# Input: 1->2->2->1
# Output: true
# 설명 : Could you do it in O(n) time and O(1) space?
#######################################################################
def isPalindrome(head: ListNode) -> bool:
    q: List = []
    if not head:
        return True

    node = head
    #리스트변환
    while node is not None:
        q.append(node.val)
        print(node.val)
        node = node.next
    #팰린드롬판별
    while len(q) > 1:
        if q.pop(0) != q.pop(0):
            return False
    return True

isPalindrome()

# Deque
def isPalindrome_deque(head: ListNode) -> bool:
    q: Deque = collections.deque() #Deque로 수정
    if not head:
        return True

    node = head
    #리스트변환
    while node is not None:
        q.append(node.val)
        node = node.next
    #팰린드롬판별
    while len(q) > 1:
        # Deque로 수정
        if q.popleft(0) != q.pop(0):
            return False
    return true


def isPalindrome_rev(head: ListNode) -> bool:
    rev = None
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        slow, rev = slow.next, rev.next
    return not rev

    return true
#######################################################################
# 14. 두 정렬 리스트의 병합 (리트코드21.) *
# 정렬되어 있는 두 연결 리스트를 합쳐라
# input = 1->2->4, 1->3->4
# output = 1->1->2->3->4->4
# Input: 1->3->4
# Output: true
# 설명 : Could you do it in O(n) time and O(1) space?
#######################################################################
def mergeTwoLists(self, l1:ListNode, l2:ListNode) -> ListNode:
    if (not l1) or (l2 and l1.val > l2.val):
        l1, l2 = l2, l1
    if l1:
        l1.next = self.mergeTwoLists(l1.next,12)
    return l1
#######################################################################
# 15. 역순연결리스 (리트코드206.) *
# 연결리스트를 뒤집어라
# input = 1->2->3->4->5->NULL
# output = 5->4->3->2->1->NULL
#
#######################################################################
"""
1|2 -- 2|3 -- 3|4 -- 4|5 -- 5|None
5|4 -- 4|3 -- 3|2 -- 2|1 -- 1|None
"""
def reverseList(head: ListNode) -> ListNode:
    node, prev = head, None

    while node:
        next, node.next = node.next, prev
        prev, node = node, next
    return prev

"""
node : 1|2
prev : None
--------------------------------1 - 1|2
118
next : 2를 가리키는 2|3
node.next : None

119
prev : 1|None
node : 2를 가리키는 2|3
------------------------------2 - 2|3
118
next : 3를 가리키는 3|4
node.next : 1|None

119
prev : 2|1
node : 3를 가리키는 3|4
"""

###########################################
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

reverseList(node1)

############################### id 주소값 보기
node = node5 #node5
while node:
    print("{} : {} | {}".format(node.val,id(node),id(node.next)))
    node = node.next


############################## 객체로 바로 보기
node = node1
while node:
    print("{} : {} | {}".format(node.val,node,node.next))
    node = node.next
