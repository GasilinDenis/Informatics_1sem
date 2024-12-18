class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.height = 1

class Tree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        if node:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_left(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        if T2:
            T2.parent = z
        y.parent = z.parent
        z.parent = y

        self.update_height(z)
        self.update_height(y)
        return y

    def rotate_right(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        if T3:
            T3.parent = z
        y.parent = z.parent
        z.parent = y

        self.update_height(z)
        self.update_height(y)
        return y

    def rebalance(self, node):
        self.update_height(node)
        balance = self.get_balance(node)
        #print(node.value, balance, self.get_height(node))

        if balance > 1:
            if self.get_balance(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        if balance < -1:
            if self.get_balance(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def add(self, value):
        def _add(node, value):
            if not node:
                return Node(value)

            if value < node.value:
                node.left = _add(node.left, value)
                node.left.parent = node
            else:
                node.right = _add(node.right, value)
                node.right.parent = node

            return self.rebalance(node)

        self.root = _add(self.root, value)

    def search(self, value):
        t = self.root
        while t is not None and t.value != value:
            t = t.left if value < t.value else t.right
        #print("t= ", t.value if t != None else None)
        return t is not None

    def remove(self, value):
        def _remove(node, value):
            if not node:
                return node

            if value < node.value:
                node.left = _remove(node.left, value)
            elif value > node.value:
                node.right = _remove(node.right, value)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left

                #2 children
                successor = node.right
                while successor.left:
                    successor = successor.left
                node.value = successor.value
                node.right = _remove(node.right, successor.value)

            return self.rebalance(node)

        self.root = _remove(self.root, value)


T = Tree()
T.add(4)
T.add(1)
T.add(2)
T.add(6)
T.add(-3)
print(T.search(2))
print(T.search(-3))
T.remove(-3)
print(T.search(-3))
T.remove(2)
print(T.search(2))
