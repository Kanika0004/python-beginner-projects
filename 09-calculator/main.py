import art

def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}

def calculator():
    print(art.logo)
    cont=True
    first_num=float(input("What's the first Number?:"))
    while cont:
        print("+\n-\n*\n/\n")
        op=input("Pick an operation: ")
        sec_num=float(input("What's the next number?:"))
        for key in operations:
            if key==op:
                ans=operations[key](first_num,sec_num)
                print(f"{first_num} {key} {sec_num} = {ans}")
        cont_ans=input(f"Type 'y' to continue calculating with {ans}, or type 'n' to start a new calculation:")
        if cont_ans=="y":
            cont=True
            first_num=ans
        else :
            cont=False
            calculator()

calculator()