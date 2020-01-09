#author : V-M4K4R0V
#add music , graphics , national anthem
#more dialogs
from enemies import world_map


print("privyet!! Comrade")

#im = Image.open('/home/o11q/Desktop/git clone/chto-takoe-stolitsa/mozer racha/put.jpg')
#print(im.format, im.size, im.mode)

comrade_user = input('enter your name : ') #NameError

R_SPY = open('/home/o11q/Desktop/git clone/Stalina-Blitzkrieg/mozer racha/names.txt','r')

i = 19 #fix STRING INDEX   

print("You know what ill call you " + R_SPY.readline(i))
path = input("is it okay to call you "  + R_SPY.readline(i) + "my FKHIEND [YES]or[NO] : ").upper() #fix \n

#ADD A LOOP
if(path == 'NO'):
        print("SYKAA!! GET OUT U FUCKING WESTERN SPY")
elif(path == 'YES'):
    print("SO! my APYR what country  u want to invade today ?")
    enemy = input("choose your enemy : ").lower()
    world_map(enemy) #enemies from enemies.py
else:
    print("you fucking donkey i said yes or not")
    #playsound('audio.mp3') #ownage pranks ill slap ur ass like 3abas
R_SPY.close() #close theTXT FILE
