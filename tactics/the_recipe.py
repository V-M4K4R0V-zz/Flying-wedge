from pathlib import Path
from countries import world_map

way1 = Path("pics")
way2 = Path("national anthems")

def ask_usr():
    #names file
    name = '/home/o11q/Desktop/git clone/Flying-wedge/tactics/names.txt'
    
    comrade_user = input('Enter your name : ')
    B_year = input('Enter your birth year : ')
    age = 2020 - int(B_year)
    #age fuction from age.py
    comrade_age(age)
    
    R_SPY = open(name,'r')
    #fix STRING INDEX i
    i = 19
    print("hello! "+comrade_user)
    print("You know what ill call you " + R_SPY.readline(i))
    print("SO! what country  u want to know about?")
    enemy = input("choose a country : ").lower()

    #countries from countries.py
    world_map(enemy)
    
    #close the names close
    R_SPY.close()
