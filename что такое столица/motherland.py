#author : V-M4K4R0V

print("privyet!! Comrade")
usr = input("your name : ")

f = open("russian_spys.txt", "r")

if f.mode == 'r':
     R_SPY =f.read()
print("You know what ill call you " + R_SPY)
path = input("is it okay to call you my FKHIEND [YES]or[NO] : ").upper
