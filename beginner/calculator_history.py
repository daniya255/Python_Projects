

history_file="history.txt"

def view_history():
     with open(history_file,"r") as f:
        lines=f.readlines()
        if lines:
            for line in lines:
                print(line.strip())
        else:
            print("Nothing to show ....")

def clear_history():
    with open (history_file,"w") as f:
        pass

    print("History is cleared")

def save_history(eq,result):
    with open (history_file,"a") as f:
        f.writelines(f"{eq} = {result} \n")


def cal(op1,op,op2):
    if op == "+" :
        result = op1 + op2
    elif op == "-" :
        result = op1 - op2
    elif op == "*" :
      result = op1 * op2
    elif op == "**" :
        result = op1 ** op2
    elif op ==  "%" :
        result = op1 % op2
    elif op ==  "/":
        if op2 == 0:
            print("A number cannot be divided by zero")
            result=None
        else:
            result= op1 /op2
    else:
        print("Incorrect operator inputted")
        result=None

    print(f"The result of your calculation is : {result}")
    return result


   
        

def main():
    while True:
        user=input("Enter the equation you want to evaluate or type a command from : exit,view and clear : ")

        if user=="exit":
            print("GOODBYE 🖐 Have a nice day")
            break

        elif user == "view":
            view_history()

        elif user == "clear":
            clear_history()

        else:
            parts=user.split()
            if len(parts) != 3:
                print("In correct format.... please use the following format")
                print("Example : 2 + 3")

            else:
                try:
                    op1=float(parts[0])
                    op=parts[1]
                    op2=float(parts[2])

                    result=cal(op1,op,op2)
                    if result is not None:
                        save_history(user,result)

                except ValueError:
                    print("Incorrect numbers entered")

main()       