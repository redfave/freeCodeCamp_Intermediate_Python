import functools

print('Function decorators')
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result

    return wrapper


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator_repeat

# a decorator function that prints debug information about the wrapped function
def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result
    return wrapper

# start_end_decorator(print_name)
# The decorators are called by their declaration order
@debug
@start_end_decorator
@repeat(3)
def print_name(name):
    # print('Alex')
    print(f'Hello, my name is {name} :)')


print_name('Alex')
print('\n')

print('Function identity')
print(help(print_name))
print(print_name.__name__)
print('\n')

print('Class decorators')

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    #Allows class instance to be called as function
    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f'This is executed {self.num_calls} times')
        return self.func(*args, **kwargs)

@CountCalls
def say_hello():
    print('Hello')

say_hello()
say_hello()
