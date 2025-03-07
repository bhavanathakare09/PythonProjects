def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mult(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1/n2


dictionary ={
    "+" :add,
    "-" : sub,
    "*" : mult,
    "/" : divide
}

def calculation():
    import art
    print(art.logo)
    choice = True
    first_number = float(input("What is first number?\n"))
    while choice:
        for key in dictionary:
            print(key)
        operation = input("Pick an operation: ")
        second_number = float(input("What is next number?: "))
        answer = dictionary[operation](first_number,second_number)
        print(f"{first_number} {operation} {second_number} = {answer}")
        next_choice = input("Type 'y' to continue calculating with 30.0, or type 'n' to start a new calculation or 'x' to exit: ").lower()
        if next_choice == "y":
            first_number = answer
        elif next_choice == "n":
            choice = False
            print("\n" * 20)
            calculation()
        else:
            print("Thank You for using calculator ")
            break
calculation()





