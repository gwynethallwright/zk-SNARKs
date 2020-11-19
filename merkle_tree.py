import hashlib
import random

TREE_DEFAULT_INIT_STRING = 'HELLO WORLD'
RANDOM_DATA_UPPER = 100
RANDOM_DATA_LOWER = -RANDOM_DATA_UPPER


def hash_string(input_string):
    return hashlib.sha256(input_string.encode()).hexdigest()


class MerkleTreeNode:
    def __init__(self, value=hash_string(TREE_DEFAULT_INIT_STRING)):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


class MerkleTree:
    def __init__(self, parsed_solution):
        self.values = parsed_solution
        self.root = MerkleTreeNode()
        construct_tree(parsed_solution, self.root, 0)


def add_random_data_to_solution(tree):
    random_data = [str(random.randint(RANDOM_DATA_LOWER, RANDOM_DATA_UPPER)) for _ in range(len(tree))]
    return [x for pair in zip(tree, random_data) for x in pair]


def parse_tree_data(witness):
    if not witness:
        return []
    witness = add_random_data_to_solution(witness)
    num_extra_nodes = len(witness)-1
    parsed_solution = ['' for _ in range(num_extra_nodes)]+[hash_string(item) for item in witness]
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
    root.left.parent = root
    construct_tree(data, root.left, left_index)
    right_index = 2*index+2
    if right_index >= len(data):
        return
    root.right = MerkleTreeNode(right_index)
    root.right.parent = root
    construct_tree(data, root.right, right_index)


def dfs_tree_inorder(root):
    if not root:
        return
    dfs_tree_inorder(root.left)
    print(root.value)
    dfs_tree_inorder(root.right)


def get_authentication_path(node):
    if not node or not node.parent:
        return []
    authentication_path = []
    current_parent = node.parent
    current_node = node
    while current_parent:
        if current_parent.left == current_node:
            authentication_path.append((current_parent.right.value, False))
        else:
            authentication_path.append((current_parent.left.value, True))
        current_node = current_node.parent
        current_parent = current_node.parent
    return authentication_path


def is_valid_merkle_path(root, first_provided_hash, authentication_path):
    current_hash_string = first_provided_hash
    for provided_hash, add_first in authentication_path:
        if add_first:
            current_hash_string = hash_string(provided_hash + current_hash_string)
        else:
            current_hash_string = hash_string(current_hash_string + provided_hash)
    return current_hash_string == root.value


def test_merkle_path_verifier(root, node):
    if node:
        assert(is_valid_merkle_path(root, node.value, get_authentication_path(node)))
        if node.left:
            test_merkle_path_verifier(root, node.left)
        if node.right:
            test_merkle_path_verifier(root, node.right)
    return True


def main():
    solution = [str(i) for i in range(3)]
    parsed_solution = parse_tree_data(solution)
    merkle_tree = MerkleTree(parsed_solution)
    dfs_tree_inorder(merkle_tree.root)
    test_merkle_path_verifier(merkle_tree.root, merkle_tree.root)


if __name__ == '__main__':
    main()
