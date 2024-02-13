def fitness_for_index(out, excpected_out, read_vars=0, current_variables = "{'X1':1}", number_of_inputs_after_reading_all_vars = 0, program = " " ):
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

import hashlib 
import random
def fitness_2_small_or_large(out, excpected_out,input_numbers = [1,2,3], read_vars=0, current_variables = "{'X1':1}", number_of_outputs_after_reading_all_vars = 0, program = " "):
    
    rand_str = str(random.random())

    program_string = program + rand_str
    # Generate a hash of the program string
    hash_object = hashlib.sha1(program_string.encode())
    hex_dig = hash_object.hexdigest()

    # Create a 10-character long filename from the hash
    filename = hex_dig[:10]


    with open(f'small_2/{filename}.txt', 'w') as file:
        if input_numbers[0] < 1000:
            file.write(f"program returned ! small ! \n input is {input_numbers} \n ")
        elif input_numbers[0] >= 2000:
            file.write(f"program returned ! large ! \n input is {input_numbers} \n ")
        else:
            file.write(f"program returned !      ! \n input is {input_numbers} \n")
    
    return 0

def fitness_6_collatz(out, excpected_out,input_numbers = [1,2,3], read_vars=0, current_variables = "{'X1':1}", number_of_outputs_after_reading_all_vars = 0, program = " " ):
    
    def collatz_sequence_length(n):
        count = 1
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
            count += 1
        
        return count

    result = collatz_sequence_length(input_numbers[0])

    rand_str = str(random.random())

    program_string = program + rand_str
    hash_object = hashlib.sha1(program_string.encode())
    hex_dig = hash_object.hexdigest()
    filename = hex_dig[:10]


    with open(f'collatz_6/{filename}.txt', 'w') as file:
        file.write(f"program returned ! {result} ! \n input is {input_numbers} \n ")
    
    return 0
    


def fitness_26_median(out, excpected_out,input_numbers = [1,2,3], read_vars=0, current_variables = "{'X1':1}", number_of_outputs_after_reading_all_vars = 0, program = " " ):
    # Zwrócić większą z inputu
    fit = 0
    if read_vars < 3:
        fit += -1000
    if read_vars >= 3:
        
        number_of_inputs_in_vars = 0
        for input_value in input_numbers:
            if input_value in current_variables.values():
                number_of_inputs_in_vars += 1
            else:
                pass

        
        
        if number_of_inputs_in_vars < len(input_numbers):
            fit += - 600
        else:
            if number_of_outputs_after_reading_all_vars == 1:

                if len(out) == 0:
                    fit += -150
                elif len(out) == 1:
                    if out[0] >= min(excpected_out) and out[0] <= max(excpected_out) and out[0] in input_numbers:
                        return 0
                    else:
                        fit -= 100  
                else:
                    fit += -200
            else:
                fit += -300

    return fit

def fitness_1_1_A(out, excpected_out, input_numbers, read_vars=0, current_variables = "{'X1':1}", number_of_inputs_after_reading_all_vars = 0, program = " " ,):
    fit = 0
    if read_vars > 2:
        if number_of_inputs_after_reading_all_vars >0:
            return -1
        if len(out) == 0:
            return -1234
        elif 1 in out:
            return -20
        else:
            for i in range(len(excpected_out)):
                fit += -50
    else:
        return -300
    return fit

def fitness_1_1_B(out, excpected_out,input_numbers = [1,2,3], read_vars=0, current_variables = "{'X1':1}", number_of_inputs_after_reading_all_vars = 0, program = " " ):
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

def fitness_1_1_C(out, excpected_out,input_numbers = [1,2,3], read_vars=0, current_variables = "{'X1':1}", number_of_inputs_after_reading_all_vars = 0, program = " " ):
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

def fitness_1_1_D(out, excpected_out,input_numbers = [1,2,3], read_vars=0, current_variables = "{'X1':1}", number_of_inputs_after_reading_all_vars = 0, program = " " ):
    fit = 0
    if 1.0-0.001 >= out[0] >= 1.0 + 0.001:
        return 0
    if len(out) == 0:
        return -1000
    if len(out)>0:
        distances_from_1 = abs(out[0] - 1)
        fit += -distances_from_1
    return fit

def fitness_1_1_E(out, excpected_out,input_numbers = [1,2,3], read_vars=0, current_variables = "{'X1':1}", number_of_inputs_after_reading_all_vars = 0, program = " " ):
    fit = 0
    if 789 - 0.01 >= out[0] >= 789.0 + 0.01:
        return 0
    if len(out) == 0:
        fit += -1000
    if len(out) > 0:
        distance_from_789 = abs(out[0] - 789)
        fit += -distance_from_789
    return fit

def fitness_1_1_F(out, excpected_out,input_numbers = [1,2,3], read_vars=0, current_variables = "{'X1':1}", number_of_inputs_after_reading_all_vars = 0, program = " " ):

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

