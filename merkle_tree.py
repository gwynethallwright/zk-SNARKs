import hashlib

TREE_DEFAULT_INIT_STRING = 'HELLO WORLD'


def hash_string(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()


class MerkleTreeNode:
    def __init__(self, value=hash_string(TREE_DEFAULT_INIT_STRING)):
        self.value = value
        self.left = None
        self.right = None


def construct_tree(data, root, index):
    if not root:
        return
    if index >= len(data):
        return
    root.value = hash_string(data[index])
    left_index = 2*index+1
    if left_index >= len(data):
        return
    root.left = MerkleTreeNode(data[left_index])
    construct_tree(data, root.left, left_index)
    right_index = 2*index+2
    if right_index >= len(data):
        return
    root.right = MerkleTreeNode(right_index)
    construct_tree(data, root.right, right_index)


def dfs_tree_inorder(root):
    if not root:
        return
    dfs_tree_inorder(root.left)
    print(root.value)
    dfs_tree_inorder(root.right)


def main():
    root = MerkleTreeNode()
    construct_tree([str(i) for i in range(10)], root, 0)
    dfs_tree_inorder(root)


if __name__ == '__main__':
    main()
