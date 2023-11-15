#!/urs/bin/env python3 #shabang

def Calcolatrice1():

    op = input("Scegliere quale operazione fare: \n") #+ - * /
    num1 = input("Primo numero \n")
    num2 = input("Secondo numero \n")
    risultato1=0
    def somma (num1, num2):
        return num1+num2

    def sottrazione (num1, num2):
        return num1-num2

    def moltiplicazione (num1, num2):
        return num1*num2

    def divisione (num1, num2):
        return num1/num2

    if (op == "+"):
        risultato1 = somma(num1,num2)
    elif (op == "-"):
        risultato1 = sottrazione(num1, num2)
    elif (op == "*"):
        risultato1 = moltiplicazione(num1, num2)
    elif (op == "/"):
        risultato1 = divisione(num1, num2)

    print (risultato1)

# Execute
if __name__ == '__main__':
    Calcolatrice1()

