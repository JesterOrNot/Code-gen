from os import system
def code_gen_3000():
    f = open("generated.py", "w+")
    f.write("print('Hello World from generated code!')")
code_gen_3000()
system("python3 generated.py")
