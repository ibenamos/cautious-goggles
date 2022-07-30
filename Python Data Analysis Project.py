#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[6]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def name_Prepper(i):
    #x = len(i)
    for x in i:
        x = '"' + x + '"'
        print('= steam[steam["Game_Name"] == ', x)

steam=pd.read_csv(r'C:\Users\super\Desktop\Valve_Player_Data.csv')
twitch=pd.read_csv(r'C:\Users\super\Desktop\Twitch_global_data.csv')
names_abbrev=pd.read_csv(r'C:\Users\super\Desktop\Abbreviations and Full Names.csv')

call_trace = sorted(set(names_abbrev['call trace gain'].unique()))
games = sorted(set(steam['Game_Name'].unique()))
abbrev_name= names_abbrev['Abbreviation'].tolist()
game_name= names_abbrev['Full Game Name'].tolist()
m = games.index('Need foor Speed Heat')
games = games[:m]+['Need for Speed Heat']+games[m+1:]
#print(abbrev_name)

fig=go.Figure()

#fig.update_layout(showlegend=False, updatemenus=[{"buttons":buttons, "direction":"down", "active":games.index(default_game), "showactive":True,"x":0.5, "y":1.30}])
#fig.update_yaxes(title_text='Average Players')
#fig.show()

##Add date markers for summer/winter sales for possible context on high numbers on games
#print(games)
#name_Prepper(games)

SDD = steam[steam["Game_Name"] ==  "7 Days to Die"]
ARK = steam[steam["Game_Name"] ==  "ARK: Survival Evolved"]
AOE2= steam[steam["Game_Name"] ==  "Age of Empires II: Definitive Edition"]
APL= steam[steam["Game_Name"] ==  "Apex Legends"]
ARM3= steam[steam["Game_Name"] ==  "Arma 3"]
BF1= steam[steam["Game_Name"] ==  "Battlefield 1"]
BF5= steam[steam["Game_Name"] ==  "Battlefield V"]
BDO= steam[steam["Game_Name"] ==  "Black Desert"]
BUD= steam[steam["Game_Name"] ==  "Bless Unleashed "]
BTD6= steam[steam["Game_Name"] ==  "Bloons TD 6"]
BHA= steam[steam["Game_Name"] ==  "Brawlhalla"]
CSL= steam[steam["Game_Name"] ==  "Cities: Skylines"]
CBL= steam[steam["Game_Name"] ==  "Conqueror's Blade"]
CKC= steam[steam["Game_Name"] ==  "Cookie Clicker"]
CSGO= steam[steam["Game_Name"] ==  "Counter Strike: Global Offensive"]
CTS= steam[steam["Game_Name"] ==  "Counter-Strike"]
CK3= steam[steam["Game_Name"] ==  "Crusader Kings III"]
CBP= steam[steam["Game_Name"] ==  "Cyberpunk 2077"]
DS3= steam[steam["Game_Name"] ==  "DARK SOULS III"]
DYZ= steam[steam["Game_Name"] ==  "Dayz"]
DBD= steam[steam["Game_Name"] ==  "Dead by Daylight"]
DES2= steam[steam["Game_Name"] ==  "Destiny 2"]
DOS2= steam[steam["Game_Name"] ==  "Divinity: Original Sin 2"]
DST= steam[steam["Game_Name"] ==  "Don't Starve Together"]
DT2= steam[steam["Game_Name"] ==  "Dota 2"]
DYL= steam[steam["Game_Name"] ==  "Dying Light "]
DSP= steam[steam["Game_Name"] ==  "Dyson Sphere Program"]
FIF21= steam[steam["Game_Name"] ==  "EA SPORTS FIFA 21"]
ETR= steam[steam["Game_Name"] ==  "Eternal Return "]
ETS2= steam[steam["Game_Name"] ==  "Euro Truck Simulator 2"]
EU4= steam[steam["Game_Name"] ==  "Europa Universalis IV"]
FF14= steam[steam["Game_Name"] ==  "FINAL FANTASY XIV Online"]
FAC= steam[steam["Game_Name"] ==  "Factorio"]
FGUK= steam[steam["Game_Name"] ==  "Fall Guys: Ultimate Knockout"]
FO4= steam[steam["Game_Name"] ==  "Fallout 4"]
FS19= steam[steam["Game_Name"] ==  "Farming Simulator 19"]
FBM20= steam[steam["Game_Name"] ==  "Football Manager 2020"]
FBM21= steam[steam["Game_Name"] ==  "Football Manager 2021 "]
FH4= steam[steam["Game_Name"] ==  "Forza Horizion 4"]
GAM= steam[steam["Game_Name"] ==  "Garry's Mod"]
GED= steam[steam["Game_Name"] ==  "Geometry Dash"]
GTA5= steam[steam["Game_Name"] ==  "Grand Theft Auto V"]
HOI4= steam[steam["Game_Name"] ==  "Hearts of Iron IV"]
HSD= steam[steam["Game_Name"] ==  "Hunt: Showdown"]
L4D2= steam[steam["Game_Name"] ==  "Left 4 Dead 2"]
MIR4= steam[steam["Game_Name"] ==  "MIR4"]
MED= steam[steam["Game_Name"] ==  "Medieval Dynasty"]
MHW= steam[steam["Game_Name"] ==  "Monster Hunter: World"]
MB2B= steam[steam["Game_Name"] ==  "Mount & Blade II: Bannerlord "]
NBP= steam[steam["Game_Name"] ==  "NARAKA: BLADEPOINT"]
NB21= steam[steam["Game_Name"] ==  "NBA 2k21"]
NB22= steam[steam["Game_Name"] ==  "NBA 2k22"]
NFSH= steam[steam["Game_Name"] ==  "Need for Speed Heat"]
NMS= steam[steam["Game_Name"] ==  "No Man's Sky"]
ONI= steam[steam["Game_Name"] ==  "Oxygen Not Included"]
PD2= steam[steam["Game_Name"] ==  "PAYDAY 2"]
PUBG= steam[steam["Game_Name"] ==  "PUBG: Battlegrounds"]
POE= steam[steam["Game_Name"] ==  "Path of Exile"]
PWR= steam[steam["Game_Name"] ==  "Pathfinder: Wrath of Righteous"]
PHAS= steam[steam["Game_Name"] ==  "Phasmophobia"]
RDR2= steam[steam["Game_Name"] ==  "Red Dead Redemption 2"]
RMW= steam[steam["Game_Name"] ==  "RimWorld"]
RKTL= steam[steam["Game_Name"] ==  "Rocket League"]
RST= steam[steam["Game_Name"] ==  "Rust"]
SCM= steam[steam["Game_Name"] ==  "SCUM"]
STF= steam[steam["Game_Name"] ==  "Satisfactory"]
SOT= steam[steam["Game_Name"] ==  "Sea of Thieves"]
SDV= steam[steam["Game_Name"] ==  "Shadowverse"]
SMC5= steam[steam["Game_Name"] ==  "Sid Meier's Civilization V"]
SMC4= steam[steam["Game_Name"] ==  "Sid Meier's Civilization VI"]
STS= steam[steam["Game_Name"] ==  "Slay the Spire"]
SDP= steam[steam["Game_Name"] ==  "Soundpad"]
SPCW= steam[steam["Game_Name"] ==  "Spacewar"]
STRD= steam[steam["Game_Name"] ==  "Stardew Valley"]
STEL= steam[steam["Game_Name"] ==  "Stellaris"]
TOA= steam[steam["Game_Name"] ==  "Tales of Arise"]
TF2= steam[steam["Game_Name"] ==  "Team Fortress 2"]
TERR= steam[steam["Game_Name"] ==  "Terraria"]
TBOIR= steam[steam["Game_Name"] ==  "The Binding of Isaac: Rebirth"]
TESO= steam[steam["Game_Name"] ==  "The Elder Scrolls Online"]
TES5= steam[steam["Game_Name"] ==  "The Elder Scrolls V: Skyrim Special Edition"]
SIM4= steam[steam["Game_Name"] ==  "The Sims 4"]
TW3WH= steam[steam["Game_Name"] ==  "The Witcher 3: Wild Hunt"]
TCR6S= steam[steam["Game_Name"] ==  "Tom Clancy's Rainbow Six Seige"]
TW3K= steam[steam["Game_Name"] ==  "Total War: THREE KINGDOMS"]
TWW2= steam[steam["Game_Name"] ==  "Total War: WARHAMMER II"]
UTD= steam[steam["Game_Name"] ==  "Unturned"]
VRC= steam[steam["Game_Name"] ==  "VRChat"]
VALH= steam[steam["Game_Name"] ==  "Valheim"]
WAPE= steam[steam["Game_Name"] ==  "Wallpaper Engine"]
WART= steam[steam["Game_Name"] ==  "War Thunder"]
WAFR= steam[steam["Game_Name"] ==  "Warframe"]
WOTB= steam[steam["Game_Name"] ==  "World of Tanks Blitz"]
WOWS= steam[steam["Game_Name"] ==  "World of Warships"]
YGODL= steam[steam["Game_Name"] ==  "Yu-Gi-Oh! Duel Links"]
FBP= steam[steam["Game_Name"] ==  "eFootball PES 2021 SEASON UPDATE"]
TMOL= steam[steam["Game_Name"] ==  "tModLoader"]
MJS= steam[steam["Game_Name"] ==  "雀魂麻将(MahjongSoul)"]

