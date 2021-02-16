import math

def SDE(a,b,c):
    delta = b**2-4*a*c
    if delta < 0:
        print('This equation does not have answer')
    elif delta == 0:
        x = -b/2*a
        print('This equation has one answer its {}'.format(x))
    elif delta > 0:
        x1_numerator = -b+math.sqrt(delta)
        x1 = round(x1_numerator/2*a, 2)
        x2_numerator = -b-math.sqrt(delta)
        x2 = round(x2_numerator/2*a, 2)
        print('This equation has two answer x1 is {} and x2 is {}'.format(x1,x2))

SDE(1,-5,6)
