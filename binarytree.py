class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.val) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

    @classmethod
    def insert(cls, root, key):
        if root is None:
            return cls(key)
        else:
            if key < root.val:
                root.left = cls.insert(root.left, key)
            else:
                root.right = cls.insert(root.right, key)
        return root

    @classmethod
    def search(cls, root, key):
        if root is None or root.val == key:
            return root
        if key < root.val:
            return cls.search(root.left, key)
        return cls.search(root.right, key)