fig = go.Figure()
fig.add_trace(go.Scatter(x=AOE2['Month_Year'],y=AOE2['Gain'], mode='lines+markers', name=  "Age of Empires II: Definitive Edition"))
fig.add_trace(go.Scatter(x=APL['Month_Year'],y=APL['Gain'], mode='lines+markers', name=  "Apex Legends"))
fig.add_trace(go.Scatter(x=ARM3['Month_Year'],y=ARM3['Gain'], mode='lines+markers', name=  "Arma 3"))
fig.add_trace(go.Scatter(x=ARK['Month_Year'],y=ARK['Gain'], mode='lines+markers', name=  "ARK: Survival Evolved"))
fig.add_trace(go.Scatter(x=BDO['Month_Year'],y=BDO['Gain'], mode='lines+markers', name=  "Black Desert"))
fig.add_trace(go.Scatter(x=BF1['Month_Year'],y=BF1['Gain'], mode='lines+markers', name=  "Battlefield 1"))
fig.add_trace(go.Scatter(x=BF5['Month_Year'],y=BF5['Gain'], mode='lines+markers', name=  "Battlefield V"))
fig.add_trace(go.Scatter(x=BHA['Month_Year'],y=BHA['Gain'], mode='lines+markers', name=  "Brawlhalla"))
fig.add_trace(go.Scatter(x=BTD6['Month_Year'],y=BTD6['Gain'], mode='lines+markers', name=  "Bloons TD 6"))
fig.add_trace(go.Scatter(x=BUD['Month_Year'],y=BUD['Gain'], mode='lines+markers', name=  "Bless Unleashed "))
fig.add_trace(go.Scatter(x=CBL['Month_Year'],y=CBL['Gain'], mode='lines+markers', name=  "Conqueror's Blade"))
fig.add_trace(go.Scatter(x=CBP['Month_Year'],y=CBP['Gain'], mode='lines+markers', name=  "Cyberpunk 2077"))
fig.add_trace(go.Scatter(x=CK3['Month_Year'],y=CK3['Gain'], mode='lines+markers', name=  "Crusader Kings III"))
fig.add_trace(go.Scatter(x=CKC['Month_Year'],y=CKC['Gain'], mode='lines+markers', name=  "Cookie Clicker"))
fig.add_trace(go.Scatter(x=CSGO['Month_Year'],y=CSGO['Gain'], mode='lines+markers', name=  "Counter Strike: Global Offensive"))
fig.add_trace(go.Scatter(x=CSL['Month_Year'],y=CSL['Gain'], mode='lines+markers', name=  "Cities: Skylines"))
fig.add_trace(go.Scatter(x=CTS['Month_Year'],y=CTS['Gain'], mode='lines+markers', name=  "Counter-Strike"))
fig.add_trace(go.Scatter(x=DBD['Month_Year'],y=DBD['Gain'], mode='lines+markers', name=  "Dead by Daylight"))
fig.add_trace(go.Scatter(x=DES2['Month_Year'],y=DES2['Gain'], mode='lines+markers', name=  "Destiny 2"))
fig.add_trace(go.Scatter(x=DOS2['Month_Year'],y=DOS2['Gain'], mode='lines+markers', name=  "Divinity: Original Sin 2"))
fig.add_trace(go.Scatter(x=DS3['Month_Year'],y=DS3['Gain'], mode='lines+markers', name=  "DARK SOULS III"))
fig.add_trace(go.Scatter(x=DSP['Month_Year'],y=DSP['Gain'], mode='lines+markers', name=  "Dyson Sphere Program"))
fig.add_trace(go.Scatter(x=DST['Month_Year'],y=DST['Gain'], mode='lines+markers', name=  "Don't Starve Together"))
fig.add_trace(go.Scatter(x=DT2['Month_Year'],y=DT2['Gain'], mode='lines+markers', name=  "Dota 2"))
fig.add_trace(go.Scatter(x=DYL['Month_Year'],y=DYL['Gain'], mode='lines+markers', name=  "Dying Light "))
fig.add_trace(go.Scatter(x=DYZ['Month_Year'],y=DYZ['Gain'], mode='lines+markers', name=  "Dayz"))
fig.add_trace(go.Scatter(x=ETR['Month_Year'],y=ETR['Gain'], mode='lines+markers', name=  "Eternal Return "))
fig.add_trace(go.Scatter(x=ETS2['Month_Year'],y=ETS2['Gain'], mode='lines+markers', name=  "Euro Truck Simulator 2"))
fig.add_trace(go.Scatter(x=EU4['Month_Year'],y=EU4['Gain'], mode='lines+markers', name=  "Europa Universalis IV"))
fig.add_trace(go.Scatter(x=FAC['Month_Year'],y=FAC['Gain'], mode='lines+markers', name=  "Factorio"))
fig.add_trace(go.Scatter(x=FBM20['Month_Year'],y=FBM20['Gain'], mode='lines+markers', name=  "Football Manager 2020"))
fig.add_trace(go.Scatter(x=FBM21['Month_Year'],y=FBM21['Gain'], mode='lines+markers', name=  "Football Manager 2021 "))
fig.add_trace(go.Scatter(x=FBP['Month_Year'],y=FBP['Gain'], mode='lines+markers', name=  "eFootball PES 2021 SEASON UPDATE"))
fig.add_trace(go.Scatter(x=FF14['Month_Year'],y=FF14['Gain'], mode='lines+markers', name=  "FINAL FANTASY XIV Online"))
fig.add_trace(go.Scatter(x=FGUK['Month_Year'],y=FGUK['Gain'], mode='lines+markers', name=  "Fall Guys: Ultimate Knockout"))
fig.add_trace(go.Scatter(x=FH4['Month_Year'],y=FH4['Gain'], mode='lines+markers', name=  "Forza Horizion 4"))
fig.add_trace(go.Scatter(x=FIF21['Month_Year'],y=FIF21['Gain'], mode='lines+markers', name=  "EA SPORTS FIFA 21"))
fig.add_trace(go.Scatter(x=FO4['Month_Year'],y=FO4['Gain'], mode='lines+markers', name=  "Fallout 4"))
fig.add_trace(go.Scatter(x=FS19['Month_Year'],y=FS19['Gain'], mode='lines+markers', name=  "Farming Simulator 19"))
fig.add_trace(go.Scatter(x=GAM['Month_Year'],y=GAM['Gain'], mode='lines+markers', name=  "Garry's Mod"))
fig.add_trace(go.Scatter(x=GED['Month_Year'],y=GED['Gain'], mode='lines+markers', name=  "Geometry Dash"))
fig.add_trace(go.Scatter(x=GTA5['Month_Year'],y=GTA5['Gain'], mode='lines+markers', name=  "Grand Theft Auto V"))
fig.add_trace(go.Scatter(x=HOI4['Month_Year'],y=HOI4['Gain'], mode='lines+markers', name=  "Hearts of Iron IV"))
fig.add_trace(go.Scatter(x=HSD['Month_Year'],y=HSD['Gain'], mode='lines+markers', name=  "Hunt: Showdown"))
fig.add_trace(go.Scatter(x=L4D2['Month_Year'],y=L4D2['Gain'], mode='lines+markers', name=  "Left 4 Dead 2"))
fig.add_trace(go.Scatter(x=MB2B['Month_Year'],y=MB2B['Gain'], mode='lines+markers', name=  "Mount & Blade II: Bannerlord "))
fig.add_trace(go.Scatter(x=MED['Month_Year'],y=MED['Gain'], mode='lines+markers', name=  "Medieval Dynasty"))
fig.add_trace(go.Scatter(x=MHW['Month_Year'],y=MHW['Gain'], mode='lines+markers', name=  "Monster Hunter: World"))
fig.add_trace(go.Scatter(x=MIR4['Month_Year'],y=MIR4['Gain'], mode='lines+markers', name=  "MIR4"))
fig.add_trace(go.Scatter(x=MJS['Month_Year'],y=MJS['Gain'], mode='lines+markers', name=  "雀魂麻将(MahjongSoul)"))
fig.add_trace(go.Scatter(x=NB21['Month_Year'],y=NB21['Gain'], mode='lines+markers', name=  "NBA 2k21"))
fig.add_trace(go.Scatter(x=NB22['Month_Year'],y=NB22['Gain'], mode='lines+markers', name=  "NBA 2k22"))
fig.add_trace(go.Scatter(x=NBP['Month_Year'],y=NBP['Gain'], mode='lines+markers', name=  "NARAKA: BLADEPOINT"))
fig.add_trace(go.Scatter(x=NFSH['Month_Year'],y=NFSH['Gain'], mode='lines+markers', name=  "Need for Speed Heat"))
fig.add_trace(go.Scatter(x=NMS['Month_Year'],y=NMS['Gain'], mode='lines+markers', name=  "No Man's Sky"))
fig.add_trace(go.Scatter(x=ONI['Month_Year'],y=ONI['Gain'], mode='lines+markers', name=  "Oxygen Not Included"))
fig.add_trace(go.Scatter(x=PD2['Month_Year'],y=PD2['Gain'], mode='lines+markers', name=  "PAYDAY 2"))
fig.add_trace(go.Scatter(x=PHAS['Month_Year'],y=PHAS['Gain'], mode='lines+markers', name=  "Phasmophobia"))
fig.add_trace(go.Scatter(x=POE['Month_Year'],y=POE['Gain'], mode='lines+markers', name=  "Path of Exile"))
fig.add_trace(go.Scatter(x=PUBG['Month_Year'],y=PUBG['Gain'], mode='lines+markers', name=  "PUBG: Battlegrounds"))
fig.add_trace(go.Scatter(x=PWR['Month_Year'],y=PWR['Gain'], mode='lines+markers', name=  "Pathfinder: Wrath of Righteous"))
fig.add_trace(go.Scatter(x=RDR2['Month_Year'],y=RDR2['Gain'], mode='lines+markers', name=  "Red Dead Redemption 2"))
fig.add_trace(go.Scatter(x=RKTL['Month_Year'],y=RKTL['Gain'], mode='lines+markers', name=  "Rocket League"))
fig.add_trace(go.Scatter(x=RMW['Month_Year'],y=RMW['Gain'], mode='lines+markers', name=  "RimWorld"))
fig.add_trace(go.Scatter(x=RST['Month_Year'],y=RST['Gain'], mode='lines+markers', name=  "Rust"))
fig.add_trace(go.Scatter(x=SCM['Month_Year'],y=SCM['Gain'], mode='lines+markers', name=  "SCUM"))
fig.add_trace(go.Scatter(x=SDD['Month_Year'],y=SDD['Gain'], mode='lines+markers', name=  "7 Days to Die"))
fig.add_trace(go.Scatter(x=SDP['Month_Year'],y=SDP['Gain'], mode='lines+markers', name=  "Soundpad"))
fig.add_trace(go.Scatter(x=SDV['Month_Year'],y=SDV['Gain'], mode='lines+markers', name=  "Shadowverse"))
fig.add_trace(go.Scatter(x=SIM4['Month_Year'],y=SIM4['Gain'], mode='lines+markers', name=  "The Sims 4"))
fig.add_trace(go.Scatter(x=SMC4['Month_Year'],y=SMC4['Gain'], mode='lines+markers', name=  "Sid Meier's Civilization VI"))
fig.add_trace(go.Scatter(x=SMC5['Month_Year'],y=SMC5['Gain'], mode='lines+markers', name=  "Sid Meier's Civilization V"))
fig.add_trace(go.Scatter(x=SOT['Month_Year'],y=SOT['Gain'], mode='lines+markers', name=  "Sea of Thieves"))
fig.add_trace(go.Scatter(x=SPCW['Month_Year'],y=SPCW['Gain'], mode='lines+markers', name=  "Spacewar"))
fig.add_trace(go.Scatter(x=STEL['Month_Year'],y=STEL['Gain'], mode='lines+markers', name=  "Stellaris"))
fig.add_trace(go.Scatter(x=STF['Month_Year'],y=STF['Gain'], mode='lines+markers', name=  "Satisfactory"))
fig.add_trace(go.Scatter(x=STRD['Month_Year'],y=STRD['Gain'], mode='lines+markers', name=  "Stardew Valley"))
fig.add_trace(go.Scatter(x=STS['Month_Year'],y=STS['Gain'], mode='lines+markers', name=  "Slay the Spire"))
fig.add_trace(go.Scatter(x=TBOIR['Month_Year'],y=TBOIR['Gain'], mode='lines+markers', name=  "The Binding of Isaac: Rebirth"))
fig.add_trace(go.Scatter(x=TCR6S['Month_Year'],y=TCR6S['Gain'], mode='lines+markers', name=  "Tom Clancy's Rainbow Six Seige"))
fig.add_trace(go.Scatter(x=TERR['Month_Year'],y=TERR['Gain'], mode='lines+markers', name=  "Terraria"))
fig.add_trace(go.Scatter(x=TES5['Month_Year'],y=TES5['Gain'], mode='lines+markers', name=  "The Elder Scrolls V: Skyrim Special Edition"))
fig.add_trace(go.Scatter(x=TESO['Month_Year'],y=TESO['Gain'], mode='lines+markers', name=  "The Elder Scrolls Online"))
fig.add_trace(go.Scatter(x=TF2['Month_Year'],y=TF2['Gain'], mode='lines+markers', name=  "Team Fortress 2"))
fig.add_trace(go.Scatter(x=TMOL['Month_Year'],y=TMOL['Gain'], mode='lines+markers', name=  "tModLoader"))
fig.add_trace(go.Scatter(x=TOA['Month_Year'],y=TOA['Gain'], mode='lines+markers', name=  "Tales of Arise"))
fig.add_trace(go.Scatter(x=TW3K['Month_Year'],y=TW3K['Gain'], mode='lines+markers', name=  "Total War: THREE KINGDOMS"))
fig.add_trace(go.Scatter(x=TW3WH['Month_Year'],y=TW3WH['Gain'], mode='lines+markers', name=  "The Witcher 3: Wild Hunt"))
fig.add_trace(go.Scatter(x=TWW2['Month_Year'],y=TWW2['Gain'], mode='lines+markers', name=  "Total War: WARHAMMER II"))
fig.add_trace(go.Scatter(x=UTD['Month_Year'],y=UTD['Gain'], mode='lines+markers', name=  "Unturned"))
fig.add_trace(go.Scatter(x=VALH['Month_Year'],y=VALH['Gain'], mode='lines+markers', name=  "Valheim"))
fig.add_trace(go.Scatter(x=VRC['Month_Year'],y=VRC['Gain'], mode='lines+markers', name=  "VRChat"))
fig.add_trace(go.Scatter(x=WAFR['Month_Year'],y=WAFR['Gain'], mode='lines+markers', name=  "Warframe"))
fig.add_trace(go.Scatter(x=WAPE['Month_Year'],y=WAPE['Gain'], mode='lines+markers', name=  "Wallpaper Engine"))
fig.add_trace(go.Scatter(x=WART['Month_Year'],y=WART['Gain'], mode='lines+markers', name=  "War Thunder"))
fig.add_trace(go.Scatter(x=WOTB['Month_Year'],y=WOTB['Gain'], mode='lines+markers', name=  "World of Tanks Blitz"))
fig.add_trace(go.Scatter(x=WOWS['Month_Year'],y=WOWS['Gain'], mode='lines+markers', name=  "World of Warships"))
fig.add_trace(go.Scatter(x=YGODL['Month_Year'],y=YGODL['Gain'], mode='lines+markers', name=  "Yu-Gi-Oh! Duel Links"))

