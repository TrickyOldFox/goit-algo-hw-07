from binarytree import Node


# Assignment 1
def max_value_node(node) -> Node:
    current = node
    while current.right:
        current = current.right
    return current


# Assignment 2
def min_value_node(node) -> Node:
    current = node
    while current.left:
        current = current.left
    return current


# Assignment 3
def sum_value_node(node) -> int:
    if node is None:
        return 0

    if node.right is None:
        return node.val + sum_value_node(node.left)

    if node.left is None:
        return node.val + sum_value_node(node.right)

    return (
        node.val +
        sum_value_node(node.right) +
        sum_value_node(node.left)
    )


if __name__ == '__main__':
    # Test
    root = Node(5)
    root = Node.insert(root, 3)
    root = Node.insert(root, 2)
    root = Node.insert(root, 4)
    root = Node.insert(root, 7)
    root = Node.insert(root, 6)
    root = Node.insert(root, 8)

    assert min_value_node(root).val == 2
    assert max_value_node(root).val == 8
    assert sum_value_node(root) == 35

    root = Node.insert(root, 11)

    print(root)

    assert min_value_node(root).val == 2
    assert max_value_node(root).val == 11
    assert sum_value_node(root) == 46

    print(f"Min root: {min_value_node(root)}")
    print(f"Max root: {max_value_node(root)}")
    print(f"Sum: {sum_value_node(root)}")
