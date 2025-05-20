class Logger:
    def __init__(self):
        print("logger created")
    def __del__(self):
        print("Logger destroyed")

log = Logger()
del log