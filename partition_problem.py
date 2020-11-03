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


def check_witness(witness):
    if witness[0] != witness[-1]:
        return False
    return True


def get_partial_sum(problem, signed_solution):
    offset = random.randint(RANDOM_OFFSET_LOWER, RANDOM_OFFSET_UPPER)
    partial_sum = [0]
    for num_1, num_2 in zip(problem, signed_solution):
        partial_sum.append(num_1*num_2+partial_sum[-1])
    for i, num in enumerate(partial_sum):
        partial_sum[i] = num+offset
    return partial_sum


def get_witness(problem, solution):
    signed_solution = solution.copy()
    sign = get_random_sign()
    for i, item in enumerate(signed_solution):
        signed_solution[i] = sign*item
    partial_sum = get_partial_sum(problem, signed_solution)
    return partial_sum


def main():
    problem = [2, 3, 5]
    solution = [1, 1, -1]
    assert(check_solution(problem, solution))
    witness = get_witness(problem, solution)
    assert(check_witness(witness))
    print(witness)


if __name__ == '__main__':
    main()
