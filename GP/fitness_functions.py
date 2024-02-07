def fitness_for_index(out, excpected_out, read_vars=0):
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
                

def fitness_1_1_A(out, excpected_out, read_vars=0):
    fit = 0
    if len(out) == 0:
        return -1234
    elif 1 in out:
        return 0
    else:
        for i in range(len(excpected_out)):
            fit += -50
    return fit

def fitness_1_1_B(out, excpected_out, read_vars=0):
    fit = 0
    if 789 in out:
        return 0
    elif len(out) == 0:
        fit += -10000
    elif len(out) > 1:
        for i in range(len(out)):
            if out[i] != 789:
    
                fit += -10
    else:
        fit += -10000
    return fit

def fitness_1_1_C(out, excpected_out, read_vars=0):
    fit = 0
    if len(out) == 0:
        return -345678
    elif 31415 in out:
        return 0
    else:
        for i in range(len(excpected_out)):
            fit += -abs(out[i] - excpected_out[i])
    return fit

def fitness_1_1_D(out, excpected_out, read_vars=0):
    fit = 0
    if len(out) == 0:
        return -1000
    elif out[0] == 1:
        return 0
    else:
        for i in range(len(excpected_out)):
            fit += 10 * -abs(out[i] - excpected_out[i])
    return fit

def fitness_1_1_E(out, excpected_out, read_vars=0):
    fit = 0
    if len(out) == 0:
        return -100000
    elif out[0] == 789:
        return 0
    else:
        fit += 100 * -abs(out[0] - excpected_out[0])
    return fit

def fitness_1_1_F(out, excpected_out, read_vars=0):

    fit = 0

    if out == [1]:
        return fit 

    if len(out) == 0:
        fit += -1000
    if len(out) > 1:
        fit += -1000000
    else:
        fit += -2000    
    return fit

def fitness_1_2_A(out, excpected_out, read_vars=0):
    fit = 0
    if read_vars < 2:
        fit += -10000  
    elif len(out) == 0:
        fit += -1000
    elif len(out) > 1:
        fit += -10000
    elif out[0] == excpected_out:
        return 0
    else:
        fit += -10000

    return fit


def fitness_1_2_B(out, excpected_out, read_vars=0):
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

def fitness_1_2_C(out, excpected_out, read_vars=0):
    fit = 0
    if read_vars < 2:
        fit += -10000  
    elif len(out) == 0:
        fit += -1000
    elif len(out) > 1:
        fit += -10000
    elif out[0] == excpected_out:
        return 0
    else:
        fit += -10000

    return fit

def fitness_1_2_D(out, excpected_out, read_vars=0):
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

def fitness_1_2_E(out, excpected_out, read_vars=0):
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

def fitness_1_3_A(out, excpected_out, read_vars=0):
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

def fitness_1_3_B(out, excpected_out, read_vars=0):
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

def fitness_1_4_A(out, excpected_out, read_vars=0):
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