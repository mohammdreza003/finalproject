
class Node:
    def __init__(self, key, name, family):
        self.key = key
        self.data = [name, family]
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert_recursive(self, key, name, family):
        self.root = self._insert_recursive(self.root, None, key, name, family)

    def _insert_recursive(self, root, parent, key, name, family):
        if root is None:
            node = Node(key, name, family)
            node.parent = parent
            return node
        elif key < root.key:
            root.left = self._insert_recursive(root.left, root, key, name, family)
        elif key > root.key:
            root.right = self._insert_recursive(root.right, root, key, name, family)
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
            return None
        data = current.data
        children_count = self.get_children_count(current)
        if children_count == 0:
            self.delete_no_children(parent, current)
        elif children_count == 1:
            self.delete_one_child(parent, current)
        elif children_count == 2:
            self.delete_two_children(parent, current)
        del current
        return data

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, node, key):
        if not node:
            return None
        if key == node.key:
            return node.data
        elif key < node.key:
            return self._search_recursive(node.left, key)
        else:
            return self._search_recursive(node.right, key)


class HashTableWithBST:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def _hash_function(self, key):
        a = 0.618033
        return int(self.size * ((key * a) % 1))

    def insert(self, key, name, family):
        index = self._hash_function(key)
        if self.table[index] is None:
            self.table[index] = BST()
        self.table[index].insert_recursive(key, name, family)

    def search(self, key):
        index = self._hash_function(key)
        if self.table[index] is None:
            return None
        return self.table[index].search(key)

    def delete(self, key):
        index = self._hash_function(key)
        if self.table[index] is None:
            return None
        return self.table[index].delete(key)
