
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


'''
#Other 2 questions since canvas messed up the format of code

#Question 1

 #1.

previnput = 1
while True:
    userinput = int(input('Enter a number: '))
    if (int(userinput % 2) == 0 and int(previnput % 2) == 0):
        break 
    previnput = userinput

print ((previnput), (userinput))
'''



'''

#Question 3

boolp = False
countp = 0
while True:
    str = input('Enter a string: ')
    if (str == 'stop'):
        break
    else:
        for i in range(len(str)): 
            if (str[i] == 'p'):
                countp += 1    
print (countp)
print()
'''


# ******************************


# Requirement
# No need to use list
# All input values are taken one by one separatively.
###
