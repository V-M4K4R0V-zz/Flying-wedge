#author : V-M4K4R0V

print("privyet!! Comrade")

usr = input("your name : ")

R_SPY = open('russian_spys.txt', 'r')

print("You know what ill call you " + R_SPY)

path = input("is it okay to call you" + R_SPY + "my друг [YES]or[NO] : ").upper

if(path == 'NO'):
    print("SYKAA!! GET OUT U FUCKING WESTERN SPY")
elif(path == 'YES'):
    print("SO! my друг what country  u want to invade today ?")
    enemy = input("choose your enemy :").lower
else:
    print("you fucking donkey i said yes or no not" + path)