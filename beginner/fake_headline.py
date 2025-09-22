                    # This code generates fake news headline



import random,time

subject=["Imran Khan", " a fat cat", "ganji churail", "birju kay papa", " Bilal Abbas", "Aunty Shakeela", "Durdana","Babu Rao", "Munna Bhai", "Salar Sikander", "Raju Rocket", "Shinchan", "Doremon"]


action=[" was dancing","sang", " is jumping","ate", " spotted recording"," was crying", " was swimming ", " has been living", " was found playing", " is found running"," shouted", " was roasting", " was drinking"]

places=[" at a bar", " in mental assaylum", " in a toothi phutti imarat", " on the bus"," at nagan chowrangi", " at anda mor", " on the stage", " under a gutter", " on jail road", " in delulu", " in his/her dadi's shaadi", "in adiala jail"]

def gen_headline():
    sub=random.choice(subject)
    act=random.choice(action)
    venue=random.choice(places)

    headline= sub  +  act  +  venue
    return f"{sub} {act} { venue}"

if __name__ == "__main__":

    print("Welcome to our very own fake news headline generator")
    print()
    print("Let's get started")


    while True:

    
        print("Your headline is generating")
        time.sleep(1.5)
        print(gen_headline())

        print("Do you wish to continue : (yes/no)")
        ans=input().strip().lower()

        if ans == "no":
            break
    