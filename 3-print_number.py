number = 333
try:
    print(f"{number} Battery street")
except ValueError:
    print("ValueError: Unknown format code 'd' for object of type 'str'")
