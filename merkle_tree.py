import hashlib

TREE_DEFAULT_INIT_STRING = 'HELLO WORLD'


def hash_string(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()


class MerkleTreeNode:
    def __init__(self, value=hash_string(TREE_DEFAULT_INIT_STRING)):
        self.value = value
        self.left = None
        self.right = None


def add_filler_to_solution(tree):
    if (len(tree) % 2) == 1:
        tree = tree + ['']
    return tree


def parse_tree_data(solution):
    if not solution:
        return []
    solution = add_filler_to_solution(solution)
    num_extra_nodes = len(solution)-1
    parsed_solution = ['' for _ in range(num_extra_nodes)]+[hash_string(item) for item in solution]
    for i in reversed(range(num_extra_nodes)):
        parsed_solution[i] = hash_string(parsed_solution[2*i+1]+parsed_solution[2*i+2])
    return parsed_solution


def construct_tree(data, root, index):
    if (not root) or (not data):
        return
    if index >= len(data):
        return
    root.value = data[index]
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
    solution = [str(i) for i in range(3)]
    parsed_solution = parse_tree_data(solution)
    root = MerkleTreeNode()
    construct_tree(parsed_solution, root, 0)
    dfs_tree_inorder(root)


if __name__ == '__main__':
    main()
