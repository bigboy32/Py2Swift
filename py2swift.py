import os
import platform

if 'Windows' in platform.system():
    nt = True
else:
    nt = False

print('\nWelcome to py2swift! The python to swift transilator!')
print('Please not We do not support object oriented programming transilation yet. Sorry but we are still working on that!')
print('Please note that the tranislator is not yet that good and we relly on hard coded rules on hot to transilate')
print('To make a constant in python then use "@const " and then the variable name!')
print('Use the cleanconst.py script to remove the @const at the end so you can interpret the code without errors!')
print('Last note: please only use f-strings while writing insertions in print statements!')
print('\n\n')
filename = input('MOVE THE FILE IN TO THE DIRECTORY AND ENTER THE FILE NAME: ')
File = open(filename, 'r').readlines()
# VARIABLES STORED TO MAKE TRANSILATION MORE FLUENT
Mem = []

# PYTHON CONSTANT
const_py = '@const '
# HARD CODED SWIFT

print_statement_open = 'print('
string_sign = '"'
var = "var "
const = "let "

nf = open(filename.replace('.py', '.swift'), 'w')
print(nf)
def parse_file():
    for line in File:
        if 'print(' in line:
            nf.write(line.replace("'", string_sign) + ';')
        if '=' in line and not '@const ' in line:
            if line.split('=')[0] not in Mem:
                nf.write(var + line.replace("'", string_sign) + ';')
                Mem.append(line.split('=')[0])
            else:
                nf.write(line.replace("'", string_sign) + ';')
        if '=' in line and '@const ' in line:
            nf.write(const + line.replace('@const ', '').replace("'", string_sign) + ';')
parse_file()
