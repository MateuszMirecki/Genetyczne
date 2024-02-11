def fitness_for_index(out, excpected_out, read_vars=0, current_variables = "{'X1':1}" ):
    fit = 0
    if read_vars < 3:
        fit += -1000
    if len(out) < len(excpected_out):
        fit += -100
    elif len(out) > len(excpected_out):
        fit += -100000
    elif len(out) == len(excpected_out):
        for i in range(len(excpected_out)):
            if out[i] != excpected_out[i]:
                fit += -100000
        if fit == 0:
            return 0
    return fit
                

def fitness_1_1_A(out, excpected_out, input_numbers, read_vars=0, current_variables = "{'X1':1}" ,):
    fit = 0
    for number in out:
        if 1 - 0.01 <= number <= 1 + 0.01:
            return 0
    if len(out) == 0:
        return -1000
    else:
        for out_number in out:
            fit += -abs(out_number - 1)
    return fit

def fitness_1_1_B(out, excpected_out,input_numbers, read_vars=0, current_variables = "{'X1':1}" ):
    fit = 0
    for number in out:
        if 789 - 0.01 <= number <= 789 + 0.01:
            return 0
    if len(out) == 0:
        fit += -10000
    if len(out) > 0:
        distances_from_789 = [abs(x - 789) for x in out]
        fit += -min(distances_from_789)
    return fit

def fitness_1_1_C(out, excpected_out,input_numbers, read_vars=0, current_variables = "{'X1':1}" ):
    fit = 0
    for number in out:
        if 31415 - 0.01 <= number <= 31415 + 0.01:
            return 0
    if len(out) == 0:
        fit += -1000
    if len(out) > 0:
        distance_from_31415 = [abs(x - 31415) for x in out]
        fit += -min(distance_from_31415)
    return fit

def fitness_1_1_D(out, excpected_out,input_numbers, read_vars=0, current_variables = "{'X1':1}" ):
    fit = 0
    if 1.0-0.001 >= out[0] >= 1.0 + 0.001:
        return 0
    if len(out) == 0:
        return -1000
    if len(out)>0:
        distances_from_1 = abs(out[0] - 1)
        fit += -distances_from_1
    return fit

def fitness_1_1_E(out, excpected_out,input_numbers, read_vars=0, current_variables = "{'X1':1}" ):
    fit = 0
    if 789 - 0.01 >= out[0] >= 789.0 + 0.01:
        return 0
    if len(out) == 0:
        fit += -1000
    if len(out) > 0:
        distance_from_789 = abs(out[0] - 789)
        fit += -distance_from_789
    return fit

def fitness_1_1_F(out, excpected_out,input_numbers, read_vars=0, current_variables = "{'X1':1}" ):

    fit = 0

    for number in out:
        if 1 - 0.01 <= number <= 1 + 0.01:
            return 0
    if len(out) != 0:
        for _ in out:
            fit += -100

    distance_from_1 = [abs(out[x] - 1) for x in out]
    fit += -min(distance_from_1)
    return fit




def teach_to_read_only_2_vars_and_return_only_one(out, excpected_out, read_vars=0, current_variables = "{'X1':1}" ):
    fit = 0
    if read_vars  == 2 and len(out) == 1:
        return 0

    if read_vars == 0:
        fit += -2
    if read_vars == 2:
        fit += -1
    for i in range(3, 100):
        if read_vars == i:
            fit += -i
    if read_vars >= 100:
        fit += -1000

    if len(out) == 0:
        fit += -1
    for i in range(2, 100):
        if len(out) == i:
            fit += -i
    if len(out) >= 100:
        fit += -1000

    return fit

def fitness_1_2_A(out, excpected_out,input_numbers, read_vars=0, current_variables = "{'X1':1}" ):
    fit = 0

    if read_vars == 2 and len(out) == 1:
        distance_from_expected_value = abs(input_numbers[0] + input_numbers[1] - out[0])
        fit += -distance_from_expected_value

    if input_numbers[0] not in current_variables.values() or input_numbers[1] not in current_variables.values():
        fit += -100


    if read_vars == 0:
        fit += -2
    if read_vars == 2:
        fit += -1
    for i in range(3, 100):
        if read_vars == i:
            fit += -i
    if read_vars >= 100:
        fit += -1000

    if len(out) == 0:
        fit += -1
    for i in range(2, 100):
        if len(out) == i:
            fit += -i
    if len(out) >= 100:
        fit += -1000


    return fit



