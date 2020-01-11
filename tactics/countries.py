#add more countries & songs
from mplayer import Player, CmdPrefix

def world_map(enemy):
     Player.cmd_prefix = CmdPrefix.PAUSING_KEEP
     player = Player()
     if(enemy == 'morocco'):
          print("Country : Morocco")
          print("Capital : Rabat")
          print("population : 39M")
          player.loadfile('natio_an_MA.mp3')
     elif(enemy == 'russia'):
          print("")
          #playsound('audio.mp3')
     elif(enemy == 'Afghanistan'):
          print("")
          #playsound('audio.mp3')
     elif(enemy == 'Australia'):
          print("")
     elif(enemy == 'Canada'):
          print("")
     elif(enemy == 'China'):
          print("")
     elif(enemy == 'Cuba'):
          print("")
     elif(enemy == 'Czech'):
          print("")
     elif(enemy == 'Egypt'):
          print("")
     elif(enemy == 'France'):
          print("")
     elif(enemy == 'Germany'):
          print("")
     elif(enemy == 'India'):
          print("")
     elif(enemy == 'Iran'):
          print("")
     elif(enemy == 'Iraq'):
          print("")
     elif(enemy == 'Israel'):
          print("")
     elif(enemy == 'Italy'):
          print("")
     else:
          print("cc")
