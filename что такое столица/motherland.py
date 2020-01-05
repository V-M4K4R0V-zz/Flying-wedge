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
    def switch_demo(enemy):
    switcher = {
        morocco: "those are our друг's",
        russia: "SYYYKA! you are a fucking traitor KGB ant to know ur location",
        Afghanistan: ""
        Albania: ""
        Algeria: ""
        Andorra: ""
        Angola: ""
        Antigua: ""
        Argentina: ""
        Armenia: ""
        Australia: ""
        Austria: ""
        Azerbaijan: ""
        The Bahamas: ""
        Bahrain: ""
        Bangladesh: ""
        Barbados: ""
        Belarus: ""
        Belgium: ""
        Belize: ""
        Benin: ""
        Bhutan: ""
        Bolivia: ""
        Bosnia: ""
        Botswana: ""
        Brazil: ""
        Brunei: ""
        Bulgaria: ""
        Burkina Faso: ""
        Burundi: ""
        Cabo Verde: ""
        Cambodia: ""
        Cameroon: ""
        Canada: ""
        Central African Republic: ""
        Chad: ""
        Chile: ""
        China: ""
        Colombia: ""
        Comoros: ""
        Congo, Democratic Republic of the: ""
        Congo, Republic of the: ""
        Costa Rica: ""
        Côte d’Ivoire: ""
        Croatia: ""
        Cuba: ""
        Cyprus: ""
        Czech Republic: ""
        Denmark: ""
        Djibouti: ""
        Dominica: ""
        Dominican Republic: ""
        Ecuador: ""
        Egypt: ""
        El Salvador: ""
        Equatorial Guinea: ""
        Eritrea: ""
        Estonia: ""
        Eswatini: ""
        Ethiopia: ""
        Fiji: ""
        Finland: ""
        France: ""
        Gabon: ""
        The Gambia: ""
        Georgia: ""
        Germany: ""
        Ghana: ""
        Greece: ""
        Grenada: ""
        Guatemala: ""
        Guinea: ""
        Guyana: ""
        Haiti: ""
        Honduras: ""
        Iceland: ""
        India: ""
        Indonesia: ""
        Iran: ""
        Iraq: ""
        Ireland: ""
        Israel: ""
        Italy: ""
    }
    print switcher.get(enemy, "Invalid month")
else:
    print("you fucking donkey i said yes or no not" + path)