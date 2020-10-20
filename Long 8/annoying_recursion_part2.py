# test 2

def annoying_valley(n):
    if n > 6:
        string_to_print = "." * (n-1)
        print(string_to_print + '/')
        annoying_valley(n-1)
        print(string_to_print + '\\')
    if n == 0:
        pass
    if n == 1:
        print('*')
    if n == 2:
        print('./\n*\n.\\')
    if n == 3:
        print('../\n./\n*\n.\\\n..\\')
    if n == 4:
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
    if n > 6:
        last_seq = annoying_int_sequence(n-1)
        out_seq = (last_seq + [n]) * (n-1) + last_seq
        return out_seq
    if n == 0:
        return []
    if n == 1:
        return [1]
    if n == 2:
        return [1, 2, 1]
    if n == 3:
        return [1, 2, 1, 3, 1, 2, 1, 3, 1, 2, 1]
    if n == 4:
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