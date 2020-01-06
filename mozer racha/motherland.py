#author : V-M4K4R0V
#add music , graphics , national anthem
#more dialogs
#fi
print("privyet!! Comrade")
user = input("enter your name : ")
R_SPY = open('/home/o11q/Desktop/git clone/chto-takoe-stolitsa/mozer racha/names.txt','r')
i = 19 #STRING INDEX #try to fix it
print("You know what ill call you " + R_SPY.readline(i))
path = input("is it okay to call you "+ R_SPY.readline(i) +"my FKHIEND [YES]or[NO] : ").upper() #BDL LBLASSA DLVARIBLE
#ADD A LOOP
if(path == 'NO'): #ADD MORE COUNTRIES
     print("SYKAA!! GET OUT U FUCKING WESTERN SPY")
elif(path == 'YES'):
    print("SO! my APYR what country  u want to invade today ?")
    enemy = input("choose your enemy : ").lower()
    if(enemy == 'morocco'):
        print("those are our APYR's u shouldnt attack them")
    elif(enemy == 'russia'):
        print("CYYYKA BLYAAAT! you are a fucking traitor KGB want to know your location")
    elif(enemy == 'Afghanistan'):
        print("kha-kha-kha!ooh those freaking terrorists u'd better shoot them with the votkalachnikov")
    elif(enemy == 'Australia'):
        print("hi")
    else:
        print("try again")
else:
    print("you fucking donkey i said yes or not" + path)
R_SPY.close() #TXT FILE