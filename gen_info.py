import itertools


def generate_bool_test_cases(k, function):
    test_cases = []
    for inputs in itertools.product([0, 1], repeat=k):
        if function == 'AND':
            result = int(all(inputs))
        elif function == 'OR':
            result = int(any(inputs))
        elif function == 'XOR':
            result = sum(inputs) % 2
        test_case = f"{' '.join(map(str, inputs))} : {result}"
        test_cases.append(test_case)
    return test_cases

for k in range(1, 3):
    for function in ['AND', 'OR', 'XOR']:
        test_cases = generate_bool_test_cases(k, function)
        print(f"Test cases for k = {k}, function = {function}:")
        for test_case in test_cases:
            print(test_case)
        print("\n")