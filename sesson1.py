## sesson1.0

##check a varible's type?
##type(varible)
##
##cases that get SyntaxError
##case 1: not begin by a letter
##ex: 6hu = int(6)
##case 2: contain space
##ex: 6 hu = int(6)
##case 3: contain special characters (#,*,=,+,...)
##ex: *6hu = int(6)

##session1.1
x = 0
for i in range(1,5):
    x = x + 1
    y = x 
    z = x + y
    if i == 4:
        print('The pairs of rabit after 4 months is ', z)