fig.add_annotation(x='March 2020',y=0, text='Lockdown for COVID-19', showarrow=True, arrowhead=5, ax=10, ay=-90)
fig.show()


# In[11]:


import pandas
import matplotlib.pyplot as plt
import numpy
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def name_Prepper(i):
    #x = len(i)
    for x in i:
        x = '"' + x + '"'
        print('= steam[steam["Game_Name"] == ', x)

steam_data=pandas.read_csv(r'C:\Users\super\Desktop\Valve_Player_Data.csv')
twitch_game_data=pandas.read_csv(r'C:\Users\super\Desktop\Twitch_global_data.csv')

games = sorted(set(steam_data['Game_Name'].unique()))
m = games.index('Need foor Speed Heat')
games = games[:m]+['Need for Speed Heat']+games[m+1:]
print(games[m])


# In[ ]:





# In[4]:


fig=go.Figure()
fig.add_trace(go.Scatter(x=AOE2['Month_Year'],y=AOE2['Peak_Players'], mode='lines+markers', name=  "Age of Empires II: Definitive Edition"))
fig.add_trace(go.Scatter(x=APL['Month_Year'],y=APL['Peak_Players'], mode='lines+markers', name=  "Apex Legends"))
fig.add_trace(go.Scatter(x=ARM3['Month_Year'],y=ARM3['Peak_Players'], mode='lines+markers', name=  "Arma 3"))
fig.add_trace(go.Scatter(x=ARK['Month_Year'],y=ARK['Peak_Players'], mode='lines+markers', name=  "ARK: Survival Evolved"))
fig.add_trace(go.Scatter(x=BDO['Month_Year'],y=BDO['Peak_Players'], mode='lines+markers', name=  "Black Desert"))
fig.add_trace(go.Scatter(x=BF1['Month_Year'],y=BF1['Peak_Players'], mode='lines+markers', name=  "Battlefield 1"))
fig.add_trace(go.Scatter(x=BF5['Month_Year'],y=BF5['Peak_Players'], mode='lines+markers', name=  "Battlefield V"))
fig.add_trace(go.Scatter(x=BHA['Month_Year'],y=BHA['Peak_Players'], mode='lines+markers', name=  "Brawlhalla"))
fig.add_trace(go.Scatter(x=BTD6['Month_Year'],y=BTD6['Peak_Players'], mode='lines+markers', name=  "Bloons TD 6"))
fig.add_trace(go.Scatter(x=BUD['Month_Year'],y=BUD['Peak_Players'], mode='lines+markers', name=  "Bless Unleashed "))
fig.add_trace(go.Scatter(x=CBL['Month_Year'],y=CBL['Peak_Players'], mode='lines+markers', name=  "Conqueror's Blade"))
fig.add_trace(go.Scatter(x=CBP['Month_Year'],y=CBP['Peak_Players'], mode='lines+markers', name=  "Cyberpunk 2077"))
fig.add_trace(go.Scatter(x=CK3['Month_Year'],y=CK3['Peak_Players'], mode='lines+markers', name=  "Crusader Kings III"))
fig.add_trace(go.Scatter(x=CKC['Month_Year'],y=CKC['Peak_Players'], mode='lines+markers', name=  "Cookie Clicker"))
fig.add_trace(go.Scatter(x=CSGO['Month_Year'],y=CSGO['Peak_Players'], mode='lines+markers', name=  "Counter Strike: Global Offensive"))
fig.add_trace(go.Scatter(x=CSL['Month_Year'],y=CSL['Peak_Players'], mode='lines+markers', name=  "Cities: Skylines"))
fig.add_trace(go.Scatter(x=CTS['Month_Year'],y=CTS['Peak_Players'], mode='lines+markers', name=  "Counter-Strike"))
fig.add_trace(go.Scatter(x=DBD['Month_Year'],y=DBD['Peak_Players'], mode='lines+markers', name=  "Dead by Daylight"))
fig.add_trace(go.Scatter(x=DES2['Month_Year'],y=DES2['Peak_Players'], mode='lines+markers', name=  "Destiny 2"))
fig.add_trace(go.Scatter(x=DOS2['Month_Year'],y=DOS2['Peak_Players'], mode='lines+markers', name=  "Divinity: Original Sin 2"))
fig.add_trace(go.Scatter(x=DS3['Month_Year'],y=DS3['Peak_Players'], mode='lines+markers', name=  "DARK SOULS III"))
fig.add_trace(go.Scatter(x=DSP['Month_Year'],y=DSP['Peak_Players'], mode='lines+markers', name=  "Dyson Sphere Program"))
fig.add_trace(go.Scatter(x=DST['Month_Year'],y=DST['Peak_Players'], mode='lines+markers', name=  "Don't Starve Together"))
fig.add_trace(go.Scatter(x=DT2['Month_Year'],y=DT2['Peak_Players'], mode='lines+markers', name=  "Dota 2"))
fig.add_trace(go.Scatter(x=DYL['Month_Year'],y=DYL['Peak_Players'], mode='lines+markers', name=  "Dying Light "))
fig.add_trace(go.Scatter(x=DYZ['Month_Year'],y=DYZ['Peak_Players'], mode='lines+markers', name=  "Dayz"))
fig.add_trace(go.Scatter(x=ETR['Month_Year'],y=ETR['Peak_Players'], mode='lines+markers', name=  "Eternal Return "))
fig.add_trace(go.Scatter(x=ETS2['Month_Year'],y=ETS2['Peak_Players'], mode='lines+markers', name=  "Euro Truck Simulator 2"))
fig.add_trace(go.Scatter(x=EU4['Month_Year'],y=EU4['Peak_Players'], mode='lines+markers', name=  "Europa Universalis IV"))
fig.add_trace(go.Scatter(x=FAC['Month_Year'],y=FAC['Peak_Players'], mode='lines+markers', name=  "Factorio"))
fig.add_trace(go.Scatter(x=FBM20['Month_Year'],y=FBM20['Peak_Players'], mode='lines+markers', name=  "Football Manager 2020"))
fig.add_trace(go.Scatter(x=FBM21['Month_Year'],y=FBM21['Peak_Players'], mode='lines+markers', name=  "Football Manager 2021 "))
fig.add_trace(go.Scatter(x=FBP['Month_Year'],y=FBP['Peak_Players'], mode='lines+markers', name=  "eFootball PES 2021 SEASON UPDATE"))
fig.add_trace(go.Scatter(x=FF14['Month_Year'],y=FF14['Peak_Players'], mode='lines+markers', name=  "FINAL FANTASY XIV Online"))
fig.add_trace(go.Scatter(x=FGUK['Month_Year'],y=FGUK['Peak_Players'], mode='lines+markers', name=  "Fall Guys: Ultimate Knockout"))
fig.add_trace(go.Scatter(x=FH4['Month_Year'],y=FH4['Peak_Players'], mode='lines+markers', name=  "Forza Horizion 4"))
fig.add_trace(go.Scatter(x=FIF21['Month_Year'],y=FIF21['Peak_Players'], mode='lines+markers', name=  "EA SPORTS FIFA 21"))
fig.add_trace(go.Scatter(x=FO4['Month_Year'],y=FO4['Peak_Players'], mode='lines+markers', name=  "Fallout 4"))
fig.add_trace(go.Scatter(x=FS19['Month_Year'],y=FS19['Peak_Players'], mode='lines+markers', name=  "Farming Simulator 19"))
fig.add_trace(go.Scatter(x=GAM['Month_Year'],y=GAM['Peak_Players'], mode='lines+markers', name=  "Garry's Mod"))
fig.add_trace(go.Scatter(x=GED['Month_Year'],y=GED['Peak_Players'], mode='lines+markers', name=  "Geometry Dash"))
fig.add_trace(go.Scatter(x=GTA5['Month_Year'],y=GTA5['Peak_Players'], mode='lines+markers', name=  "Grand Theft Auto V"))
fig.add_trace(go.Scatter(x=HOI4['Month_Year'],y=HOI4['Peak_Players'], mode='lines+markers', name=  "Hearts of Iron IV"))
fig.add_trace(go.Scatter(x=HSD['Month_Year'],y=HSD['Peak_Players'], mode='lines+markers', name=  "Hunt: Showdown"))
fig.add_trace(go.Scatter(x=L4D2['Month_Year'],y=L4D2['Peak_Players'], mode='lines+markers', name=  "Left 4 Dead 2"))
fig.add_trace(go.Scatter(x=MB2B['Month_Year'],y=MB2B['Peak_Players'], mode='lines+markers', name=  "Mount & Blade II: Bannerlord "))
fig.add_trace(go.Scatter(x=MED['Month_Year'],y=MED['Peak_Players'], mode='lines+markers', name=  "Medieval Dynasty"))
fig.add_trace(go.Scatter(x=MHW['Month_Year'],y=MHW['Peak_Players'], mode='lines+markers', name=  "Monster Hunter: World"))
fig.add_trace(go.Scatter(x=MIR4['Month_Year'],y=MIR4['Peak_Players'], mode='lines+markers', name=  "MIR4"))
fig.add_trace(go.Scatter(x=MJS['Month_Year'],y=MJS['Peak_Players'], mode='lines+markers', name=  "雀魂麻将(MahjongSoul)"))
fig.add_trace(go.Scatter(x=NB21['Month_Year'],y=NB21['Peak_Players'], mode='lines+markers', name=  "NBA 2k21"))
fig.add_trace(go.Scatter(x=NB22['Month_Year'],y=NB22['Peak_Players'], mode='lines+markers', name=  "NBA 2k22"))
fig.add_trace(go.Scatter(x=NBP['Month_Year'],y=NBP['Peak_Players'], mode='lines+markers', name=  "NARAKA: BLADEPOINT"))
fig.add_trace(go.Scatter(x=NFSH['Month_Year'],y=NFSH['Peak_Players'], mode='lines+markers', name=  "Need for Speed Heat"))
fig.add_trace(go.Scatter(x=NMS['Month_Year'],y=NMS['Peak_Players'], mode='lines+markers', name=  "No Man's Sky"))
fig.add_trace(go.Scatter(x=ONI['Month_Year'],y=ONI['Peak_Players'], mode='lines+markers', name=  "Oxygen Not Included"))
fig.add_trace(go.Scatter(x=PD2['Month_Year'],y=PD2['Peak_Players'], mode='lines+markers', name=  "PAYDAY 2"))
fig.add_trace(go.Scatter(x=PHAS['Month_Year'],y=PHAS['Peak_Players'], mode='lines+markers', name=  "Phasmophobia"))
fig.add_trace(go.Scatter(x=POE['Month_Year'],y=POE['Peak_Players'], mode='lines+markers', name=  "Path of Exile"))
fig.add_trace(go.Scatter(x=PUBG['Month_Year'],y=PUBG['Peak_Players'], mode='lines+markers', name=  "PUBG: Battlegrounds"))
fig.add_trace(go.Scatter(x=PWR['Month_Year'],y=PWR['Peak_Players'], mode='lines+markers', name=  "Pathfinder: Wrath of Righteous"))
fig.add_trace(go.Scatter(x=RDR2['Month_Year'],y=RDR2['Peak_Players'], mode='lines+markers', name=  "Red Dead Redemption 2"))
fig.add_trace(go.Scatter(x=RKTL['Month_Year'],y=RKTL['Peak_Players'], mode='lines+markers', name=  "Rocket League"))
fig.add_trace(go.Scatter(x=RMW['Month_Year'],y=RMW['Peak_Players'], mode='lines+markers', name=  "RimWorld"))
fig.add_trace(go.Scatter(x=RST['Month_Year'],y=RST['Peak_Players'], mode='lines+markers', name=  "Rust"))
fig.add_trace(go.Scatter(x=SCM['Month_Year'],y=SCM['Peak_Players'], mode='lines+markers', name=  "SCUM"))
fig.add_trace(go.Scatter(x=SDD['Month_Year'],y=SDD['Peak_Players'], mode='lines+markers', name=  "7 Days to Die"))
fig.add_trace(go.Scatter(x=SDP['Month_Year'],y=SDP['Peak_Players'], mode='lines+markers', name=  "Soundpad"))
fig.add_trace(go.Scatter(x=SDV['Month_Year'],y=SDV['Peak_Players'], mode='lines+markers', name=  "Shadowverse"))
fig.add_trace(go.Scatter(x=SIM4['Month_Year'],y=SIM4['Peak_Players'], mode='lines+markers', name=  "The Sims 4"))
fig.add_trace(go.Scatter(x=SMC4['Month_Year'],y=SMC4['Peak_Players'], mode='lines+markers', name=  "Sid Meier's Civilization VI"))
fig.add_trace(go.Scatter(x=SMC5['Month_Year'],y=SMC5['Peak_Players'], mode='lines+markers', name=  "Sid Meier's Civilization V"))
fig.add_trace(go.Scatter(x=SOT['Month_Year'],y=SOT['Peak_Players'], mode='lines+markers', name=  "Sea of Thieves"))
fig.add_trace(go.Scatter(x=SPCW['Month_Year'],y=SPCW['Peak_Players'], mode='lines+markers', name=  "Spacewar"))
fig.add_trace(go.Scatter(x=STEL['Month_Year'],y=STEL['Peak_Players'], mode='lines+markers', name=  "Stellaris"))
fig.add_trace(go.Scatter(x=STF['Month_Year'],y=STF['Peak_Players'], mode='lines+markers', name=  "Satisfactory"))
fig.add_trace(go.Scatter(x=STRD['Month_Year'],y=STRD['Peak_Players'], mode='lines+markers', name=  "Stardew Valley"))
fig.add_trace(go.Scatter(x=STS['Month_Year'],y=STS['Peak_Players'], mode='lines+markers', name=  "Slay the Spire"))
fig.add_trace(go.Scatter(x=TBOIR['Month_Year'],y=TBOIR['Peak_Players'], mode='lines+markers', name=  "The Binding of Isaac: Rebirth"))
fig.add_trace(go.Scatter(x=TCR6S['Month_Year'],y=TCR6S['Peak_Players'], mode='lines+markers', name=  "Tom Clancy's Rainbow Six Seige"))
fig.add_trace(go.Scatter(x=TERR['Month_Year'],y=TERR['Peak_Players'], mode='lines+markers', name=  "Terraria"))
fig.add_trace(go.Scatter(x=TES5['Month_Year'],y=TES5['Peak_Players'], mode='lines+markers', name=  "The Elder Scrolls V: Skyrim Special Edition"))
fig.add_trace(go.Scatter(x=TESO['Month_Year'],y=TESO['Peak_Players'], mode='lines+markers', name=  "The Elder Scrolls Online"))
fig.add_trace(go.Scatter(x=TF2['Month_Year'],y=TF2['Peak_Players'], mode='lines+markers', name=  "Team Fortress 2"))
fig.add_trace(go.Scatter(x=TMOL['Month_Year'],y=TMOL['Peak_Players'], mode='lines+markers', name=  "tModLoader"))
fig.add_trace(go.Scatter(x=TOA['Month_Year'],y=TOA['Peak_Players'], mode='lines+markers', name=  "Tales of Arise"))
fig.add_trace(go.Scatter(x=TW3K['Month_Year'],y=TW3K['Peak_Players'], mode='lines+markers', name=  "Total War: THREE KINGDOMS"))
fig.add_trace(go.Scatter(x=TW3WH['Month_Year'],y=TW3WH['Peak_Players'], mode='lines+markers', name=  "The Witcher 3: Wild Hunt"))
fig.add_trace(go.Scatter(x=TWW2['Month_Year'],y=TWW2['Peak_Players'], mode='lines+markers', name=  "Total War: WARHAMMER II"))
fig.add_trace(go.Scatter(x=UTD['Month_Year'],y=UTD['Peak_Players'], mode='lines+markers', name=  "Unturned"))
fig.add_trace(go.Scatter(x=VALH['Month_Year'],y=VALH['Peak_Players'], mode='lines+markers', name=  "Valheim"))
fig.add_trace(go.Scatter(x=VRC['Month_Year'],y=VRC['Peak_Players'], mode='lines+markers', name=  "VRChat"))
fig.add_trace(go.Scatter(x=WAFR['Month_Year'],y=WAFR['Peak_Players'], mode='lines+markers', name=  "Warframe"))
fig.add_trace(go.Scatter(x=WAPE['Month_Year'],y=WAPE['Peak_Players'], mode='lines+markers', name=  "Wallpaper Engine"))
fig.add_trace(go.Scatter(x=WART['Month_Year'],y=WART['Peak_Players'], mode='lines+markers', name=  "War Thunder"))
fig.add_trace(go.Scatter(x=WOTB['Month_Year'],y=WOTB['Peak_Players'], mode='lines+markers', name=  "World of Tanks Blitz"))
fig.add_trace(go.Scatter(x=WOWS['Month_Year'],y=WOWS['Peak_Players'], mode='lines+markers', name=  "World of Warships"))
fig.add_trace(go.Scatter(x=YGODL['Month_Year'],y=YGODL['Peak_Players'], mode='lines+markers', name=  "Yu-Gi-Oh! Duel Links"))

