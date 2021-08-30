def type_logger(func):
    def wrapper(args):
        w = {}
        w[args] = type(args)
        result = w
        print(f'{func.__name__}{w}')
        return result

    return wrapper

@type_logger
def calc_cube():
    exit()

print(calc_cube(4))