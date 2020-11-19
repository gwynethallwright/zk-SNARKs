from partition_problem import *
from merkle_tree import *

DEFAULT_NUM_QUERIES = 10


def get_proof(problem, solution, num_queries=DEFAULT_NUM_QUERIES):
    proof = []
    witness = get_witness(problem, solution)
    parsed_solution = parse_tree_data(witness)
    merkle_tree = MerkleTree(parsed_solution)
    for _ in range(num_queries):
        random_query_index = random.randint(0, len(problem))
        # query_and_response = [merkle_tree_root, random_query_index, merkle_tree.values[i], get_authentication_path(node)]


def main():
    problem = [2, 3, 5]
    solution = [1, 1, -1]
    get_proof(problem, solution)