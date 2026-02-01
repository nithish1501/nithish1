def logger(*args, **kwargs):
    for arg in args:
        print("ARG:", arg)
    for key, value in kwargs.items():
        print(f"{key} = {value}")

logger(1, 2, 3, level="INFO", active=True)