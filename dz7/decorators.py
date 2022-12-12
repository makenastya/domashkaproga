def reverse_args(fn):
    def wrapper(*args):
        return fn(*(reversed(args)))
    return wrapper()


def print_args(fn):
    def wrapper(*args):
        ans = fn(*args)
        print(*args)
        return ans
    return wrapper


def catch_error(fn):
    def wrapper(*args):
        try:
            return fn(*args)
        except Exception:
            print("error")
    return wrapper
