
def max(*args):
    max_num = 0
    for arg in args:
        if arg > max_num:
            max_num = arg
    return max_num


print('Масимально число среди заданных равно: ', max(-10,-25,0))