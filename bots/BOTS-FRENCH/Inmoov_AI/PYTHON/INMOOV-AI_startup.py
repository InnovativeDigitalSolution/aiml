# ##############################################################################
# 							*** SETUP / INSTALLATION ***
# ##############################################################################
# -----------------------------------
# - Inmoov-AI Version 2.0.2 By Moz4r
# - Credit :
# - Rachel the humano�de
# - Wikidatafetcher By Beetlejuice
# - Azure translator by Papaoutai
# - Grog / Kwatters / Calamity and All MRL team
# - HairyGael
# - Heisenberg
# - Grattounet
# - Lecagnois
# - Dom
# -----------------------------------
#									multilingual base python script
#							( you just need translate all the aiml :)
# -----------------------------------
# !!! INSTALL : ( if you get this from github ) !!!
# !!! PLEASE copy all aiml files to : ProgramAB\bots\YOUR_BOT_NAME\aiml !!!
# !!! AND https://github.com/MyRobotLab/aiml/tree/master/bots/BOTS-FRENCH/INMOOV_AI/BDD + SOUND + PICTURES to the root of MRL
#
# 
# I use realTime voice syncronisation but you can check mouthcontrol=1 in INMOOV-AI_config.py 
# https://github.com/MyRobotLab/pyrobotlab/blob/master/home/moz4r/mouthcontrol_hardware.ino
# -
#  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#  !!!!!!!!!!!!!!!! CONFIG INSIDE THIS FILE !!! / ENTREZ VOS PARAMETRES DANS CE FICHIER  !!!!!!!!!!
#  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

# 						INMOOV-AI_config.py


# ###
# 
# ##############################################################################
#  						*** END SETUP ***
# ##############################################################################




version=20
#EN : We wait startup before robot can start to ear
global IcanStartToEar
#EN : After timer we don't want the robot listen everything we say
global IcanEarOnlyKnowsWords
IcanStartToEar=0
IcanEarOnlyKnowsWords=-1
#Robot state
global RobotIsStarted
global RobotIsSleepingSoft
RobotIsStarted=0
RobotIsSleepingSoft=0
global ParrotMod
ParrotMod=0
#Python libraries

import urllib2

from java.lang import String
import random
import threading
import io
import itertools
import random
import time
import textwrap
import codecs
import socket
import os
import shutil
import hashlib
import subprocess
import json
import time
import csv
from datetime import datetime
from subprocess import Popen, PIPE
from org.myrobotlab.service import Servo



#check runing folder
oridir=os.getcwd().replace("\\", "/")+"/"
#print oridir

# check if a config file exist or create default one
if os.path.isfile(oridir + '2-INMOOV-AI_config.py'):
	shutil.move(oridir + '2-INMOOV-AI_config.py', oridir + 'INMOOV-AI_config.py')

if os.path.isfile(oridir + 'INMOOV-AI_config.py'):
	print("ok")
else:
	shutil.copyfile(oridir + 'INMOOV-AI_config.py.default',oridir + 'INMOOV-AI_config.py')
# -- coding: utf-8 --
execfile(u'INMOOV-AI_config.py')
	
gesturesPath = (oridir)+"gestures"
BotURL=BotURL+"?lang="+lang+"&FixPhpCache="+str(time.time())

#fix programab aimlif problems : remove all aimlif files
#print oridir+'ProgramAB/bots/'+myAimlFolder+'/aimlif'
try:
	shutil.rmtree(oridir+'ProgramAB/bots/'+myAimlFolder+'/aimlif')
except: 
	pass

#some voice emotions
laugh = [" #LAUGH01# ", " #LAUGH02# ", " #LAUGH03# ", " ", " "]
troat = [" #THROAT01# ", " #THROAT02# ", " #THROAT03# ", " ", " ", " "]

#service pictures
image=Runtime.createAndStart("ImageDisplay", "ImageDisplay")

