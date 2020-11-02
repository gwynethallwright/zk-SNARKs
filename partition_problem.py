import random

RANDOM_OFFSET_UPPER = 100
RANDOM_OFFSET_LOWER = -RANDOM_OFFSET_UPPER


def check_solution_pm_unity(solution):
    for item in solution:
        if item not in [-1, 1]:
            return False
    return True


def check_solution_valid(problem, solution):
    if len(problem) != len(solution):
        return False
    sum = 0
    for num_1, num_2 in zip(problem, solution):
        sum += num_1*num_2
    if sum != 0:
        return False
    return True


def get_random_sign():
    if random.randint(0, 1):
        return 1
    return -1


def check_solution(problem, solution):
    if (not solution) or (not problem):
        return False
    if not check_solution_pm_unity(solution):
        return False
    if not check_solution_valid(problem, solution):
        return False
    return True


def get_witness(problem, solution):
    witness = solution.copy()
    offset = random.randint(RANDOM_OFFSET_LOWER, RANDOM_OFFSET_UPPER)
    sign = get_random_sign()
    for i, item in enumerate(witness):
        witness[i] = sign*item+offset
    return witness


def main():
    problem = [2, 3, 5]
    solution = [1, 1, -1]
    assert(check_solution(problem, solution))
    witness = get_witness(problem, solution)
    print(witness)


if __name__ == '__main__':
    main()
