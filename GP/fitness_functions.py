def fitness_1_1_A(out, excpected_out):
    fit = 0
    if len(out) == 0:
        return -1000
    elif 1 in out:
        return 0
    for i in range(len(excpected_out)):
        fit += -abs(out[i] - excpected_out[i])
    return fit

def fitness_1_1_B(out, excpected_out):
    fit = 0
    if len(out) == 0:
        return -10000
    elif 789 in out:
        return 0
    for i in range(len(excpected_out)):
        fit += -abs(out[i] - excpected_out[i])
    return fit

def fitness_1_1_C(out, excpected_out):
    fit = 0
    if len(out) == 0:
        return -100000
    elif 31415 in out:
        return 0
    for i in range(len(excpected_out)):
        fit += -abs(out[i] - excpected_out[i])
    return fit

def fitness_1_1_D(out, excpected_out):
    fit = 0
    if len(out) == 0:
        return -1000
    elif 1 in out:
        return 0
    for i in range(len(excpected_out)):
        fit += -abs(out[i] - excpected_out[i])
    return fit

def fitness_1_1_E(out, excpected_out):
    fit = 0
    if len(out) == 0:
        return -1000
    elif 1 in out:
        return 0
    for i in range(len(excpected_out)):
        fit += -abs(out[i] - excpected_out[i])
    return fit

def fitness_1_1_F(out, excpected_out):
    fit = 0
    if len(out) == 0:
        return -1000
    elif 1 in out:
        return 0
    for i in range(len(excpected_out)):
        fit += -abs(out[i] - excpected_out[i])
    return fit

def fitness_1_2_A(out, excpected_out):
    fit = 0
    if len(out) == 0:
        return -1000
    elif 1 in out:
        return 0
    for i in range(len(excpected_out)):
        fit += -abs(out[i] - excpected_out[i])
    return fit

def fitness_1_2_B(out, excpected_out):
    fit = 0
    if len(out) == 0:
        return -1000
    elif 1 in out:
        return 0
    for i in range(len(excpected_out)):
        fit += -abs(out[i] - excpected_out[i])
    return fit

def fitness_1_2_C(out, excpected_out):
    fit = 0
    if len(out) == 0:
        return -1000
    elif 1 in out:
        return 0
    for i in range(len(excpected_out)):
        fit += -abs(out[i] - excpected_out[i])
    return fit

def fitness_1_2_D(out, excpected_out):
    fit = 0
    if len(out) == 0:
        return -1000
    elif 1 in out:
        return 0
    for i in range(len(excpected_out)):
        fit += -abs(out[i] - excpected_out[i])
    return fit

def fitness_1_2_E(out, excpected_out):
    fit = 0
    if len(out) == 0:
        return -1000
    elif 1 in out:
        return 0
    for i in range(len(excpected_out)):
        fit += -abs(out[i] - excpected_out[i])
    return fit

def fitness_1_3_A(out, excpected_out):
    fit = 0
    if len(out) == 0:
        return -1000
    elif 1 in out:
        return 0
    for i in range(len(excpected_out)):
        fit += -abs(out[i] - excpected_out[i])
    return fit

def fitness_1_3_B(out, excpected_out):
    fit = 0
    if len(out) == 0:
        return -1000
    elif 1 in out:
        return 0
    for i in range(len(excpected_out)):
        fit += -abs(out[i] - excpected_out[i])
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
    "1_3_B": fitness_1_3_B

}

def get_fit_func(name):
    return fittness_functions[name]