#service aiml
Runtime.createAndStart("chatBot", "ProgramAB")

#service wikidata
Runtime.createAndStart("wdf", "WikiDataFetcher")

#service inmoov
i01 = Runtime.create("i01", "InMoov")

#disable autocheck
i01.setMute(1)

#start acapela and webkit ear

#r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\loading.jpg',1)
#r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\loading.jpg',1)
#webgui.start()

# inmoov servo configuration

left = Runtime.create("i01.left", "Arduino")
leftHand = Runtime.create("i01.leftHand", "InMoovHand")
leftArm = Runtime.create("i01.leftArm", "InMoovArm")
right=Runtime.create("i01.right", "Arduino")
rightHand = Runtime.create("i01.rightHand", "InMoovHand")
rightArm = Runtime.create("i01.rightArm", "InMoovArm")
head = Runtime.create("i01.head","InMoovHead")
torso = Runtime.create("i01.torso", "InMoovTorso")

torso.topStom.setMinMax(TorsoTopMin,TorsoTopMax)
torso.topStom.map(0,180,TorsoTopMin,TorsoTopMax)
torso.topStom.setMinMax(0,180)

torso.midStom.setMinMax(TorsoMidMin,TorsoMidMax)
torso.midStom.map(0,180,TorsoMidMin,TorsoMidMax)
torso.midStom.setMinMax(0,180)
torso.topStom.setRest(90)
torso.midStom.setRest(90)

leftHand.thumb.setMinMax(ThumbLeftMIN,ThumbLeftMAX) 
leftHand.index.setMinMax(IndexLeftMIN,IndexLeftMAX) 
leftHand.majeure.setMinMax(majeureLeftMIN,majeureLeftMAX) 
leftHand.ringFinger.setMinMax(ringFingerLeftMIN,ringFingerLeftMAX) 
leftHand.pinky.setMinMax(pinkyLeftMIN,pinkyLeftMAX) 
leftHand.thumb.map(0,180,ThumbLeftMIN,ThumbLeftMAX) 
leftHand.index.map(0,180,IndexLeftMIN,IndexLeftMAX) 
leftHand.majeure.map(0,180,majeureLeftMIN,majeureLeftMAX) 
leftHand.ringFinger.map(0,180,ringFingerLeftMIN,ringFingerLeftMAX) 
leftHand.pinky.map(0,180,majeureLeftMIN,majeureLeftMAX) 

rightHand.thumb.setMinMax(ThumbRightMIN,ThumbRightMAX) 
rightHand.index.setMinMax(IndexRightMIN,IndexRightMAX) 
rightHand.majeure.setMinMax(majeureRightMIN,majeureRightMAX) 
rightHand.ringFinger.setMinMax(ringFingerRightMIN,ringFingerRightMAX) 
rightHand.pinky.setMinMax(pinkyRightMIN,pinkyRightMAX) 
rightHand.thumb.map(0,180,ThumbRightMIN,ThumbRightMAX) 
rightHand.index.map(0,180,IndexRightMIN,IndexRightMAX) 
rightHand.majeure.map(0,180,majeureRightMIN,majeureRightMAX) 
rightHand.ringFinger.map(0,180,ringFingerRightMIN,ringFingerRightMAX) 
rightHand.pinky.map(0,180,majeureRightMIN,majeureRightMAX)

head.jaw.setMinMax(JawMIN,JawMAX)
if JawInverted==1:
	head.jaw.map(0,180,JawMAX,JawMIN)
else:
	head.jaw.map(0,180,JawMIN,JawMAX)
head.jaw.setMinMax(0,180)
head.jaw.setRest(0)

