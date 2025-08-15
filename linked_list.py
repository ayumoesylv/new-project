class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def TraverseList(head):
    """Traverses a linked list and prints out each item until it reaches the end
    parameters: node
    preconditions: """
    while head != None:
        print(head.val, end=" ")
        head = head.next

def main():
    head = Node(val = 10)
    head.next = Node(val = 20)
    head.next.next = Node(val = 30)
    TraverseList(head)

if __name__ == '__main__':
    main()