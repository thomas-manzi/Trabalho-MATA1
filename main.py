import math

def primo(n):
    cont = 0 # contador
    if(n<2):
        return False 
    if (n % 2 ==0):
        if(n==2):
            return True
        else:
            return False
    else:
        cont=3
        while(cont<=math.sqrt(n)):
            if(n % cont == 0):
                return True
            else:
                cont = cont + 2 
    if(math.sqrt(n) < cont):
        return True


def mdcEuclides(a , b):
    t=True
    r=0  # resultado do mod
    while(t):
        r = a % b
        a = b
        r = b 
        if (r == 0 ):
            t = False
    return(b)

        





print(primo(29996224275833))




