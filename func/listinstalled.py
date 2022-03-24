#List installed games

import os, json
import configpath
from gameName import rspchar
from legendaryclean import legendaryclean
from createlaunchfile import createlaunchfile

def listinstalled():

    #Path to heroic's GamesConfig dir where each installed game's json is stored
    #gamesjsonpath = os.path.expanduser("~") + "/.config/heroic/GamesConfig"

  #EPIC GAMES LIBRARY
  #------------------------------------------------------------------------------------
  if os.path.exists(configpath.legendaryinstalledpath):
    #legendary cleanup
    legendaryclean()

    #Path to installed games via legendary's installed.json file
    #legendaryinstalledpath = os.path.expanduser("~") + "/.config/legendary/installed.json"

    #Convert legendary json to dict
    with open(configpath.legendaryinstalledpath, encoding='utf-8') as l:
      installed = json.load(l) 

    #Games' AppNames stored in list 
    installedkeyarray = list(installed.keys())

    # Moving one directory up
    #os.chdir(os.path.dirname(os.getcwd()))
    #print(os.getcwd())

    #Proceed to making launch files
    print("\n\nDone! Now creating launch files for your Epic Games library ...\n")
    for i in installedkeyarray:
      
      #Make sure the entries are games, not DLC
      if installed[i]["is_dlc"] == False:

        #Removing special characters from the game name (Steam issue)
        gamename = rspchar(installed[i]["title"])
        
        #Print current action
        print(gamename + " [" + i + "]...\n") # installed[i] = game's name, i = game's appname

        #Pointing to the game's json file
        gamejson = configpath.gamesjsonpath + "/" + i + ".json"

        #Preparing launch file
        createlaunchfile(gamename, i, gamejson, "epic") # gamename, appname, game's json file path

  #GOG LIBRARY
  #------------------------------------------------------------------------------------
  if os.path.exists(configpath.goginstalledpath):

    #Convert both json to dict
    with open(configpath.goginstalledpath, encoding='utf-8') as l:
      goginstalled = json.load(l)

    with open(configpath.goglibrarypath, encoding='utf-8') as p:
      goglibrary = json.load(p) 

    #Stored as list 
    goginstalledkeyarray = list(goginstalled['installed'])
    goglibrarykeyarray = list(goglibrary['games'])

    #Proceed to making launch files
    print("\n\nDone! Now creating launch files for your GOG library ...\n")
    for i in goginstalledkeyarray:

      for j in goglibrarykeyarray:

        if i['appName'] == j['app_name'] and i['is_dlc'] == False:

          #Removing special characters from the game name (Steam issue)
          gamename = rspchar(j['title'])

          #Print current action
          print(gamename + " [" + i['appName'] + "]...\n")

          #Pointing to the game's json file
          gamejson = configpath.gamesjsonpath + "/" + j['app_name'] + ".json"

          #Check if game is linux or windows
          if i['platform'] == "linux":
            gametype = "gog-linux"
          else:
            gametype = "gog-win"

          #Preparing launch file
          createlaunchfile(gamename, j['app_name'], gamejson, gametype) # gamename, appname, game's json file path

  #END OF THE PROGRAM
  print("\n...Process finished. Launch files stored in GameFiles folder and you can now sync games to Steam via AddToSteam\nHave fun gaming!")
