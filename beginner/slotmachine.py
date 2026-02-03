import random

# 1.print symbols....
# 2.print balance....
# 3.check balance....
# 4.check winner...
# 5.get amount....

symbols=["💧","🎈","🔮","🍒","🍀"]
balance=100

def print_symbols():
    global balance
    print("Spinning...")
    print("***********************")
    row=[random.choice(symbols) for _ in range(3)]
    print(f"{row[0]}    |   {row[1]}    |   {row[2]}")
    print("***********************")
    
    def check(line):
        if line[0]==line[1]==line[2]:
            print("---------Woohoooo you won the luck game---------")
            if line[0]=='💧':
                balance+=5
            elif line[0]=='🎈':
                balance+=10
            elif line[0]=='🔮':
                balance+=15
            elif line[0]=='🍒':
                balance+=30
            else:
                balance+=50
        else:
             print ("Keep spinning for luck.")
             
    check(row)
def check_balance(amount):
        global balance
        if  not isinstance(amount,(int,float)):
            print("Amount must be integer or floating point.")
            return False
        
        elif amount>balance:
            print("Insufficient funds.")
            print(f"Your balance is ${balance}")
            return False
        
        elif amount<=0:
            print("Enter a valid amount.")
            return False
        
        else:
            balance-=amount
            return True
            
        
def main():
    global balance
    print("_"*42)
    print("----Welcome to the game of sheer luck-----")
    print("_"*42)
        
    while True:
        money=int((input("Enter your betting amount : $"))).strip()
        
        result=check_balance(money)
        if result:
            print_symbols()
            print(f"Your balance is ${balance}")
            answer=input("Do you wish to contiue (y/n) : ").lower().strip()
            if answer=='n':
                print("Exiting.......")
                print("_"*42)
                break
        else:
            continue
if __name__=="__main__":
    main()