def fitness_1_2_B(out, excpected_out,input_numbers, read_vars=0, current_variables = "{'X1':1}" ):
    fit = 0

    if read_vars == 2 and len(out) == 1:
        distance_from_expected_value = abs(input_numbers[0] + input_numbers[1] - out[0])
        fit += -distance_from_expected_value

    if input_numbers[0] not in current_variables.values() or input_numbers[1] not in current_variables.values():
        fit += -100

    if read_vars == 0:
        fit += -2
    if read_vars == 2:
        fit += -1
    for i in range(3, 100):
        if read_vars == i:
            fit += -i
    if read_vars >= 100:
        fit += -1000

    if len(out) == 0:
        fit += -1
    for i in range(2, 100):
        if len(out) == i:
            fit += -i
    if len(out) >= 100:
        fit += -1000

    return fit

def fitness_1_2_C(out, excpected_out,input_numbers, read_vars=0, current_variables = "{'X1':1}" ):
    fit = 0

    if read_vars == 2 and len(out) == 1:
        distance_from_expected_value = abs(input_numbers[0] + input_numbers[1] - out[0])
        fit += -distance_from_expected_value

    if input_numbers[0] not in current_variables.values() or input_numbers[1] not in current_variables.values():
        fit += -100

    if read_vars == 0:
        fit += -2
    if read_vars == 2:
        fit += -1
    for i in range(3, 100):
        if read_vars == i:
            fit += -i
    if read_vars >= 100:
        fit += -1000

    if len(out) == 0:
        fit += -1
    for i in range(2, 100):
        if len(out) == i:
            fit += -i
    if len(out) >= 100:
        fit += -1000

    return fit

def fitness_1_2_D(out, excpected_out, input_numbers, read_vars=0, current_variables = "{'X1':1}" ):
    fit = 0
    if read_vars < 2:
        fit += -10000  
    if len(out) == 0:
        fit += -1000
    elif len(out) > 1:
        fit += -10000
    elif out[0] == excpected_out:
        return 0
    else:
        fit += -10000

    return fit

def fitness_1_2_E(out, excpected_out,input_numbers, read_vars=0, current_variables = "{'X1':1}" , ):
    fit = 0
    if read_vars < 2:
        fit += -10000  
    if len(out) == 0:
        fit += -1000
    elif len(out) > 1:
        fit += -10000
    if out[0] == excpected_out:
        return 0
    else:
        fit += -10000

    return fit

def fitness_1_3_A(out, excpected_out,input_numbers,read_vars=0, current_variables = "{'X1':1}" ):
    fit = 0

        # write
    if len(out) == 0:
        fit += -1
    for i in range(2,100):
        if len(out) == i:
            fit += -i
    if len(out) > 100:
        fit += -100

        #read
    if read_vars == 0:
        fit += -2
    if read_vars == 1:
        fit += -1
    for i in range(3,100):
        if read_vars == i:
            fit += -i
    if read_vars > 100:
        fit += -100

    # if max(input_numbers) != max(out):
    #     fit += -100


    return fit

def fitness_1_3_B(out, excpected_out,input_numbers, read_vars=0, current_variables = "{'X1':1}" ):
    fit = 0
    if read_vars < 2:
        fit += -10000  
    if len(out) == 0:
        fit += -1000
    elif len(out) > 1:
        fit += -10000
    elif out[0] == excpected_out:
        return 0
    else:
        fit += -10000

    return fit

def fitness_1_4_A(out, excpected_out,input_numbers, read_vars=0, current_variables = "{'X1':1}" ):
    fit = 0
    if read_vars < 10:
        fit += -1000  
    if len(out) == 0:
        fit += -10
    elif len(out) > 1:
        fit += -100000
    elif out[0] == excpected_out:
        return 0
    else:
        fit += -10000

    return fit



fittness_functions = {
    "1_1_A": fitness_1_1_A,
    "1_1_B": fitness_1_1_B,
    "1_1_C": fitness_1_1_C,
    "1_1_D": fitness_1_1_D,
    "1_1_E": fitness_1_1_E,
    "1_1_F": fitness_1_1_F,
    "1_2_A": fitness_1_2_A,
    "1_2_B": fitness_1_2_B,
    "1_2_C": fitness_1_2_C,
    "1_2_D": fitness_1_2_D,
    "1_2_E": fitness_1_2_E,
    "1_3_A": fitness_1_3_A,
    "1_3_B": fitness_1_3_B,
    "1_4_A": fitness_1_4_A,
    "for_index": fitness_for_index

}

def get_fit_func(name):
    return fittness_functions[name]