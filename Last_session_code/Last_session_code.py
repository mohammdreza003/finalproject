
class Array:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size
        self.count = 0

    def add(self, x):
        if self.count < self.size:
            self.array[self.count] = x
            self.count += 1
            return True
        return False

    def remove(self, x):
        for i in range(self.count):
            if self.array[i] == x:
                for j in range(i, self.count - 1):
                    self.array[j] = self.array[j + 1]
                self.array[self.count - 1] = None
                self.count -= 1
                return True
        return False

    def search(self, x):
        for i in range(self.size):
            if self.array[i] == x:
                return True
        return False


class LLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = LLNode(data)
        new_node.next = self.head
        self.head = new_node

    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            self.head = current_node.next
            del current_node
            return True
        prev = None
        while current_node and current_node.data != key:
            prev = current_node
            current_node = current_node.next
        if current_node is None:
            return False
        prev.next = current_node.next
        del current_node
        return True

    def find(self, key):
        current_node = self.head
        while current_node:
            if current_node.data == key:
                return True
            current_node = current_node.next
        return False


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert_recursive(self, key):
        self.root = self._insert_recursive(self.root, None, key)

    def _insert_recursive(self, root, parent, key):
        if root is None:
            node = BSTNode(key)
            node.parent = parent
            return node
        elif key < root.key:
            root.left = self._insert_recursive(root.left, root, key)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, root, key)
        return root

    def find_successor(self, node):
        parent = node
        successor = node.right
        while successor.left:
            parent = successor
            successor = successor.left
        return successor, parent

    def delete_no_children(self, parent, current):
        if not parent:
            self.root = None
        elif parent.left == current:
            parent.left = None
        else:
            parent.right = None

    def delete_one_child(self, parent, current):
        child = current.left if current.left else current.right
        if not parent:
            self.root = child
        elif parent.left == current:
            parent.left = child
        else:
            parent.right = child

    def delete_two_children(self, parent, current):
        successor, successor_parent = self.find_successor(current)
        if not parent:
            self.root = successor
        elif parent.left == current:
            parent.left = successor
        else:
            parent.right = successor
        successor.left = current.left
        if successor != current.right:
            successor.right = current.right
        if successor_parent != current:
            successor_parent.left = successor.right

    def get_children_count(self, node):
        if not node.left and not node.right:
            return 0
        elif not node.left or not node.right:
            return 1
        else:
            return 2

    def find_node_and_parent(self, key):
        parent = None
        current = self.root
        while current and current.key != key:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right
        return current, parent

    def delete(self, key):
        current, parent = self.find_node_and_parent(key)
        if not current:
            return False
        children_count = self.get_children_count(current)
        if children_count == 0:
            self.delete_no_children(parent, current)
        elif children_count == 1:
            self.delete_one_child(parent, current)
        elif children_count == 2:
            self.delete_two_children(parent, current)
        del current
        return True


class NewData:
    def __init__(self):
        self.main_data_set = Array(12)
        self.start = 2000

    def insert(self, data, key):
        roz = int(key[6:])
        mah = int(key[4:6])
        sal = int(key[0:4]) - self.start
        if self.main_data_set[sal] is None:
            self.main_data_set[sal] = LinkedList()

        temp = self.main_data_set[sal]
        if temp.search(mah) is None:
            temp = temp.search(mah)
        else:
            temp.insert(mah, BST())
            temp = temp.search(mah)

        temp.insert(roz, data)


