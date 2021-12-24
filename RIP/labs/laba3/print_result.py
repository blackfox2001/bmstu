def print_result(my_func):
    def wrapper(*args):
        print(my_func.__name__)
        result = my_func(*args)
        if isinstance(result, list):
            for value in result:
                print(str(value))
        elif isinstance(result, dict):
            for key in result.keys():
                print(str(key) + ' = ' + str(result[key]))
        else:
            print(result)
        return result

    return wrapper