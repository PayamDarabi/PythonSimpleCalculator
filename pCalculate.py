print "It`s a sipmle calculator based on python. written by Payam Darabi."

def Calculate():
    first=(input("Enter a Number: "))
    second=(input("Enter Second Number: ")) 
    print "What Do You Want To Do??? ( + / - * ) ",
    print "Choose One Of This Oprators"
    Operator = (input())
    if(str(Operator)== "*"):
        return first * second
    elif(str(Operator)== '+'):
        return first + second
    elif(str(Operator)== '-'):
        return first - second
    elif(str(Operator)== '/'):
        return first / second
    return 0
result = Calculate()
print result
raw_input("Press any key...")   


    