fig.add_annotation(x='December 2012',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='July 2012',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='July 2013',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='December 2013',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='June 2014',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='December 2014',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='June 2015',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='December 2015',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='June 2016',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='December 2016',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='June 2017',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='December 2017',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='June 2018',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='December 2018',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='June 2019',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='December 2019',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='June 2020',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='December 2020',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='June 2021',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)






fig.show()


# In[108]:


fig=go.Figure()


fig.add_trace(go.Scatter(x=CSGO['Month_Year'],y=CSGO['Peak_Players'], mode='lines+markers', name=  "Counter Strike: Global Offensive"))
fig.add_trace(go.Scatter(x=DT2['Month_Year'],y=DT2['Peak_Players'], mode='lines+markers', name=  "Dota 2"))


fig.add_annotation(x='December 2012',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='July 2012',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='July 2013',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='December 2013',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='June 2014',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='December 2014',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='June 2015',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='December 2015',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='June 2016',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='December 2016',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='June 2017',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='December 2017',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='June 2018',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='December 2018',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='June 2019',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='December 2019',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='June 2020',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='December 2020',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.add_annotation(x='June 2021',y=0, text='', showarrow=True, arrowhead=0, ax=0, ay=-280)
fig.update_layout(title='Peak Numbers of Players per Month')

fig.show()


# In[112]:


fig=go.Figure()

for game_avg, group in steam.groupby("Game_Name"):
    fig.add_trace(go.Bar(x=group["Game_Name"], y=group["Avg_players"], name=game_avg))

#fig.show()

fig = px.bar(steam, x="Game_Name", y="Avg_players", color="Game_Name", barmode="group")
fig.update_traces(width=1)
fig.update_layout(title='Average Number of Players per Game')
fig.show()


# In[113]:


fig = make_subplots(rows=3,cols=2, subplot_titles=('Dota 2: Average Players','Warframe: Average Players','','','Dota 2: Peak Players', 'Warframe: Peak Players' ))

fig.add_trace(go.Bar(x=DT2['Month_Year'],y=DT2['Avg_players'], marker_color='indianred',showlegend=False),row=1,col=1)
fig.add_trace(go.Bar(x=DT2['Month_Year'],y=DT2['Peak_Players'], marker_color='indianred',showlegend=False),row=3,col=1)
fig.add_trace(go.Bar(x=WAFR['Month_Year'],y=WAFR['Avg_players'], marker_color='blue',showlegend=False),row=1,col=2)
fig.add_trace(go.Bar(x=WAFR['Month_Year'],y=WAFR['Avg_players'], marker_color='blue',showlegend=False),row=3,col=2)

#fig.add_annotation(x='February 2016',y=0, text='Patch 6.86e', bgcolor = 'goldenrod', showarrow=True, arrowcolor = 'goldenrod',arrowhead=0, ax=0, ay=120)

fig.show()

