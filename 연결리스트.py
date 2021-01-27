# 노드 클래스 정의
class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

# 연결리스트 클래스 정의
class LinkedList:

    # 초기화 메소드
    def __init__(self):
        dummy = Node("dummy")
        self.head = dummy
        self.tail = dummy

        self.current = None
        self.before = None

        self.num_of_data = 0

    # append 메소드 (insert - 맨 뒤에 노드 추가, tail과 node의 next, 데이터 개수 변경)
    def append(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

        self.num_of_data += 1

    # first 메소드 (search1 - 맨 앞의 노드 검색, before, current 변경)
    def first(self):
        if self.num_of_data == 0:  # 데이터가 없는 경우 첫번째 노드도 없기 때문에 None 리턴
            return None

        self.before = self.head
        self.current = self.head.next

        return self.current

    # next 메소드 (search2 - current 노드의 다음 노드 검색, 이전에 first 메소드가 한번은 실행되어야 함)
    def next(self):
        if self.current.next is None:
            return None

        self.before = self.current
        self.current = self.current.next

        return self.current.data

    # 깊은 복사를 위한 메소드 추가
    def deep_copy(self):
        copied = LinkedList()
        item = self.first()

        if item:
            copied.append(item.val)
            while True:
                item = item.next
                if item:
                    copied.append(item.val)
                else:
                    break

        return copied
#################################################################

a = LinkedList()
a.append(1)
a.append(2)
a.append(3)
a.append(4)
a.append(5)

# 깊은 복사 (deep copy)
c = a.deep_copy()

a.first().val = 10
print(a.first().val, c.first().val)

# 결과: 10 1
