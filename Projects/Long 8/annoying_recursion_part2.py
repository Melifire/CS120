def annoying_valley(n):
    # works for all cases except n == 1 and n == 0 which are the only needed base cases
    if n > 6:
        string_to_print = "." * (n-1)
        print(string_to_print + '/')
        annoying_valley(n-1)  # recurion called enveloped by other code in the function
        print(string_to_print + '\\')
    if n == 0:  # base case: do nothing at 0
        pass
    if n == 1:  # base case: print the * at 1
        print('*')
    if n == 2:  # at n == 2 and n == 3 outputs are hardcoded in accordance with the rules
        print('./\n*\n.\\') 
    if n == 3:
        print('../\n./\n*\n.\\\n..\\')
    if n == 4:  # n == 4,5,6 are coppies of n > 6 with values hardcoded
        string_to_print = "." * (3)
        print(string_to_print + '/')
        annoying_valley(3)
        print(string_to_print + '\\')
    if n == 5:
        string_to_print = "." * (4)
        print(string_to_print + '/')
        annoying_valley(4)
        print(string_to_print + '\\')
    if n == 6:
        string_to_print = "." * (5)
        print(string_to_print + '/')
        annoying_valley(5)
        print(string_to_print + '\\')

def annoying_int_sequence(n):
    # recursive case works for all cases except and n == 0, 1 which are the only needed 
    # base cases
    if n > 6:  
        last_seq = annoying_int_sequence(n-1)
        out_seq = (last_seq + [n]) * (n-1) + last_seq 
        return out_seq
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:  # n == 2, 3 hardcoded in accordance with the rules
        return [1, 2, 1]
    if n == 3:
        return [1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1]
    if n == 4:  # n == 4,5,6 are coppies of n > 6 with values hardcoded
        last_seq = annoying_int_sequence(3)
        out_seq = (last_seq + [4]) * (3) + last_seq
        return out_seq
    if n == 5:
        last_seq = annoying_int_sequence(4)
        out_seq = (last_seq + [5]) * (4) + last_seq
        return out_seq
    if n == 6:
        last_seq = annoying_int_sequence(5)
        out_seq = (last_seq + [6]) * (5) + last_seq
        return out_seq