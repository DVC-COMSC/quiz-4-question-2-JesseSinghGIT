
# ******************************
# Make your Code



numberflag = 0
minstringlen = 0
maxstringlen = 0



boolval = True
while boolval == True:
    str = input('Enter a string value: ')
    strlen = len(str)
    if (numberflag == 0):
        minstringlen = strlen + 1 
        maxstring = ''
    if (str == 'stop' or str == 'STOP'):
        boolval = False 
    if (len(str) > len(maxstring)):
        maxstring = str
        maxstringlen = len(str)
    if (len(str) < minstringlen):
        minstring = str
        minstringlen = len(str)
    numberflag = 1
print (maxstring, minstring)
# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
