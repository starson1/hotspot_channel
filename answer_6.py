# environment : linux 18.04 LTS
# 2019330012 AnSangHyuk
# Class 81 Term Project no6 answer

from wifi import Cell
import numpy as np 
import os
import sys 

def channel_data(interface):
    channel_list=[]
    tmp=[]
    for c in Cell.all(interface):
        ch = c.channel
        s = 100 + c.signal
        tmp.append(ch)
    for a in tmp:
        if a not in channel_list:
            channel_list.append(a)
    
    channel_list = sorted(channel_list)
    return channel_list

#get used channel data
interface = 'wlx002666400ba5'
channel = channel_data(interface)
print("unavailable channel : %s" % str(channel))

# search for available channel
for i in range(1,20):
    if i not in channel:
        print("Trying available channel %s\n\n"% i)
        hostapd_channel = i
        break
    else:
        continue

# try hostapd using hostapd_channel

#write conf file
conf = open("./hostapd.conf","w")
data = '''interface=wlx002666400ba5
ssid=class26_hw6_test_AP
ignore_broadcast_ssid=0
hw_mode=g
channel={channel}
wpa=2
wpa_passphrase=please_give_me_A+
wpa_key_mgmt=WPA-PSK
wpa_pairwise=TKIP
rsn_pairwise=CCMP
wpa_ptk_rekey=600
macaddr_acl=0
'''.format(channel = hostapd_channel)
conf.write(data)
conf.close()

print("\n\nhostapd.conf file written.")

print("\n\n----------Executing HOSTAPD----------")
os.system("sudo hostapd -d hostapd.conf")





