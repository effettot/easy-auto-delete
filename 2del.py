import os

file = "1del.py"

if os.path.isfile(file):
    os.remove(file)
    print(f"{file} was successfully deleted")
else:
    print(f"{file} does not exist")

os.remove(__file__)
print(f"{__file__} was successfully deleted")
