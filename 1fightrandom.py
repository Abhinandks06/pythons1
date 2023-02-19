import random
class fight:
    def __init__(self,name,age,health,phealth):
        self.name=name
        self.age=age
        self.health=health
        self.phealth=phealth
    def punch(self,p):
        self.health=self.health-p
        return self.health
    def epunch(self,ep):
        self.phealth=self.phealth-ep
        return self.phealth
    def kick(self,k):
        self.health=self.health-k
        return self.health
    def ekick(self,ep):
        self.phealth=self.phealth-ep
        return self.phealth
    def block(self,b):
        self.phealth=self.phealth-b
        return self.phealth
    def eblock(self,ep):
        self.health=self.health-ep
        return self.health
    def show(self):
        return self.health
    def showp(self):
        return self.phealth
print("----FIGHTING GAME-----")
n=input("Enter your player name")
a=int(input("Enter your age"))
if(a<13):
    print("Players below the age 13 are not allowed to play")
    print("Exited.......")
    exit(0)
elif (a > 120):
    print("Given age not valid")
    print("Exited...")
    exit(0)
o=fight(n,a,150,150)
print("Player name :",n,"\nPlayer health status =150hp\nOpponent health status =150hp")
damage=[0,1,3,5,7,13,15,17,20,22,25,27,30]
damage1=[0,1,2,3,5,6,11,13,17,20]
while(True):
    print("Choose your attack \n 1.Punch \n 2.Kick \n 3.Block")
    choice=int(input("Enter your choice"))
    if(choice==1):
        p = random.choice(damage)
        o.punch(p)
        action = [o.epunch(random.choice(damage1)), o.ekick(random.choice(damage1)), o.eblock(random.choice(damage1))]
        atk=random.choice(action)
        if(p==0):
            print("Your punch has been dodged by the enemy")
        else:
            print("Damage dealt to enemy from ", n, " is :", p)
        if(action==0):
            print("Enemys counter attack missed target ")
        else:
            print("Damage given by enemy  :", action)
        if(o.health<1):
            print("Enemey has been defeated after the final blow")
            print(("-------------------------------"))
            print("And the Winner is ",n)
            print(("-------------------------------"))
        elif(o.health>1):
            print("Enemy health status :", o.show(), "HP left")
            print(n, "'s  health status :", o.showp(), "HP left")
        elif(o.phealth < 1):
            print(n," has been defeated by Enemy after the final blow")
            print("Better luck next time...")
            print(("-------------------------------"))
        else:
            print("Enemy health status :", o.show(), "HP left")
            print(n, "'s  health status :", o.showp(), "HP left")
    elif(choice==2):
        p = random.choice(damage)
        ep = random.choice(damage1)
        o.kick(p)
        action = [o.epunch(ep), o.ekick(ep), o.eblock(ep)]
        atk=random.choice(action)
        if (p == 0):
            print("Your kick has been dodged by the enemy")
        else:
            print("Damage dealt to enemy from ", n, " is", p)
        if (ep == 0):
            print("Enemy's counter attack  missed the target")
        else:
            print("Damage given by enemy  :", ep)
        if(o.health < 1):
            print("Enemey has been defeated after the final blow")
            print(("-------------------------------"))
            print("And the Winner is ", n)
            print(("-------------------------------"))
        elif(o.health>1):
            print("Enemy health status :", o.show(), "HP left")
            print(n, "'s  health status :", o.showp(), "HP left")
        elif(o.phealth<1):
            print(n, " has been defeated by Enemy after the final blow")
            print("Better luck next time...")
            print(("-------------------------------"))
        else:
            print("Enemy health status :", o.show(), "HP left")
            print(n, "'s  health status :", o.showp(), "HP left")
    elif (choice == 3):
        ep = random.choice(damage1)
        atk = random.choice(o.epunch(ep),o.ekick(ep))
        if(ep>0):
            print("Blocking enemys attack was unsuccessfull")
        else:
            print("Blocked enemys attack successfully")
        if(o.health>1):
            print("Damage dealt from enemy after blocking is ", ep)
            print("Enemy health status :", o.show(), "HP left")
            print(n,"'s health status :", o.showp(), "HP left")
        elif(o.phealth<1):
            print(n, " has been defeated by Enemy after the final blow")
            print("Better luck next time...")
            print("-------------------------------")
    else:
        print("Please choice a valid action")
    if(o.health<1 or o.phealth<1):
        x=int(input("Press 1 to Retry or 2 to Exit"))
        if(x==1):
            o.health=150
            o.phealth=150
            print(("----------------"))
            print("Player name :", n, "\nPlayer health status =150hp\nOpponent health status =150hp")
            continue
        else:
            print("Exited.....")
            exit(0)

