#author : V-M4K4R0V

print("privyet!! Comrade")
user = input("enter your name : ")
R_SPY = open('/home/o11q/Desktop/git clone/chto-takoe-stolitsa/mozer racha/names.txt','r')
i = 19
print("You know what ill call you " + R_SPY.readline(i))
path = input("is it okay to call you " + R_SPY.readline(i) + " my FKHIEND [YES]or[NO] : ").upper

if(path == 'NO'):
     print("SYKAA!! GET OUT U FUCKING WESTERN SPY")
elif(path == 'YES'):
     print("SO! my FKHIEND what country  u want to invade today ?")
     enemy = input("choose your enemy :").lower
     if(enemy == 'morroco'):
          print("those are our FKHIEND's u shouldnt attack them")
     elif(enemy == 'russia'):
          print("SYYYKA! you are a fucking traitor KGB want to know ur location")
     elif(enemy == 'Afghanistan'):
          print("kha-kha-kha!ooh those freaking terrorists u'd better shoot them with the votkalachnikov")
     elif(enemy == 'Albania'):
          print("hello")
     elif(enemy == 'Australia'):
          print("hi")
     else:
          print("hello")       
else:
     print("you fucking donkey i said yes or no")
 
R_SPY.close()