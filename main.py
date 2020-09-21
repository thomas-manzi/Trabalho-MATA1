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
    aux = 0 
      # r = resultado do mod
    while(t):
        r = a % b
        a = b
        aux = b
        b = r 
        if (r == 0 ):
            t = False
    return(aux)


def mmc(a,b): 
    resultado = (a * b) /(mdcEuclides(a,b))
    return resultado

#lambda de n
def lambdN(p , q):
    resultado = mmc(p-1, q-1)
    return resultado


def validaChavePublica(e):
    if (e>1 and e<lambdN):
        if(mdcEuclides(e,lambdN) ==1):
            return True
        else:
            return False



#print(mmc(5,11))

#math.floor
def main():
    p = int(input("Digite P:"))
    while(primo(p) == False):
        print("Numero precisa ser primo")
        p = int(input("Digite P:"))
        

    q = int(input("Digite Q:"))
    while(primo(q) == False):
        print("Numero precisa ser primo")
        q = int(input("Digite Q:"))

    a=mdcEuclides(p,q)

    #mmc()

    e = int(input("Digite E:"))
    while(validaChavePublica(e) == False):
        print("Digite outro E")
        e = int(input("Digite E:"))

    


main()