head.eyeX.setMinMax(EyeXMIN,EyeXMAX)
head.eyeX.map(0,180,EyeXMIN,EyeXMAX)
head.eyeX.setMinMax(0,180)
head.eyeY.setMinMax(EyeYMIN,EyeYMAX)
head.eyeY.map(0,180,EyeYMIN,EyeYMAX)
head.eyeY.setMinMax(0,180)
head.eyeX.setRest(90)
head.eyeY.setRest(90)
head.neck.setMinMax(MinNeck,MaxNeck)
head.neck.setRest(90)
head.rothead.setMinMax(MinRotHead,MinRotHead)

if RotHeadInverted==1: 
	head.rothead.map(0,180,MaxRotHead,MinRotHead)
else:
	head.rothead.map(0,180,MinRotHead,MaxRotHead)

if NeckInverted==1: 
	head.neck.map(0,180,MaxNeck,MinNeck)
else:
	head.neck.map(0,180,MinNeck,MaxNeck)
	
#start the arduino
if IsInmoovArduino==1:
	
	#i01.startHead(leftPort)
	i01 = Runtime.start("i01","InMoov")
	#i01.startHead(leftPort)
	#i01.startAll(leftPort, rightPort)
	
	left = Runtime.start("i01.left", "Arduino")
	
	head.rothead.setSpeed(0.1)
	head.neck.setSpeed(0.1)
	head.rothead.setRest(90)
	head.neck.setMinMax(0,180)
	head.rothead.setMinMax(0,180)

	i01.startHead(leftPort)
	head.rothead.setSpeed(RotHeadSpeed)
	head.neck.setSpeed(NeckSpeed)	
	i01.startLeftHand(leftPort,"")
	i01.startLeftArm(leftPort)
	
	if MRLmouthControl==1:
		i01.startMouthControl(leftPort)
		i01.mouthControl.setmouth(0,180)
	if TorsoArduino=="left":	
		torso = i01.startTorso(leftPort)
	else:
		torso = i01.startTorso(rightPort)
	
	i01.head.eyeY.rest()
	i01.head.eyeX.rest()

	#i01.startHeadTracking(leftPort)
	
	right = Runtime.start("i01.right", "Arduino")
	i01.startRightHand(rightPort,"")
	i01.startRightArm(rightPort)
	
  #gestion des mouvement lat�raux de la tete ( mod pistons de Bob )
	HeadSide = Runtime.create("HeadSide","Servo")
	HeadSide.setMinMax(MinHeadSide , MaxHeadSide)
	HeadSide.map(0,180,MinHeadSide,MaxHeadSide)
	HeadSide.setMinMax(0,180)
	HeadSide.setRest(90)
	HeadSide.setSpeed(PistonSideSpeed)
	HeadSide = Runtime.start("HeadSide","Servo")
	if HeadSideArduino=="left":
		HeadSide.attach(left, HeadSidePin, 90, 5)
	else:
		HeadSide.attach(right, HeadSidePin, 90, 5)

	opencv = i01.opencv
	
i01.startMouth()
i01.startEar()
ear = i01.ear
mouth = i01.mouth

#start webgui
webgui = Runtime.create("WebGui","WebGui")
webgui.autoStartBrowser(False)
webgui.startService()

#r=image.displayFullScreen("https://i.ytimg.com/vi/tIk1Mc170yg/maxresdefault.jpg",1)
sleep(0.1)

Runtime.createAndStart("htmlFilter", "HtmlFilter")

voiceType=Voice

if lang=="FR":
   WikiFile="BDD/WIKI_prop.txt"
   wdf.setLanguage("fr")
   wdf.setWebSite("frwiki")
else:
   WikiFile="BDD/WIKI_propEN.txt"
   wdf.setLanguage("en")
   wdf.setWebSite("enwiki")

sleep(0.1)
mouth.setVoice(voiceType)
mouth.setLanguage(lang)

chatBot.startSession("ProgramAB", "default", myAimlFolder)
chatBot.addTextListener(htmlFilter)
htmlFilter.addListener("publishText", python.name, "talk") 

