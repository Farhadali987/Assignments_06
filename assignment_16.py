def log_function_call(func):
    def wrapper():
        print("function is being called")
        return func()
    return wrapper

@log_function_call
def say_hello():
    print("hello world")

say_hello()