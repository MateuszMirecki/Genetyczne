def fitness_1_1_A(out, excpected_out):
    fit = 0
    if len(out) == 0:
        return -1000
    elif 1 in out:
        return 0
    for i in range(len(excpected_out)):
        fit += -abs(out[i] - excpected_out[i])
    return fit

fittness_functions = {
    "1_1_A": fitness_1_1_A
}
def get_fit_func(name):
    return fittness_functions[name]