#var to set when robot is speaking
global Ispeak
Ispeak=1
global MoveHeadRandom
MoveHeadRandom=1

chatBot.startSession("ProgramAB", "default", myAimlFolder)
#ear.addTextListener(chatBot)
chatBot.addTextListener(htmlFilter)
htmlFilter.addListener("publishText", python.name, "talk") 

if Neopixel!="COMX":
	serial = Runtime.createAndStart("serial","Serial")
	serial.connect(Neopixel, 9600, 8, 1, 0)

  
#We include all InmoovAI mods
# -- coding: utf-8 --
execfile('INMOOV-AI_divers.py')
execfile('INMOOV-AI_memory.py')
if IhaveEyelids==1 or IhaveEyelids==2:
	execfile('INMOOV-AI_paupieres_eyeleads.py')
execfile(u'INMOOV-AI_timers.py')
if IsInmoovArduino==1:
	execfile('INMOOV-AI_opencv.py')
execfile('INMOOV-AI_move_head_random.py')
execfile('INMOOV-AI_azure_translator.py')
execfile('INMOOV-AI_messenger.py')
execfile('INMOOV-AI_KnowledgeFetchers.py')
execfile('INMOOV-AI_games.py')
execfile('INMOOV-AI_reminders.py')
execfile('INMOOV-AI_gestures.py')
execfile('INMOOV-AI_domotique.py')
execfile(u'INMOOV-AI_dictionaries.py')
execfile(u'INMOOV-AI_WeatherMap_Meteo.py')

NeoPixelF(3)

python.subscribe(mouth.getName(),"publishStartSpeaking")
python.subscribe(mouth.getName(),"publishEndSpeaking")

#Timer function to autostart webkit microphone every 10seconds
WebkitSpeachReconitionFix = Runtime.start("WebkitSpeachReconitionFix","Clock")
WebkitSpeachReconitionFix.setInterval(15000)
WebkitSpeachReconitionFix.addListener("pulse", python.name, "WebkitSpeachReconitionON")

# ##########################################################	
# program start :

Light(1,1,0)

#on remet � zero certaines variables de l'aiml ( sujets de discussion... )
ClearMemory()
if myBotname!="":
	UpdateBotName(myBotname)

rest()

if IsInmoovArduino==1:
	i01.head.attach()
	
if IsInmoovArduino==1 and tracking==1:
	trackHumans()

proc1 = subprocess.Popen("%programfiles(x86)%\Google\Chrome\Application\chrome.exe", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

Light(1,1,1)

#r=image.displayFullScreen("http://vignette2.wikia.nocookie.net/worldsofsdn/images/7/7a/Tyrell-corp.jpg",1)

if str(chatBot.getPredicate("default","botname"))!="unknown" and str(chatBot.getPredicate("default","botname"))!="default" and str(chatBot.getPredicate("default","botname"))!="":
	UpdateBotName(str(chatBot.getPredicate("default","botname")))

#if str(chatBot.getPredicate("default","bot_id"))!="unknown":
	#chatBot.getResponse("MESSAGESCHECK")

#r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\logo.jpg',1)
#r=image.displayFullScreen(os.getcwd().replace("develop", "")+'pictures\logo.jpg',1)
Light(1,1,1)
NeoPixelF(1)
CheckVersion()
GetUnreadMessageNumbers("0")
anniversaire("0")
chatBot.getResponse("WAKE_UP")
sleep(4)
webgui.startBrowser("http://localhost:8888/#/service/i01.ear")
#petit fix pour dire au robot qu'il eut commencer � �couter

if lang=="FR":
   ear.setLanguage("fr-FR")
python.subscribe(ear.getName(),"publishText")

WebkitSpeachReconitionFix.startClock()
#test de dictionaire
#print(Singularize("travaux"),Singularize("nez"),Singularize("vitraux"),Singularize("bocaux"),Singularize("poux"),Singularize("�poux"),Singularize("fraises"))