def fitness_1_2_A(out, excpected_out,input_numbers = [1,2,3], read_vars=0, current_variables = "{'X1':1}", number_of_inputs_after_reading_all_vars = 0, program = " " ):
    fit = 0
    if read_vars < 2:
        fit += -400
    if read_vars >= 2:
        
        number_of_inputs_in_vars = 0
        for input_value in input_numbers:
            if input_value in current_variables.values():
                number_of_inputs_in_vars += 1
            else:
                pass
        
        if number_of_inputs_after_reading_all_vars == 1 and len(out) == 1:
            
            if number_of_inputs_in_vars < len(input_numbers):
                fit += -200
        
            if len(out) == 0:
                fit += -90
            elif len(out) == 1:
                if out[0] == excpected_out[0]:
                    return 0
                else:
                    fit += -100  
            else:
                fit += -300
        else:
            fit += -300
    else:
        fit += -400

    return fit

    

    # elif len(out) == 0:
    #     fit += -1000
    # elif len(out) > 1:
    #     fit += -10000
    # elif out[0] == excpected_out:
    #     return 0
    # else:
    #     fit += -10000

    return fit


def fitness_1_2_B(out, excpected_out,input_numbers = [1,2,3], read_vars=0, current_variables = "{'X1':1}", number_of_inputs_after_reading_all_vars = 0, program = " " ):
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

def fitness_1_2_C(out, excpected_out,input_numbers = [1,2,3], read_vars=0, current_variables = "{'X1':1}", number_of_inputs_after_reading_all_vars = 0, program = " " ):
    fit = 0
    if read_vars < 2:
        fit += -400
    if read_vars >= 2:
        
        number_of_inputs_in_vars = 0
        for input_value in input_numbers:
            if input_value in current_variables.values():
                number_of_inputs_in_vars += 1
            else:
                pass
        
        if number_of_inputs_after_reading_all_vars == 1 and len(out) == 1:
            
            if number_of_inputs_in_vars < len(input_numbers):
                fit += -200
        
            if len(out) == 0:
                fit += -90
            elif len(out) == 1:
                if out[0] == excpected_out[0]:
                    return 0
                else:
                    fit += -100  
            else:
                fit += -300
        else:
            fit += -300
    else:
        fit += -400

    return fit

def fitness_1_2_D(out, excpected_out,input_numbers = [1,2,3], read_vars=0, current_variables = "{'X1':1}", number_of_inputs_after_reading_all_vars = 0, program = " " ):
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

def fitness_1_2_E(out, excpected_out,input_numbers = [1,2,3], read_vars=0, current_variables = "{'X1':1}", number_of_inputs_after_reading_all_vars = 0, program = " " , ):
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

def fitness_1_3_A(out, excpected_out,input_numbers = [1,2,3],read_vars=0, current_variables = "{'X1':1}", number_of_inputs_after_reading_all_vars = 0, program = " "):
    # Zwrócić większą z inputu
    fit = 0
    if read_vars < 2:
        fit += -400
    if read_vars >= 2:
        
        number_of_inputs_in_vars = 0
        for input_value in input_numbers:
            if input_value in current_variables.values():
                number_of_inputs_in_vars += 1
            else:
                pass
        
        if number_of_inputs_in_vars < len(input_numbers):
            fit += - 200
        
        if len(out) == 0:
            fit += -150
        elif len(out) == 1:
            if out[0] == excpected_out[0]:
                return 0
            else:
                fit -= 100  
        else:
            fit += -300

    return fit

def fitness_1_3_B(out, excpected_out,input_numbers = [1,2,3], read_vars=0, current_variables = "{'X1':1}", number_of_inputs_after_reading_all_vars = 0, program = " " ):
    fit = 0
    if read_vars < 2:
        fit += -400
    if read_vars >= 2:
        
        number_of_inputs_in_vars = 0
        for input_value in input_numbers:
            if input_value in current_variables.values():
                number_of_inputs_in_vars += 1
            else:
                pass
        
        if number_of_inputs_in_vars < len(input_numbers):
            fit += - 200
        
        if len(out) == 0:
            fit += -150
        elif len(out) == 1:
            if out[0] == excpected_out[0]:
                return 0
            else:
                fit -= 100  
        else:
            fit += -300

    return fit


def fitness_1_4_A(out, excpected_out,input_numbers = [1,2,3], read_vars=0, current_variables = "{'X1':1}", number_of_inputs_after_reading_all_vars = 0, program = " " ):
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
    "for_index": fitness_for_index,
    "26_median": fitness_26_median,
    "2_small_or_large": fitness_2_small_or_large,
    "6_collatz": fitness_6_collatz

}

def get_fit_func(name):
    return fittness_functions[name]