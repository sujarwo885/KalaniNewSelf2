# -*- coding: utf-8 -*-

import WIB
from WIB.libapi.ttypes import *
from datetime import datetime
import io,os,re,ast,six,sys,glob,json,time,timeit,codecs,random,shutil,urllib,urllib2,urllib3,goslate,html5lib,requests,threading,wikipedia,subprocess,googletrans
from gtts import gTTS
from random import randint
from time import sleep
from urllib import urlopen, urlretrieve, urlencode
from io import StringIO
from bs4 import BeautifulSoup
from threading import Thread
from googletrans import Translator

if (six.PY2):
    import urllib2
    import urllib
else:
    import urllib.request
    import urllib.parse

cl = WIB.LINE()
cl.login(token="EpOQouf0FQJY6L8cwOS4.v3159rqs/s56knnGYJuA5a.dZcfPzxzHX8wz6S4YXpm3sh86lkZd3JxyZ3MX6m8T0E=")
cl.loginResult()

print "=============[ Login Success Sayang ]=============\n=============[ Ya Allah, Semoga Jangan STUCK :( ]============="
reload(sys)
sys.setdefaultencoding('utf-8')

helpMenu ="""

冫𖣐－sᴇʟғʙᴏᴛ
『 📶 －ᴠᴇʀsɪᴏɴ 4.0 』
╔═══════════════╗
╠͜͡✰ ʜɢ「ʜᴇʟᴘ ɢʀᴏᴜᴘ」
╠͜͡✰ ʜᴋ「ʜᴇʟᴘ ᴋɪᴄᴋᴇʀ」
╠͜͡✰ ʜᴜ「ʜᴇʟᴘ ᴜᴛɪʟɪᴛʏ」
╠͜͡✰ ʜs「ʜᴇʟᴘ sᴇᴛᴛɪɴɢ」
╠͜͡✰ ʜᴘ「ʜᴇʟᴘ ᴘʀᴏᴛᴇᴄᴛ」
╠͜͡✰ ᴛʀ「ʜᴇʟᴘ ᴛʀᴀɴsʟᴀᴛᴇ」
╠͜͡✰ ᴘʀᴏғɪʟᴇ「ʜᴇʟᴘ ᴘʀᴏғɪʟᴇ」
╠͜͡✰ sᴇᴀʀᴄʜ「ʜᴇʟᴘ sᴇᴀʀᴄʜ」
╠͜͡✰ sᴛᴇᴀʟ「ʜᴇʟᴘ sᴛᴇᴀʟ」
╠͜͡✰ sᴘᴀᴍ「ʜᴇʟᴘ sᴘᴀᴍ」
╠͜͡✰ ғᴜɴ「ʜᴇʟᴘ ғᴜɴ」
╠͜͡✰ ᴛᴛs「ʜᴇʟᴘ ᴛᴛs」
╠͜͡✰ sᴋ「sᴇᴛᴛɪɴɢ ᴋᴇʏ」
╠͜͡✰ ᴅsᴇᴛ「ɢʀᴏᴜᴘ sᴇᴛᴛɪɴɢs」
╠͜͡✰ ᴀʙᴏᴜᴛ「ᴀʙᴏᴜᴛ ʙᴏᴛ」
╠͜͡✰ Cʀᴇᴀᴛᴏʀ
╚═══════════════╝
sᴜᴘᴘᴏʀᴛ ʙʏ :
"""
helpGroup ="""「👨‍👩‍👧‍👦」- Hᴇʟᴘ ғᴏʀ Gʀᴏᴜᴘ -「👨‍👩‍👧‍👦」

╔══════════════════╗
╠͜͡✰ ɢɪᴅ「Gɪᴅ Gʀᴜᴘ」
╠͜͡✰ ʜᴀɪ「ᴛᴀɢᴀʟʟ」
╠͜͡✰ ʜᴀʏ「ᴛᴀɢᴀʟʟ」
╠͜͡✰ ɢɪғᴛ「Hᴀᴅɪᴀʜ」
╠͜͡✰ Cᴀɴᴄᴇʟ「Cᴀɴᴄᴇʟ Rᴏᴍʙᴏɴɢᴀɴ」
╠͜͡✰ B「Cᴀɴᴄᴇʟ Sᴀᴛᴜ²」
╠͜͡✰ Oᴜᴛ「Kᴇʟᴜᴀʀ Gʀᴜᴘ」
╠͜͡✰ Oᴜᴛ:「Nᴀᴍᴀ Gʀᴜᴘ」
╠͜͡✰ Oᴜᴛᴀʟʟ「Kᴇʟᴜᴀʀ Sᴇᴍᴜᴀ Gʀᴜᴘ」
╠͜͡✰ ᴄɪᴅᴜᴋ「Sᴇᴛ Sɪᴅᴇʀ」
╠͜͡✰ ɪɴᴛɪᴘ「Cᴇᴋ Sɪᴅᴇʀ」
╠͜͡✰ ʟᴜʀᴋ ᴏɴ「Sᴇᴛ Lᴜʀᴋ」
╠͜͡✰ ʟᴜʀᴋ ᴏғғ「Mᴇɴɢʜᴀᴘᴜs Sᴇᴛ Lᴜʀᴋ」
╠͜͡✰ ʟᴜʀᴋᴇʀs「Cᴇᴋ Lᴜʀᴋᴇʀs」
╠͜͡✰ ʙǫʀ「Bᴜᴋᴀ QR Gʀᴜᴘ」
╠͜͡✰ ᴛǫʀ「Tᴜᴛᴜᴘ QR Gʀᴜᴘ」
╠͜͡✰ Iɴᴠɪᴛᴇ「Sᴇɴᴅ Cᴏɴᴛᴀᴄᴛ」
╠͜͡✰ Iɴᴠɪᴛᴇ:「MID」
╠͜͡✰ Gᴜʀʟ「Bᴜᴋᴀ QR » Lɪɴᴋ QR」
╠͜͡✰ Uʀʟ「Lɪɴᴋ QR」
╠͜͡✰ Gɴ「Nᴀᴍᴀ Gʀᴜᴘ」
╠͜͡✰ Gɪɴғᴏ「Iɴғᴏ Gʀᴜᴘ」
╠͜͡✰ Gʟɪsᴛ「Dᴀғᴛᴀʀ Gʀᴜᴘ」
╠͜͡✰ Gʟɪᴅ「Dᴀғᴛᴀʀ Gʀᴜᴘ GID」
╠͜͡✰ Iɴғᴏ ɢʀᴜᴘ:「Vɪᴀ Gɪᴅ」
╚═════════════════╝"""
helpKicker = """「💀」- Hᴇʟᴘ ғᴏʀ Kɪᴄᴋᴇʀ -「💀」

╔═════════════════╗
╠͜͡✰ Nᴜᴄᴋ「Nᴜᴋᴇ」
╠͜͡✰ Sᴀᴘᴜ「Cʟᴇᴀɴsᴇ」
╠͜͡✰ ᴛᴀᴍᴘᴏʟ @「Tᴀɢ」
╠͜͡✰ Sʟᴀɪɴ @「Tᴀɢ」
╠͜͡✰ ᴜɴʙᴀɴ @「Tᴀɢ」
╠͜͡✰ ᴜɴʙᴀɴ:「Mɪᴅ」
╠͜͡✰ ᴜɴʙᴀɴ「Sᴇɴᴅ Cᴏɴᴛᴀᴄᴛ」
╠͜͡✰ ʙᴀɴ @「Tᴀɢ」
╠͜͡✰ ʙᴀɴ:「Mɪᴅ」
╠͜͡✰ ʙᴀɴ「Sᴇɴᴅ Cᴏɴᴛᴀᴄᴛ」
╠͜͡✰ Bᴀɴ ᴀʟʟ「Bᴀɴ Mᴇᴍʙᴇʀ Gʀᴜᴘ」
╠͜͡✰ Bᴀɴʟɪsᴛ「Cᴇᴋ Bᴀɴʟɪsᴛ」
╠͜͡✰ ᴄᴏɴʙᴀɴ「Cᴇᴋ Kᴏɴᴛᴀᴋ Bᴀɴʟɪsᴛ」
╠͜͡✰ .ʙᴍ「Cᴇᴋ Bᴀɴʟɪsᴛ Mɪᴅ」
╠͜͡✰ Cʟᴇᴀʀ ʙᴀɴ「Hᴀᴘᴜs Bᴀɴʟɪsᴛ」
╠͜͡✰ ᴛᴀᴍᴘᴏʟ:「MID」
╠͜͡✰ ᴛᴀᴍᴘᴏʟ「Mᴇɴᴀᴍᴘᴏʟ Bᴀɴʟɪsᴛ」
╚═════════════════╝"""
helpUtility = """「🛠️」- Hᴇʟᴘ ғᴏʀ Uᴛɪʟɪᴛʏ -「🛠️」

╔══════════════════╗
╠͜͡✰ .ᴄᴄ「Mᴇɴɢɪʀɪᴍ Cʀᴀsʜ」
╠͜͡✰ Uɴɪ「Mᴇɴɢɪʀɪᴍ Uɴɪᴄᴏᴅᴇ」
╠͜͡✰ Bᴄ「Bᴄ Kᴇ Sᴇᴍᴜᴀ」
╠͜͡✰ Bᴄᴄ「Bᴄ Kᴇ Sᴇᴍᴜᴀ Kᴏɴᴛᴀᴋ」
╠͜͡✰ Bᴄɢ「Bᴄ Kᴇ Sᴇᴍᴜᴀ Gʀᴜᴘ」
╠͜͡✰ Mʟɪsᴛ「Dᴀғᴛᴀʀ Mᴇᴍʙᴇʀ Gʀᴜᴘ」
╠͜͡✰ Fʟɪsᴛ「Dᴀғᴛᴀʀ Tᴇᴍᴀɴ」
╠͜͡✰ ᴅsᴘ「Cᴇᴋ Sᴘᴇᴇᴅ」
╠͜͡✰ ŤĽ:「Pᴏsᴛɪɴɢ Sᴇsᴜᴀᴛᴜ ᴅɪ TL」
╠͜͡✰ ᴛᴏᴅᴀʏ「Hᴀʀɪ Iɴɪ」
╠͜͡✰ Iɴᴠ:.ɢᴄ「Iɴᴠɪᴛᴇ Cʀᴇᴀᴛᴏʀ Gʀᴜᴘ」
╠͜͡✰ .ɢᴄ「Cᴇᴋ Cʀᴇᴀᴛᴏʀ Gʀᴜᴘ」
╠͜͡✰ Aᴅᴅ:「Aᴅᴅ Oʀᴀɴɢ Vɪᴀ MID」
╠͜͡✰ .ʀᴊ「Rᴇᴊᴇᴄᴛ Uɴᴅᴀɴɢᴀɴ Gʀᴜᴘ」
╠͜͡✰ .ʀᴛ「Cᴇᴋ Wᴀᴋᴛᴜ Bᴏᴛ Bᴇʀᴊᴀʟᴀɴ」
╠͜͡✰ .ʀᴄ「Mᴇɴɢʜᴀᴘᴜs Sᴇᴍᴜᴀ Cʜᴀᴛ」
╠͜͡✰ .ʀs「Mᴇʀᴇsᴛᴀʀᴛ Bᴏᴛ」
╠͜͡✰ ᴋᴇᴅᴀᴘᴋᴇᴅɪᴘ「ᴛᴇxᴛ」
╠͜͡✰ Iᴍᴀɢᴇᴛᴇxᴛ「ᴛᴇxᴛ」
╚══════════════════╝"""
helpSettings = """「⚙️」- Hᴇʟᴘ ғᴏʀ Sᴇᴛᴛɪɴɢ -「⚙️」
    
╔══════════════╗
╠͜͡✰ 「Lɪᴋᴇ ᴏɴ/ᴏғғ」     
╠͜͡✰ 「Aᴅᴅ ᴏɴ/ᴏғғ」 	 
╠͜͡✰ 「Aᴜᴛᴏ ᴊᴏɪɴ ᴏɴ/ᴏғғ」 	   
╠͜͡✰ 「Cᴏɴᴛᴀᴄᴛ ᴏɴ/ᴏғғ」 	
╠͜͡✰ 「Lᴇᴀᴠᴇ ᴏɴ/ᴏғғ」  
╠͜͡✰ 「Sʜᴀʀᴇ ᴏɴ/ᴏғғ」           
╠͜͡✰ 「Aᴜᴛᴏ ʀᴇᴀᴅ ᴏɴ/ᴏғғ」
╠͜͡✰ 「Tᴀɢ ᴏɴ/ᴏғғ」
╠͜͡✰ 「Tʙᴀɴ ᴏɴ/ᴏғғ」
╠͜͡✰ 「Mɪᴍɪᴄ ᴏɴ/ᴏғғ」
╠͜͡✰ 「Tᴀɢᴠɴ ᴏɴ/ᴏғғ」
╠͜͡✰ 「TᴀɢBᴀɴ ᴏɴ/ᴏғғ」
╠͜͡✰ 「Wᴇʟᴄᴏᴍᴇᴍsɢ ᴏɴ/ᴏғғ」
╠͜͡✰ 「Cᴇᴋ sɪᴅᴇʀ ᴏɴ/ᴏғғ」
╠͜͡✰ 「Sɪᴍɪsɪᴍɪ ᴏɴ/ᴏғғ」
╠͜͡✰ 「Sᴛɪᴄᴋᴇʀ ᴏɴ/ᴏғғ」
╠͜͡✰ 「Jᴀᴍ ᴏɴ/ᴏғғ」			   
╠͜͡✰ 「Jᴀᴍ sᴀʏ:」			   
╠͜͡✰ 「Cᴏᴍ ᴏɴ/ᴏғғ」	
╠͜͡✰ 「Mᴇssᴀɢᴇ sᴇᴛ:」	
╠͜͡✰ 「Cᴏᴍᴍᴇɴᴛ sᴇᴛ:」	
╠͜͡✰ 「Pᴇsᴀɴ ᴀᴅᴅ:」	
╠͜͡✰ 「Pᴇsᴀɴ ᴀᴅᴅ ᴄᴇᴋ」
╚══════════════╝"""
helpProtect = """「🛡️」- Hᴇʟᴘ ғᴏʀ Pʀᴏᴛᴇᴄᴛ -「🛡️」

╔═══════════════╗
╠͜͡✰ 「Aʟʟᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ」      
╠͜͡✰ 「ᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ」			   
╠͜͡✰ 「ǫʀᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ」			   
╠͜͡✰ 「ɪɴᴠɪᴛᴇᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ」			   
╠͜͡✰ 「cᴀɴᴄᴇʟᴘʀᴏᴛᴇᴄᴛ ᴏɴ/ᴏғғ」
╚═══════════════╝"""
helpSteal = """「👁️」- Hᴇʟᴘ ғᴏʀ Sᴛᴇᴀʟ -「👁️」

╔═════════════════╗
╠͜͡✰ Sᴛᴇᴀʟ ɢᴘɪᴄ:「Fᴏᴛᴏ Gʀᴜᴘ」
╠͜͡✰ Sᴛᴇᴀʟ ɢᴘɪᴄᴛ「Fᴏᴛᴏ Gʀᴜᴘ」
╠͜͡✰ Sᴛᴇᴀʟ ɢɴ「Nᴀᴍᴀ Gʀᴜᴘ」
╠͜͡✰ Sᴛᴇᴀʟ ᴅᴘ @「DP」
╠͜͡✰ Sᴛᴇᴀʟ ᴄᴏᴠᴇʀ @「Cᴏᴠᴇʀ」
╠͜͡✰ Sᴛᴇᴀʟ ᴠɪᴅ @「Vɪᴅᴇᴏ」
╠͜͡✰ Sᴛᴇᴀʟ ɴᴀᴍᴇ @「Nᴀᴍᴀ」
╠͜͡✰ Sᴛᴇᴀʟ ʙɪᴏ @「Bɪᴏ」
╠͜͡✰ Sᴛᴇᴀʟ ᴍɪᴅ @「Mɪᴅ」
╠͜͡✰ Sᴛᴇᴀʟ ᴄᴏɴᴛᴀᴄᴛ @「Kᴏɴᴛᴀᴋ」
╠͜͡✰ Sᴛᴇᴀʟ ᴄᴏɴᴛᴀᴄᴛ:「Mɪᴅ」
╠͜͡✰ Sᴛᴇᴀʟ ɪɴғᴏ @「Iɴғᴏ」
╚═════════════════╝"""
helpSearch = """「🔍」- Hᴇʟᴘ ғᴏʀ Sᴇᴀʀᴄʜ -「🔎」

╔═══════════════╗
╠͜͡✰ .ᴍs「Mᴜsɪᴄ」
╠͜͡✰ .ʟʀ「Lɪʀɪᴋ」
╠͜͡✰ .ʏᴛ「Yᴏᴜᴛᴜʙᴇ」
╠͜͡✰ .ɪɢ「Iɴsᴛᴀɢʀᴀᴍ」
╠͜͡✰ .ᴡᴘ「Wɪᴋɪᴘᴇᴅɪᴀ」
╠͜͡✰ .ᴘs「Pʟᴀʏsᴛᴏʀᴇ」
╠͜͡✰ .ғʙ「Fᴀᴄᴇʙᴏᴏᴋ」
╠͜͡✰ .ɢʟ「Gᴏᴏɢʟᴇ」
╠͜͡✰ .ɢɪ「Gᴏᴏɢʟᴇ Iᴍᴀɢᴇ」
╠͜͡✰ .ɢᴛ「GɪᴛHᴜʙ」
╠͜͡✰ .ᴘᴛ「PʀᴀʏTɪᴍᴇ」
╠͜͡✰ .ʟᴄ「Lᴏᴄᴀᴛɪᴏɴ」
╠͜͡✰ .ᴄᴡ「Cᴜᴀᴄᴀ」
╚═══════════════╝"""
helpSpam = """「🗣️」- Hᴇʟᴘ ғᴏʀ Sᴘᴀᴍ -「🗣️」

╔═══════════════════╗
╠͜͡✰ ᴄɪᴜᴍ「ᴍɪᴅ-ᴊᴜᴍʟᴀʜ」
╠͜͡✰ Sᴘᴀᴍ ɢʀᴜᴘ「ᴍɪᴅ-ᴊᴜᴍʟᴀʜ」
╠͜͡✰ Sᴘᴀᴍ ᴏɴ/ᴏғғ「ᴊᴜᴍʟᴀʜ-ᴛᴇxᴛ」
╠͜͡✰ sᴘᴀᴍ ɢɪғᴛ「Mᴇɴɢsᴘᴀᴍ Gɪғᴛ」
╠͜͡✰ Wᴏʏ @「Mᴇɴɢsᴘᴀᴍ 1K Pᴇsᴀɴ」
╠͜͡✰ Sᴘᴀᴍᴛᴀɢ @「Mᴇɴɢsᴘᴀᴍ Tᴀɢ」
╠͜͡✰ Sᴘᴀᴍᴛᴀɢ ᴘᴄ @「〃sᴘᴀᴍ PC Tᴀɢ」
╚═══════════════════╝"""
helpProfile = """「👤」- Hᴇʟᴘ ғᴏʀ Pʀᴏғɪʟᴇ -「👤」

╔════════════════════╗
╠͜͡✰ Mʏᴄᴏᴠᴇʀ「Cᴏᴠᴇʀ Aɴᴅᴀ」
╠͜͡✰ Mʏᴘɪᴄᴛ「DP Aɴᴅᴀ」
╠͜͡✰ Mʏɴᴀᴍᴇ「Uʙᴀʜ Nᴀᴍᴀ Aɴᴅᴀ」
╠͜͡✰ Mʏʙɪᴏ「Uʙᴀʜ Bɪᴏ Aɴᴅᴀ」
╠͜͡✰ Mʏɴ「Nᴀᴍᴀ Aɴᴅᴀ」
╠͜͡✰ Mʏʙ「Bɪᴏ Aɴᴅᴀ」
╠͜͡✰ Mʏᴛ「Tᴏᴋᴇɴ Aɴᴅᴀ」
╠͜͡✰ ᴍᴇ「Kᴏɴᴛᴀᴋ Aɴᴅᴀ」
╠͜͡✰ ᴍɪᴅ「Mɪᴅ Aɴᴅᴀ」
╠͜͡✰ Tᴀɢ ᴍᴇ「Tᴀɢ Aɴᴅᴀ」
╠͜͡✰ Ꮯ @「Cᴏᴘʏ Pʀᴏғɪʟᴇ Oʀᴀɴɢ」
╠͜͡✰ Bᴀᴄᴋᴜᴘ「Bᴀᴄᴋᴜᴘ Pʀᴏғɪʟᴇ Aɴᴅᴀ」
╚════════════════════╝"""
helpMimic = """「💬」- Hᴇʟᴘ ғᴏʀ Mɪᴍɪᴄ -「💬」

╔═════════════════════╗
╠͜͡✰ Mɪᴄᴀᴅᴅ @「Mᴇɴᴀᴍʙᴀʜ Tᴀʀɢᴇᴛ」
╠͜͡✰ Mɪᴄᴅᴇʟ @「Mᴇɴɢʜᴀᴘᴜs Tᴀʀɢᴇᴛ」
╠͜͡✰ Mɪᴍɪᴄ ᴛᴀʀɢᴇᴛ「[ᴍᴇ, ᴛᴀʀɢᴇᴛ] Mᴇᴍɪʟɪʜ Oᴘsɪ」
╠͜͡✰ Mɪᴄʟɪsᴛ「Mᴇʟɪʜᴀᴛ Dᴀғᴛᴀʀ Mɪᴍɪᴄ」
╚═════════════════════╝"""
helpFun = """「🐈」- Hᴇʟᴘ ғᴏʀ Fᴜɴ -「🐈」

╔════════╗
╠͜͡✰ 「ʙᴇʀɪsɪᴋ」
╠͜͡✰ 「ᴋᴀᴄᴀɴɢ」
╠͜͡✰ 「ᴋᴇʀᴀᴅ」
╠͜͡✰ 「ʜᴀʟᴀʜ」
╠͜͡✰ 「ɢʙʟᴋ」
╠͜͡✰ 「ʜᴍᴍ」
╠͜͡✰ 「ᴘᴘǫ」
╠͜͡✰ 「ᴅɪʜ」
╠͜͡✰ 「ᴀsᴡ」
╠͜͡✰ 「–_–」
╠͜͡✰ 「:3」
╚════════╝"""
helpTTS = """「🎵」- Hᴇʟᴘ ғᴏʀ TTS -「🎵」

╔════════════════╗
╠͜͡✰ 「ᴀғ : ᴀғʀɪᴋᴀᴀɴs」
╠͜͡✰ 「sǫ : ᴀʟʙᴀɴɪᴀɴ」
╠͜͡✰ 「ᴀʀ : ᴀʀᴀʙɪᴄ」
╠͜͡✰ 「ʜʏ : ᴀʀᴍᴇɴɪᴀɴ」
╠͜͡✰ 「ʙɴ : ʙᴇɴɢᴀʟɪ」
╠͜͡✰ 「ᴄᴀ : ᴄᴀᴛᴀʟᴀɴ」
╠͜͡✰ 「ᴢʜ : ᴄʜɪɴᴇsᴇ」
╠͜͡✰ 「ᴢʜ-ᴄɴ : ᴄʜɪɴᴇsᴇ (ᴍᴀɴᴅᴀʀɪɴ/ᴄʜɪɴᴀ)」
╠͜͡✰ 「ᴢʜ-ᴛᴡ : ᴄʜɪɴᴇsᴇ (ᴍᴀɴᴅᴀʀɪɴ/ᴛᴀɪᴡᴀɴ)」
╠͜͡✰ 「ᴢʜ-ʏᴜᴇ : ᴄʜɪɴᴇsᴇ (ᴄᴀɴᴛᴏɴᴇsᴇ)」
╠͜͡✰ 「ʜʀ : ᴄʀᴏᴀᴛɪᴀɴ」
╠͜͡✰ 「ᴄs : ᴄᴢᴇᴄʜ」
╠͜͡✰ 「ᴅᴀ : ᴅᴀɴɪsʜ」
╠͜͡✰ 「ɴʟ : ᴅᴜᴛᴄʜ」
╠͜͡✰ 「ᴇɴ : ᴇɴɢʟɪsʜ」
╠͜͡✰ 「ᴇɴ-ᴀᴜ : ᴇɴɢʟɪsʜ (ᴀᴜsᴛʀᴀʟɪᴀ)」
╠͜͡✰ 「ᴇɴ-ᴜᴋ : ᴇɴɢʟɪsʜ (ᴜɴɪᴛᴇᴅ ᴋɪɴɢᴅᴏᴍ)」
╠͜͡✰ 「ᴇɴ-ᴜs : ᴇɴɢʟɪsʜ (ᴜɴɪᴛᴇᴅ sᴛᴀᴛᴇs)」
╠͜͡✰ 「ᴇᴏ : ᴇsᴘᴇʀᴀɴᴛᴏ」
╠͜͡✰ 「ғɪ : ғɪɴɴɪsʜ」
╠͜͡✰ 「ғʀ : ғʀᴇɴᴄʜ」
╠͜͡✰ 「ᴅᴇ : ɢᴇʀᴍᴀɴ」
╠͜͡✰ 「ᴇʟ : ɢʀᴇᴇᴋ」
╠͜͡✰ 「ʜɪ : ʜɪɴᴅɪ」
╠͜͡✰ 「ʜᴜ : ʜᴜɴɢᴀʀɪᴀɴ」
╠͜͡✰ 「ɪs : ɪᴄᴇʟᴀɴᴅɪᴄ」
╠͜͡✰ 「ɪᴅ : ɪɴᴅᴏɴᴇsɪᴀɴ」
╠͜͡✰ 「ɪᴛ : ɪᴛᴀʟɪᴀɴ」
╠͜͡✰ 「ᴊᴀ : ᴊᴀᴘᴀɴᴇsᴇ」
╠͜͡✰ 「ᴋᴍ : ᴋʜᴍᴇʀ (ᴄᴀᴍʙᴏᴅɪᴀɴ)」
╠͜͡✰ 「ᴋᴏ : ᴋᴏʀᴇᴀɴ」
╠͜͡✰ 「ʟᴀ : ʟᴀᴛɪɴ」
╠͜͡✰ 「ʟᴠ : ʟᴀᴛᴠɪᴀɴ」
╠͜͡✰ 「ᴍᴋ : ᴍᴀᴄᴇᴅᴏɴɪᴀɴ」
╠͜͡✰ 「ɴᴏ : ɴᴏʀᴡᴇɢɪᴀɴ」
╠͜͡✰ 「ᴘʟ : ᴘᴏʟɪsʜ」
╠͜͡✰ 「ᴘᴛ : ᴘᴏʀᴛᴜɢᴜᴇsᴇ」
╠͜͡✰ 「ʀᴏ : ʀᴏᴍᴀɴɪᴀɴ」
╠͜͡✰ 「ʀᴜ : ʀᴜssɪᴀɴ」
╠͜͡✰ 「sʀ : sᴇʀʙɪᴀɴ」
╠͜͡✰ 「sɪ : sɪɴʜᴀʟᴀ」
╠͜͡✰ 「sᴋ : sʟᴏᴠᴀᴋ」
╠͜͡✰ 「ᴇs : sᴘᴀɴɪsʜ」
╠͜͡✰ 「ᴇs-ᴇs : sᴘᴀɴɪsʜ (sᴘᴀɪɴ)」
╠͜͡✰ 「ᴇs-ᴜs : sᴘᴀɴɪsʜ (ᴜɴɪᴛᴇᴅ sᴛᴀᴛᴇs)」
╠͜͡✰ 「sᴡ : sᴡᴀʜɪʟɪ」
╠͜͡✰ 「sᴠ : sᴡᴇᴅɪsʜ」
╠͜͡✰ 「ᴛᴀ : ᴛᴀᴍɪʟ」
╠͜͡✰ 「ᴛʜ : ᴛʜᴀɪ」
╠͜͡✰ 「ᴛʀ : ᴛᴜʀᴋɪsʜ」
╠͜͡✰ 「ᴜᴋ : ᴜᴋʀᴀɪɴɪᴀɴ」
╠͜͡✰ 「ᴠɪ : ᴠɪᴇᴛɴᴀᴍᴇsᴇ」
╠͜͡✰ 「ᴄʏ : ᴡᴇʟsʜ」
╚════════════════╝
☮️ ᴄᴏɴᴛᴏʜ : "sᴀʏ-ɪᴅ ᴡɪʟᴅᴀɴ ʙᴀɪᴋ"
╚═══════════════╝"""
helptranslate = """「🎎」- Hᴇʟᴘ ғᴏʀ Tʀᴀɴsʟᴀᴛᴇ -「🎎」

╔═════════════════╗
╠͜͡✰「ᴀғ : ᴀғʀɪᴋᴀᴀɴs」
╠͜͡✰「sǫ : ᴀʟʙᴀɴɪᴀɴ」
╠͜͡✰「ᴀᴍ : ᴀᴍʜᴀʀɪᴄ」
╠͜͡✰「ᴀʀ : ᴀʀᴀʙɪᴄ」
╠͜͡✰「ʜʏ : ᴀʀᴍᴇɴɪᴀɴ」
╠͜͡✰「ᴀᴢ : ᴀᴢᴇʀʙᴀɪᴊᴀɴɪ」
╠͜͡✰「ᴇᴜ : ʙᴀsǫᴜᴇ」
╠͜͡✰「ʙᴇ : ʙᴇʟᴀʀᴜsɪᴀɴ」
╠͜͡✰「ʙɴ : ʙᴇɴɢᴀʟɪ」
╠͜͡✰「ʙs : ʙᴏsɴɪᴀɴ」
╠͜͡✰「ʙɢ : ʙᴜʟɢᴀʀɪᴀɴ」
╠͜͡✰「ᴄᴀ : ᴄᴀᴛᴀʟᴀɴ」
╠͜͡✰「ᴄᴇʙ : ᴄᴇʙᴜᴀɴᴏ」
╠͜͡✰「ɴʏ : ᴄʜɪᴄʜᴇᴡᴀ」
╠͜͡✰「ᴢʜ-ᴄɴ : ᴄʜɪɴᴇsᴇ (sɪᴍᴘʟɪғɪᴇᴅ)」
╠͜͡✰「ᴢʜ-ᴛᴡ : ᴄʜɪɴᴇsᴇ (ᴛʀᴀᴅɪᴛɪᴏɴᴀʟ)」
╠͜͡✰「ᴄᴏ : ᴄᴏʀsɪᴄᴀɴ」
╠͜͡✰「ʜʀ : ᴄʀᴏᴀᴛɪᴀɴ」
╠͜͡✰「ᴄs : ᴄᴢᴇᴄʜ」
╠͜͡✰「ᴅᴀ : ᴅᴀɴɪsʜ」
╠͜͡✰「ɴʟ : ᴅᴜᴛᴄʜ」
╠͜͡✰「ᴇɴ : ᴇɴɢʟɪsʜ」
╠͜͡✰「ᴇᴏ : ᴇsᴘᴇʀᴀɴᴛᴏ」
╠͜͡✰「ᴇᴛ : ᴇsᴛᴏɴɪᴀɴ」
╠͜͡✰「ᴛʟ : ғɪʟɪᴘɪɴᴏ」
╠͜͡✰「ғɪ : ғɪɴɴɪsʜ」
╠͜͡✰「ғʀ : ғʀᴇɴᴄʜ」
╠͜͡✰「ғʏ : ғʀɪsɪᴀɴ」
╠͜͡✰「ɢʟ : ɢᴀʟɪᴄɪᴀɴ」
╠͜͡✰「ᴋᴀ : ɢᴇᴏʀɢɪᴀɴ」
╠͜͡✰「ᴅᴇ : ɢᴇʀᴍᴀɴ」
╠͜͡✰「ᴇʟ : ɢʀᴇᴇᴋ」
╠͜͡✰「ɢᴜ : ɢᴜᴊᴀʀᴀᴛɪ」
╠͜͡✰「ʜᴛ : ʜᴀɪᴛɪᴀɴ ᴄʀᴇᴏʟᴇ」
╠͜͡✰「ʜᴀ : ʜᴀᴜsᴀ」
╠͜͡✰「ʜᴀᴡ : ʜᴀᴡᴀɪɪᴀɴ」
╠͜͡✰「ɪᴡ : ʜᴇʙʀᴇᴡ」
╠͜͡✰「ʜɪ : ʜɪɴᴅɪ」
╠͜͡✰「ʜᴍɴ : ʜᴍᴏɴɢ」
╠͜͡✰「ʜᴜ : ʜᴜɴɢᴀʀɪᴀɴ」
╠͜͡✰「ɪs : ɪᴄᴇʟᴀɴᴅɪᴄ」
╠͜͡✰「ɪɢ : ɪɢʙᴏ」
╠͜͡✰「ɪᴅ : ɪɴᴅᴏɴᴇsɪᴀɴ」
╠͜͡✰「ɢᴀ : ɪʀɪsʜ」
╠͜͡✰「ɪᴛ : ɪᴛᴀʟɪᴀɴ」
╠͜͡✰「ᴊᴀ : ᴊᴀᴘᴀɴᴇsᴇ」
╠͜͡✰「ᴊᴡ : ᴊᴀᴠᴀɴᴇsᴇ」
╠͜͡✰「ᴋɴ : ᴋᴀɴɴᴀᴅᴀ」
╠͜͡✰「ᴋᴋ : ᴋᴀᴢᴀᴋʜ」
╠͜͡✰「ᴋᴍ : ᴋʜᴍᴇʀ」
╠͜͡✰「ᴋᴏ : ᴋᴏʀᴇᴀɴ」
╠͜͡✰「ᴋᴜ : ᴋᴜʀᴅɪsʜ (ᴋᴜʀᴍᴀɴᴊɪ)」
╠͜͡✰「ᴋʏ : ᴋʏʀɢʏᴢ」
╠͜͡✰「ʟᴏ : ʟᴀᴏ」
╠͜͡✰「ʟᴀ : ʟᴀᴛɪɴ」
╠͜͡✰「ʟᴠ : ʟᴀᴛᴠɪᴀɴ」
╠͜͡✰「ʟᴛ : ʟɪᴛʜᴜᴀɴɪᴀɴ」
╠͜͡✰「ʟʙ : ʟᴜxᴇᴍʙᴏᴜʀɢɪsʜ」
╠͜͡✰「ᴍᴋ : ᴍᴀᴄᴇᴅᴏɴɪᴀɴ」
╠͜͡✰「ᴍɢ : ᴍᴀʟᴀɢᴀsʏ」
╠͜͡✰「ᴍs : ᴍᴀʟᴀʏ」
╠͜͡✰「ᴍʟ : ᴍᴀʟᴀʏᴀʟᴀᴍ」
╠͜͡✰「ᴍᴛ : ᴍᴀʟᴛᴇsᴇ」
╠͜͡✰「ᴍɪ : ᴍᴀᴏʀɪ」
╠͜͡✰「ᴍʀ : ᴍᴀʀᴀᴛʜɪ」
╠͜͡✰「ᴍɴ : ᴍᴏɴɢᴏʟɪᴀɴ」
╠͜͡✰「ᴍʏ : ᴍʏᴀɴᴍᴀʀ (ʙᴜʀᴍᴇsᴇ)」
╠͜͡✰「ɴᴇ : ɴᴇᴘᴀʟɪ」
╠͜͡✰「ɴᴏ : ɴᴏʀᴡᴇɢɪᴀɴ」
╠͜͡✰「ᴘs : ᴘᴀsʜᴛᴏ」
╠͜͡✰「ғᴀ : ᴘᴇʀsɪᴀɴ」
╠͜͡✰「ᴘʟ : ᴘᴏʟɪsʜ」
╠͜͡✰「ᴘᴛ : ᴘᴏʀᴛᴜɢᴜᴇsᴇ」
╠͜͡✰「ᴘᴀ : ᴘᴜɴᴊᴀʙɪ」
╠͜͡✰「ʀᴏ : ʀᴏᴍᴀɴɪᴀɴ」
╠͜͡✰「ʀᴜ : ʀᴜssɪᴀɴ」
╠͜͡✰「sᴍ : sᴀᴍᴏᴀɴ」
╠͜͡✰「ɢᴅ : sᴄᴏᴛs ɢᴀᴇʟɪᴄ」
╠͜͡✰「sʀ : sᴇʀʙɪᴀɴ」
╠͜͡✰「sᴛ : sᴇsᴏᴛʜᴏ」
╠͜͡✰「sɴ : sʜᴏɴᴀ」
╠͜͡✰「sᴅ : sɪɴᴅʜɪ」
╠͜͡✰「sɪ : sɪɴʜᴀʟᴀ」
╠͜͡✰「sᴋ : sʟᴏᴠᴀᴋ」
╠͜͡✰「sʟ : sʟᴏᴠᴇɴɪᴀɴ」
╠͜͡✰「sᴏ : sᴏᴍᴀʟɪ」
╠͜͡✰「ᴇs : sᴘᴀɴɪsʜ」
╠͜͡✰「sᴜ : sᴜɴᴅᴀɴᴇsᴇ」
╠͜͡✰「sᴡ : sᴡᴀʜɪʟɪ」
╠͜͡✰「sᴠ : sᴡᴇᴅɪsʜ」
╠͜͡✰「ᴛɢ : ᴛᴀᴊɪᴋ」
╠͜͡✰「ᴛᴀ : ᴛᴀᴍɪʟ」
╠͜͡✰「ᴛᴇ : ᴛᴇʟᴜɢᴜ」
╠͜͡✰「ᴛʜ : ᴛʜᴀɪ」
╠͜͡✰「ᴛʀ : ᴛᴜʀᴋɪsʜ」
╠͜͡✰「ᴜᴋ : ᴜᴋʀᴀɪɴɪᴀɴ」
╠͜͡✰「ᴜʀ : ᴜʀᴅᴜ」
╠͜͡✰「ᴜᴢ : ᴜᴢʙᴇᴋ」
╠͜͡✰「ᴠɪ : ᴠɪᴇᴛɴᴀᴍᴇsᴇ」
╠͜͡✰「ᴄʏ : ᴡᴇʟsʜ」
╠͜͡✰「xʜ : xʜᴏsᴀ」
╠͜͡✰「ʏɪ : ʏɪᴅᴅɪsʜ」
╠͜͡✰「ʏᴏ : ʏᴏʀᴜʙᴀ」
╠͜͡✰「ᴢᴜ : ᴢᴜʟᴜ」
╠͜͡✰「ғɪʟ : ғɪʟɪᴘɪɴᴏ」
╠͜͡✰「ʜᴇ : ʜᴇʙʀᴇᴡ」
╚═════════════════╝
☮️ ᴄᴏɴᴛᴏʜ : ".ᴛʀ-ᴅᴇ ᴡɪʟᴅᴀɴ ʙᴀɪᴋ"
╚═══════════════╝"""

KAC=[cl]
protectname=[cl]
mid = cl.getProfile().mid
Bots = [mid]
admin = "u577d79f51412f92e7a28d360ca351ae4"

wait = {
    "contact":False,
    'autoJoin':False,
    'autoCancel':{"on":False,"members":20},
    'leaveRoom':True,
    'timeline':True,
    'autoAdd':True,
    'message':"Ada apa ngeadd?",
    'sticker':False,
    "lang":"JP",
    "comment":"Aᴜᴛᴏ Lɪᴋᴇ ʙʏ sujar",
    "commentOn":True,
    "autoLike":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "atjointicket":True,
    "Creator":"u577d79f51412f92e7a28d360ca351ae4",
    "help":"help",
    "me":"me",
    "tagall":"hay",
    "sttext":"apa kabar?",
    "crash":".cc",
    "runtime":".rt",
    "settings":"dset",
    "gift":"Gift",
    "tagtext":"Ada apa? Kalo penting PC aja! Jangan Tag Tag!",
    "spamgrup":"TERCYDUCK",
    "detectAll":False, 
    "cName":"",
    "alwaysRead":False,
    "removeChat":False,
    "Sider":{},
    "TagBan":False,
    "tagfoto":False,
    "tagVN":False,
    "tag":True,
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
    "welcomemsg":True,
    "ppict":{},
    "pro_pict":{},
    "userAgent": [
		"Mozilla/5.0 (X11; U; Linux i586; de; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (X11; U; Linux amd64; rv:5.0) Gecko/20100101 Firefox/5.0 (Debian)",
		"Mozilla/5.0 (X11; U; Linux amd64; en-US; rv:5.0) Gecko/20110619 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux) Gecko Firefox/5.0",
		"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 FirePHP/0.5",
		"Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux x86_64) Gecko Firefox/5.0",
		"Mozilla/5.0 (X11; Linux ppc; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (X11; Linux AMD64) Gecko Firefox/5.0",
		"Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20110619 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1; rv:6.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 6.1.1; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.2; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.1; U; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.1; rv:2.0.1) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.0; WOW64; rv:5.0) Gecko/20100101 Firefox/5.0",
		"Mozilla/5.0 (Windows NT 5.0; rv:5.0) Gecko/20100101 Firefox/5.0"
	],
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    "ricoinvite":{},
    'ROM':{},
    }
    
settings = {
    "simiSimi":{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{},
    }
    
tban = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{},
    }
 
cctv = {
     'cyduk':{},
     'point':{},
     'sidermem':{},
     }
    
setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
mybackup = cl.getProfile()
mybackup.displayName = contact.displayName
mybackup.statusMessage = contact.statusMessage
mybackup.pictureStatus = contact.pictureStatus
mulai = time.time()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)
 
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    days, hours = divmod(hours,24)
    month, days = divmod(days,30)
    years, month = divmod(month,12)
    crot, years = divmod(years,2018)
    return '%02d Tahun\n%02d Bulan\n%02d Hari\n%02d Jam\n%02d Menit\n%02d Detik.' % (years, month, days, hours, mins, secs)

def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._client.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._client.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True
      
def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e

def sendAudio(self, to_, path):
      M = Message(to=to_, text=None, contentType = 3)
      M.contentMetadata = None
      M.contentPreview = None
      M2 = self.Talk.client.sendMessage(0,M)
      M_id = M2.id
      files = {
          'file': open(path, 'rb'),
      }
      params = {
          'name': 'media',
          'oid': M_id,
          'size': len(open(path, 'rb').read()),
          'type': 'audio',
          'ver': '1.0',
      }
      data = {
          'params': json.dumps(params)
      }
      r = self.post_content('https://obs-sg.line-apps.com/talk/m/upload.nhn', data=data, files=files)
      if r.status_code != 201:
          raise Exception('Upload audio failure.')
      return True
      
def sendAudioWithURL(self, to_, url):
      path = 'pythonLiness.data'
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download Audio failure.')
      try:
         self.sendAudio(to_, path)
      except Exception as e:
         raise e

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False
    
def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
        akh = akh + 2
        aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
        strt = strt + 6
        akh = akh + 4
        bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    try:
        cl.sendMessage(msg)
    except Exception as error:
        print error
       
def sendVideoWithURL(self, to_, url):
        path = 'pythonLines.data'
        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
               shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download Audio failure.')
        try:
            self.sendVideo(to_, path)
        except Exception as e:
            raise e
       
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     #If the Current Version of Python is 4.0 or above
        import urllib,request    #urllib library for Extracting web pages
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib,request.Request(url, headers = headers)
            resp = urllib,request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        #If the Current Version of Python is 2.x
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"

#Finding 'Next Image' from the given raw page
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    #If no links are found then give an error!
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"class="rg_meta"')
        start_content = s.find('"ou"',start_line+90)
        end_content = s.find(',"ow"',start_content-90)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content

#Getting all links with the help of '_images_get_next_image'
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      #Append all the links in the list named 'Links'
            time.sleep(0.1)        #Timer could be used to slow down the request for image downloads
            page = page[end_content:]
    return items

def upload_tempimage(client):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = client.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()
def NOTIFIED_LEAVE_GROUP(op):
    try:
        cl.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/"+cl.getContact(op.param2).pictureStatus)
        cl.sendText(op.param1,"Foto Orang Jelek Yang Baperan ✌")
    except Exception as e:
        print e
        print ("\n\nNOTIFIED_LEAVE_GROUP\n\n")
        return
def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 15:
             try:
                 cl.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/"+cl.getContact(op.param2).pictureStatus)
                 cl.sendText(op.param1,"Foto Orang Jelek Yang Baperan ✌")
             except Exception as e:
                 print e
                 print ("\n\nNOTIFIED_LEAVE_GROUP\n\n")
                 return
        if op.type == 17:
	   if wait["welcomemsg"] == True:
              if op.param2 not in Bots:
                 ginfo = cl.getGroup(op.param1)
                 cinfo = cl.getContact(op.param2)
                 cl.sendText(op.param1,str(cinfo.displayName)+"\nSelamat Datang Di Grup "+str(ginfo.name))
                 cl.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/"+str(cinfo.pictureStatus))
                 c = Message(to=op.param1, from_=None, text=None, contentType=13)
                 c.contentMetadata={'mid':op.param2}
                 cl.sendMessage(c)
#        if op.type == 17:
	#   if wait["welcomemsg"] == True:
#              if op.param2 not in Bots:
#                 ginfo = cl.getGroup(msg.to)
#                 gambar = ("https://s9.postimg.org/g58j60s8f/1514637355189.jpg","https://s14.postimg.org/hjeoym0z5/1511783772769.jpg","https://vignette.wikia.nocookie.net/thebreaker/images/4/42/Welcome.png/revision/latest?cb=20140706192111","https://s13.postimg.org/enqus0ck7/IMG_20171230_192241.jpg")
#                 xxx = random.choice(gambar)
#                 cl.sendImageWithURL(msg.to,xxx)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 25:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == "u577d79f51412f92e7a28d360ca351ae4":
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            cl.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = cl.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            cl.updateGroup(G)
                        except:
                            cl.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 1:
                if wait["detectAll"] == True:
                    cl.sendText(msg.to,"gambar apa itu?")
            if msg.contentType == 2:
                if wait["detectAll"] == True:
                    cl.sendText(msg.to,"Video bokep yah?!")
            if msg.contentType == 3:
                if wait["detectAll"] == True:
                    cl.sendText(msg.to, "pasti itu VN desah!")
            if msg.contentType == 6:
                if wait["detectAll"] == True:
                 if msg.toType == 0:
                    cl.sendText(msg.to, "Ngapain segala fcg vcg tai!")
            if msg.contentType == 7:
                if wait["detectAll"] == True:
                    cl.sendText(msg.to, "Stiker apa itu njay!")
            if msg.contentType == 9:
                if wait["detectAll"] == True:
                    cl.sendText(msg.to, "Makasih kak gift nya :*")
            if msg.contentType == 16:
                if wait["AutoLike"] == True:
                    url = msg.contentMetadata["postEndUrl"]
                    cl.like(url[25:58], url[66:], likeType=1003)
                    cl.comment(url[25:58], url[66:], wait["comment"])
#------------------------------------------------------------------------------------------#
            if op.type == 25:
                msg = op.message
            if "@"+cl.getProfile().displayName in msg.text:
                 if wait["tagVN"] == True:
                  aud = ("LINE_A20171224_221320477.m4a")
                  cl.sendAudio(msg.to, aud)
            if "@"+cl.getProfile().displayName in msg.text:
                 if wait["tag"] == True:
                    names = re.findall(r'@(\w+)',msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                        if mention['M'] in Bots:
                            xname = cl.getContact(msg.from_).displayName
                            xmid = cl.getContact(msg.from_).mid
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            msg.text = "@"+xname+" "+wait["tagtext"]
                            msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(msg.from_)+'}]}','EMTVER':'4'}
                            cl.sendMessage(msg)
                            c = Message(to=xmid, from_=None, text=msg.text, contentType=0)
                            c.contentMetadata={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(msg.from_)+'}]}','EMTVER':'4'}
                            cl.sendMessage(c)
            if "@"+cl.getProfile().displayName in msg.text:
             if wait["tagfoto"] == True:
              fuck = cl.getContact(msg.from_).pictureStatus
              cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/"+fuck)
              msg.contentType = 7
              msg.text = None
              msg.contentMetadata = {
                                   "STKID": "5508",
                                   "STKPKGID": "608",
                                   "STKVER": "16" }
              cl.sendMessage(msg)
            if "@" in msg.text:
             if wait["TagBan"] == True:
              asw = msg.text.replace("@","")
              cl.sendText(msg.to,"Ngapain ngetag?")
              cl.kickoutFromGroup(msg.to,[msg.from_])
            if "Info saya" in msg.text:
              kelamin = ("Waria","Laki-laki","Perempuan","Tidak Diketahui","Bencong")
              wajah = ("Standar","Ganteng","Cantik","Beruk","Hancur")
              status = ("Menikah","Pacaran","Jones")
              k = random.choice(kelamin)
              w = random.choice(wajah)
              s = random.choice(status)
              cl.sendText(msg.to,"• Nama : "+cl.getContact(msg.from_).displayName+"\n• Kelamin : "+k+"\n• Wajah : "+w+"\n• Status Kehidupan : "+s)
            if msg.text in ["line://ti/g/","http://line.me/R/ti/g/"]:
             if wait["detectAll"] == True:
              y = msg.text.replace("line://ti/g/","")
              u = msg.text.replace("http://line.me/R/ti/g/","")
              cl.sendText(msg.to,"Grup Bokep Ya!?")
            if msg.text in ["Crash","crash"]:
              dia = ("CACAT MAINANNYA CRASH","Tercyduck ingin ngecrash!","Kamu asu ngecrash terus!","crash cresh crash cresh, bikin hp orang lag anjing!")
              ngkol = random.choice(dia)
              cl.sendText(msg.to,ngkol)
              cl.kickoutFromGroup(msg.to,[msg.from_])
              cl.sendText(msg.to,"Mampus!")
            if msg.text in ["!kickall",".kickall","Nuke","Cleanse","Ratakan","Mayhem","MB Mayhem","Kickall","kickall"]:
                Peringatan = ("Manual kek jangan pake bot.","Cupu lu! Ratain pake bot!","Lain kali liat liat dulu~","ＴＥＲＣＹＤＵＣＫ")
                Vonis = random.choice(Peringatan)
                cl.sendText(msg.to, Vonis)
                cl.kickoutFromGroup(msg.to, [msg.from_])
                
        if op.type == 25:
            if wait["alwaysRead"] == True:
                if msg.toType == 0:
                    cl.sendChatChecked(msg.from_,msg.id)
                else:
                    cl.sendChatChecked(msg.to,msg.id)
                    
        if op.type == 25:
            if wait["alwaysRead"] == True:
                msg = op.message
                if msg.toType == 2:
                    msg.to = msg.to
                    msg.from_ = msg.from_
                    cl.sendChatChecked(msg.to,msg.id)
                    
        if op.type == 25:
            if wait["removeChat"] == True:
                if msg.toType == 0:
                    cl.sendChatRemoved(msg.from_,msg.id)
                else:
                    cl.sendChatRemoved(msg.to,msg.id)
        if op.type == 25:
            if wait["removeChat"] == True:
                msg = op.message
                if msg.toType == 2:
                    msg.to = msg.to
                    msg.from_ = msg.from_
                    cl.sendChatRemoved(msg.to,msg.id)
        if op.type == 25:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                cl.sendText(msg.to, "[SimiSimi] " + data['result']['response'].encode('utf-8'))
                    
        if op.type == 25:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,text)
                        
        if op.type == 25:
            msg = op.message
            if msg.from_ in tban["target"] and tban["status"] == True and tban["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        cl.sendText(msg.to,"Ngapain ngechat gblg !")
                        cl.kickoutFromGroup(msg.to,[msg.from_])
        if op.type == 11:
            if op.param3 == '1':
                if op.param1 in wait['ppict']:
                    try:
                        G = cl.getGroup(op.param1)
                    except:
                          pass
                    group.pictureStatus = wait['pro_pict'][op.param1]
                    try:
                        cl.updateGroup(G)
                    except:
                          pass
                    if op.param2 in ken:
                        pass
                    else:
                        try:
                            cl.kickoutFromGroup(op.param1,[op.param2])
                        except:
                              pass
                        cl.sendText(op.param1,"please do not change group picture-_-")
                        c = Message(to=op.param1, from_=None, text=None, contentType=13)
                        c.contentMetadata={'mid':op.param2}
                        cl.sendMessage(c)
                
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
            	if wait["ricoinvite"] == True:
                     if msg.from_ in admin:
                         _name = msg.contentMetadata["displayName"]
                         invite = msg.contentMetadata["mid"]
                         groups = cl.getGroup(msg.to)
                         pending = groups.invitee
                         targets = []
                         for s in groups.members:
                             if _name in s.displayName:
                                 cl.sendText(msg.to,"Si " + _name + " udah disini!")
                                 break
                             elif invite in wait["blacklist"]:
                                 cl.sendText(msg.to,"Sorry, " + _name + " On Banlist")
                                 cl.sendText(msg.to,"Call my daddy to use command !, \n➡unban: " + invite)
                                 break                             
                             else:
                                 targets.append(invite)
                         if targets == []:
                             pass
                         else:
                             for target in targets:
                                 try:
                                     cl.findAndAddContactsByMid(target)
                                     cl.inviteIntoGroup(msg.to,[target])
                                     random.choice(KAC).sendText(msg.to,"Sukses menginvite gembel ini😆: \n➡ " + _name)
                                     wait2["ricoinvite"] = False
                                     break                              
                                 except:             
                                          cl.sendText(msg.to,"Your Account Limit Invitation.")
                                          wait2["ricoinvite"] = False
                                          break
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam👈")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"Itu tidak berkomentar👈")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"Tidak ada dalam daftar hitam👈")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"sudah masuk daftar hitam")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"Done👈")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"Done👈")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "Post URL Yang Diatas\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
#taruh di sebelum elif msg.text is None
            elif msg.contentType == 7: # <-- elif atau if tergantung posisinya di awal apa ditengah
                if wait['sticker'] == True:
                    stk_id = msg.contentMetadata['STKID']
                    stk_ver = msg.contentMetadata['STKVER']
                    pkg_id = msg.contentMetadata['STKPKGID']
                    filler = "『 Sticker Check 』\nSTKID : %s\nSTKPKGID : %s\nSTKVER : %s\n『 Link 』\nline://shop/detail/%s" % (stk_id,pkg_id,stk_ver,pkg_id)
                    cl.sendText(msg.to, filler)
                else:
                    pass
                
            elif msg.text is None:
                return
#===========HELP SECTION=========================================================================================
#            elif msg.text.lower()  == wait["help"]:
#                    cl.sendText(msg.to,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞\n\n冫𖣐－TGB sᴇʟғʙᴏᴛ\n『 📶 －ᴠᴇʀsɪᴏɴ 4.0 』\n🃏ʜᴇʟᴘ ᴋᴇʏ : "+wait["help"]+"\n╔═════════════════════╗\n╠͜͡✰ ʜɢ「ʜᴇʟᴘ ɢʀᴏᴜᴘ」\n╠͜͡✰ ʜᴋ「ʜᴇʟᴘ ᴋɪᴄᴋᴇʀ」\n╠͜͡✰ ʜᴜ「ʜᴇʟᴘ ᴜᴛɪʟɪᴛʏ」\n╠͜͡✰ ʜs「ʜᴇʟᴘ sᴇᴛᴛɪɴɢ」\n╠͜͡✰ ʜᴘ「ʜᴇʟᴘ ᴘʀᴏᴛᴇᴄᴛ」\n╠͜͡✰ ᴛʀ「ʜᴇʟᴘ ᴛʀᴀɴsʟᴀᴛᴇ」\n╠͜͡✰ ᴘʀᴏғɪʟᴇ「ʜᴇʟᴘ ᴘʀᴏғɪʟᴇ」\n╠͜͡✰ sᴇᴀʀᴄʜ「ʜᴇʟᴘ sᴇᴀʀᴄʜ」\n╠͜͡✰ sᴛᴇᴀʟ「ʜᴇʟᴘ sᴛᴇᴀʟ」\n╠͜͡✰ sᴘᴀᴍ「ʜᴇʟᴘ sᴘᴀᴍ」\n╠͜͡✰ ғᴜɴ「ʜᴇʟᴘ ғᴜɴ」\n╠͜͡✰ ᴛᴛs「ʜᴇʟᴘ ᴛᴛs」\n╠͜͡✰ sᴋ「sᴇᴛᴛɪɴɢ ᴋᴇʏ」\n╠͜͡✰ ᴅsᴇᴛ「ɢʀᴏᴜᴘ sᴇᴛᴛɪɴɢs」\n╠͜͡✰ ᴀʙᴏᴜᴛ「ᴀʙᴏᴜᴛ ʙᴏᴛ」\n╚═════════════════════╝\nsᴜᴘᴘᴏʀᴛ ʙʏ :\nᎢ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞\n 👤「ᴄᴏɴᴛᴀᴄᴛ ᴘᴇʀsᴏɴᴀʟ」\n line://ti/p/TtnMdaDG_d")
            elif msg.text.lower()  == wait["help"]:
                   cl.sendText(msg.to,helpMenu)
            elif "Set help: " in msg.text:
                wait["help"] = msg.text.replace("Set help: ","")
                cl.sendText(msg.to,"Help Key Berhasil Diubah Menjadi : 「"+wait["help"]+"」")
            elif msg.text.lower()  == 'hg':
                   cl.sendText(msg.to,helpGroup)
            elif msg.text.lower()  == 'tr':
                   cl.sendText(msg.to,helptranslate)
            elif msg.text.lower()  == 'hk':
                   cl.sendText(msg.to,helpKicker)
            elif msg.text.lower()  == 'hu':
                   cl.sendText(msg.to,helpUtility)
            elif msg.text.lower()  == 'hs':
                   cl.sendText(msg.to,helpSettings)
            elif msg.text.lower()  == 'hp':
                   cl.sendText(msg.to,helpProtect)
            elif msg.text.lower()  == 'steal':
                   cl.sendText(msg.to,helpSteal)
            elif msg.text.lower()  == 'profile':
                   cl.sendText(msg.to,helpProfile)
            elif msg.text.lower()  == 'spam':
                   cl.sendText(msg.to,helpSpam)
            elif msg.text.lower()  == 'search':
                   cl.sendText(msg.to,helpSearch)
            elif msg.text.lower()  == 'mimic':
                   cl.sendText(msg.to,helpMimic)
            elif msg.text.lower()  == 'tts':
                   cl.sendText(msg.to,helpTTS)
            elif msg.text.lower()  == 'fun':
                   cl.sendText(msg.to,helpFun)
            elif msg.text.lower()  == 'sk':
                   sk = ""
                   sk+="「🗝️」- Hᴇʟᴘ ғᴏʀ Kᴇʏ -「🗝️」\n"
                   sk+="╔═══════════════╗\n"
                   sk+="╠͜͡✰ ʜᴇʟᴘ「"+wait["help"]+"」\n"
                   sk+="╠͜͡✰ ᴍᴇ「"+wait["me"]+"」\n"
                   sk+="╠͜͡✰ ᴛᴀɢᴀʟʟ「"+wait["tagall"]+"」\n"
                   sk+="╠͜͡✰ ɴᴀᴍᴀ sᴘᴀᴍɢʀᴜᴘ「"+wait["spamgrup"]+"」\n"
                   sk+="╠͜͡✰ sᴘᴀᴍᴛᴀɢ ᴛᴇxᴛ「"+wait["sttext"]+"」\n"
                   sk+="╠͜͡✰ ᴛᴀɢ ᴛᴇxᴛ「"+wait["tagtext"]+"」\n"
                   sk+="╠͜͡✰ ᴄʀᴀsʜ「.ᴄᴄ」 \n"
                   sk+="╠͜͡✰ ʀᴜɴᴛɪᴍᴇ「"+wait["runtime"]+"」\n"
                   sk+="╠͜͡✰ sᴇᴛᴛɪɴɢs「"+wait["settings"]+"」\n"
                   sk+="╠͜͡✰ ɢɪғᴛ「"+wait["gift"]+"」\n"
                   sk+="╚═══════════════╝\n"
                   sk+="💡 Cᴀʀᴀ Mᴇɴɢᴀᴛᴜʀ Kᴇʏ\n"
                   sk+="📄 Sᴇᴛ [ᴋᴇʏ]: [ᴋᴇʏ ʏɢ ᴍᴀᴜ ᴅɪ ᴀᴛᴜʀ]\n"
                   sk+="📄 Cᴏɴᴛᴏʜ:\nSᴇᴛ ᴍᴇ: ᴄᴏɢᴀɴ"
                   cl.sendText(msg.to,sk)
#===========HELP SECTION===============================================
#----------------ABOUT SECTION----------#
            elif "about" in msg.text: #ABOUT BOT#
               if msg.from_ in admin:
                x = "「Aʙᴏᴜᴛ Bᴏᴛ」\nTGB “Bᴏᴛ” Eᴅɪᴛɪᴏɴ♪\n"
                x+="Tɪᴍᴇ: " + datetime.today().strftime('%H:%M:%S') + " \n\n"
                x+="「Bᴏᴛ Iɴғᴏʀᴍᴀᴛɪᴏɴ」\n"
                x+="╠═════════════════════\n"
                x+="☸️ Bᴏᴛ Cʀᴇᴀᴛᴇᴅ ɪɴ: 01-12-2017\n"
                x+="☸️ Bᴏᴛ Cʀᴇᴀᴛᴏʀ: danrfq\n"
                x+="☸️ Bᴏᴛ Oᴡɴᴇʀ: "+cl.getProfile().displayName+"\n"
                x+="☸️ Bᴏᴛ Tʏᴘᴇ: Sᴇʟғʙᴏᴛ\n"
                x+="☸️ Vᴇʀsɪᴏɴ: 4.0\n"
                x+="╠═════════════════════\n"
                x+="「Cᴏɴᴛᴀᴄᴛ Pᴇʀsᴏɴᴀʟ」\n"
                x+="「 ▶️ ID LINE: line://ti/p/~danrfq 」\n\n"
                x+="Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞"
                cl.sendText(msg.to,x)
                msg.contentType = 13
                msg.contentMetadata = {'mid': admin}
                cl.sendMessage(msg)
#----------------ABOUT SECTION FINISH-----#
            elif msg.text in ["dih"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "15664369",
                                     "STKPKGID": "1405437",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
            elif "-_-" in msg.text:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "2754644",
                                     "STKPKGID": "1066653",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
            elif msg.text in ["madtah","Mastah"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "15664390",
                                     "STKPKGID": "1405437",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
            elif msg.text in ["wkwk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "153383",
                                     "STKPKGID": "2000006",
                                     "STKVER": "1" }
                cl.sendMessage(msg)
            elif msg.text in [":3"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "206271",
                                     "STKPKGID": "1003601",
                                     "STKVER": "2" }
                cl.sendMessage(msg)
            elif "kacang" in msg.text:
            	cl.sendImageWithURL(msg.to,"https://cdn.pixabay.com/photo/2010/12/13/09/51/peanut-1750_960_720.jpg")
            elif msg.text in [wait["gift"],"Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '3b92ccf5-54d3-4765-848f-c9ffdc1da020',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif "Set gift: " in msg.text:
                wait["gift"] = msg.text.replace("Set gift: ","")
                cl.sendText(msg.to,"Gift Key Berhasil Diubah Menjadi : 「"+wait["gift"]+"」")
#--------------------------------------------------------
            elif msg.text in ["cancel","Cancel"]:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                        cl.sendText(msg.to,"Sukses Mengancel Undangan")
                    else:
                        cl.sendText(msg.to,"No one is inviting")
                else:
                    cl.sendText(msg.to,"Can not be used outside the group")
                    
            elif msg.text in ["Mangat","B","tes apk no limit"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
#----------------------------------------------
                
            elif msg.text.lower() == wait["runtime"]:
                eltime = time.time() - mulai
                dan = "「Waktu Keaktifan Bot」\n"+waktu(eltime)
                cl.sendText(msg.to,dan)
            elif "Set runtime: " in msg.text:
                wait["runtime"] = msg.text.replace("Set runtime: ","")
                cl.sendText(msg.to,"Runtime Key Berhasil Diubah Menjadi : 「"+wait["runtime"]+"」")
            elif ":v" in msg.text:
                url = ("https://i.imgur.com/WbYWq38.jpg")
                urllib.urlretrieve(url, "gambar.png")
                cl.sendImage(msg.to, "gambar.png")
            elif "hmm" in msg.text:
            	url = ("https://ih1.redbubble.net/image.414126097.7189/flat,800x800,070,f.u1.jpg")
                urllib.urlretrieve(url, "gambar.png")
                cl.sendImage(msg.to, "gambar.png")
            elif msg.text in ["hilih","halah"]:
            	url = ("https://s14.postimg.org/e89u8gpo1/1514433298070.jpg")
                say = ("Hilih kinthil")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasyl.mp3")
                cl.sendImageWithURL(msg.to,url)
                cl.sendAudio(msg.to,"hasyl.mp3")
            elif msg.text in ["brisik","Berisik","Brisik","berisik","berisik asw"]:
            	vn = ("LINE_A20171229_005634157.m4a")
                cl.sendAudio(vn)
            elif "/gCall" in msg.text:
            	group = cl.getGroup(msg.to)
                cl.createGroupCall(msg.to)
            elif msg.text.lower() == 'spam gift':
              if msg.from_ in admin:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
                cl.sendMessage(msg)
             
#==================================================
            elif msg.text in ["Conban","Contactban","conban"]:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    cl.sendText(msg.to,"Daftar Kontak Penjahat")
                    h = ""
                    for i in wait["blacklist"]:
                        h = cl.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        cl.sendMessage(M)
#==================================================================
            elif "Steal name " in msg.text:
                    mention = eval(msg.contentMetadata["MENTION"])
                    mention1 = mention["MENTIONEES"][0]["M"]
                    contact = cl.getContact(mention1)
                    try:
                        cl.sendText(msg.to, "[ Display Name ]\n" + contact.displayName)
                    except:
                        pass
            elif "Steal bio " in msg.text:
                    mention = eval(msg.contentMetadata["MENTION"])
                    mention1 = mention["MENTIONEES"][0]["M"]
                    contact = cl.getContact(mention1)
                    try:
                        cl.sendText(msg.to, "[ Status Message ]\n" + contact.statusMessage)
                    except:
                        pass
#==================================================================
            elif msg.text.lower() == wait["tagall"]:
                     group = cl.getGroup(msg.to)
                     nama = [contact.mid for contact in group.members]
                     nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                     if jml <= 100:
                        summon(msg.to, nama)
                     if jml > 100 and jml < 200:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, len(nama)-1):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                     if jml > 200  and jml < 500:
                        for i in range(0, 99):
                            nm1 += [nama[i]]
                        summon(msg.to, nm1)
                        for j in range(100, 199):
                            nm2 += [nama[j]]
                        summon(msg.to, nm2)
                        for k in range(200, 299):
                            nm3 += [nama[k]]
                        summon(msg.to, nm3)
                        for l in range(300, 399):
                            nm4 += [nama[l]]
                        summon(msg.to, nm4)
                        for m in range(400, len(nama)-1):
                            nm5 += [nama[m]]
                        summon(msg.to, nm5)
                     if jml > 500:
                         print "Terlalu Banyak. Member 500+"
                     cnt = Message()
                     cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                     cnt.to = msg.to
                     cl.sendMessage(cnt)           
            elif "Set tagall: " in msg.text:
                wait["tagall"] = msg.text.replace("Set tagall: ","")
                cl.sendText(msg.to,"TagAll Key Berhasil Diubah Menjadi : 「"+wait["tagall"]+"」")
#===========================================     
            elif "TL: " in msg.text:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"Post URLnya\nline://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif ".ss " in msg.text:
                     website = msg.text.replace(".ss ","")
                     response = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link="+website+"")
                     data = response.json()
                     pictweb = data['result']
                     cl.sendImageWithURL(msg.to,pictweb)
            elif ".is " in msg.text:
                instagram = msg.text.replace(".is ","")
                response = requests.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link=www.instagram.com/"+instagram+"")
                data = response.json()
                pictig = data['result']
                cl.sendImageWithURL(msg.to,pictig)
            elif "Steal contact" in msg.text:
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = cl.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                cl.sendMessage(msg)
                
            elif "Steal contact: " in msg.text:
                mmid = msg.text.replace("Steal contact: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)

            elif msg.text in ["Tag on"]:
                if wait["tag"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"turned to on")
                else:
                    wait["tag"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned to on")
                    else:
                        cl.sendText(msg.to,"already on")
                        
            elif msg.text in ["Tag off"]:
                if wait["tag"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"turned to off")
                else:
                    wait["tag"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"turned to off")
                    else:
                        cl.sendText(msg.to,"already off")
    
            elif "Allbio: " in msg.text:
                string = msg.text.replace("Allbio: ","")
                if len(string.decode('utf-8')) <= 50000:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)

            elif "cium " in msg.text:
                korban = msg.text.replace("cium ","")
                korban2 = korban.split()
                midd = korban2[0]
                jumlah = int(korban2[1])
                if jumlah <= 1000:
                    for var in range(0,jumlah):
                        cl.sendText(midd,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                else:
                    cl.sendText(msg.to, "Kebanyakan gblk! ")
                print "T E R S P A M"
                
            elif "Spam grup " in msg.text:
              if msg.from_ in admin:
                korban = msg.text.replace("Spam grup ","")
                korban2 = korban.split()
                midd = korban2[0]
                jumlah = int(korban2[1])
                if jumlah <= 500:
                    for var in range(0,jumlah):
                            cl.findAndAddContactsByMid(midd)
                            cl.createGroup(wait["spamgrup"],[midd])
                            cl.inviteIntoGroup(msg.to,[midd])
                            cl.sendText(msg.to,"Sukses Spamming Grup!\nTarget: "+cl.getContact(midd).displayName+"\nJumlah Grup Yang Di Spam: "+jumlah)
                else:
                    cl.sendText(msg.to, "Kebanyakan gblk! ")            
                print "T E R S P A M."
            elif "Set nama spamgrup: " in msg.text:
                wait["spamgrup"] = msg.text.replace("Set nama spamgrup: ","")
                cl.sendText(msg.to,"Nama SpamGrup Berhasil Diubah Menjadi : 「"+wait["spamgrup"]+"」")
            elif "Add: " in msg.text:
                target = msg.text.replace("Add: ","")
                cl.findAndAddContactsByMid(target)
                cl.sendText(msg.to, "Sukses Add " +cl.getContact(target).displayName+ ". ")
                msg.contentType = 13
                msg.contentMetadata = {"mid": target}
                cl.sendMessage(msg)
                print "Add user"
#--------------------------------------------------------
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sudah On")
                    else:
                        cl.sendText(msg.to,"It is already open")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already open 👈")
                    else:
                        cl.sendText(msg.to,"It is already open 􀜁􀇔􏿿")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"sudah off ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"It is already off ô€œ��ô€„‰👈")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"off ô€œô€„‰already")
                    else:
                        cl.sendText(msg.to,"already Close ô€œô€„‰👈")
            elif "Tban " in msg.text:
                cmd = msg.text.replace("Tban ","")
                if cmd == "on":
                    if tban["status"] == False:
                        tban["status"] = True
                        cl.sendText(msg.to,"Talkban on")
                    else:
                        cl.sendText(msg.to,"Talkban already on")
                elif cmd == "off":
                    if tban["status"] == True:
                        tban["status"] = False
                        cl.sendText(msg.to,"Talkban off")
                    else:
                        cl.sendText(msg.to,"Talkban already off")
            elif ("Tbanadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        tban["target"][target] = True
                        cl.sendText(msg.to,"「Target Saving To List」")
                        break
                    except:
                        cl.sendText(msg.to,"「Failed」")
                        break
                    
            elif ("Tbandel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del tban["target"][target]
                        cl.sendText(msg.to,"「Target Delete From List」")
                        break
                    except:
                        cl.sendText(msg.to,"「Gagal Menghapus Target」")
                        break
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'qrprotect on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔��👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'inviteprotect on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨����👈")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'cancelprotect on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text.lower() == 'auto join on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka ô€¨👈")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already ON􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already On ô€¨")
            elif msg.text in ["Allprotect on","Panick:on"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect invite on 􀜁􀇔􏿿")
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect cancel on 􀜁􀇔􏿿")
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Already on")
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah on 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already on")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR on 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Already on")
            elif msg.text in ["Allprotect off","Panick:off"]:
              if msg.from_ in admin:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect invite off 􀜁􀇔􏿿")
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect cancel off 􀜁􀇔􏿿")
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Already off")
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Ini sudah off 􀜁􀇔􏿿👈")
                    else:
                        cl.sendText(msg.to,"Already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR off 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Already off")
            elif msg.text.lower() == 'auto join off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Auto Join Already Off")
                    else:
                        cl.sendText(msg.to,"Auto Join set off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif "Pictlock on" in msg.text:
              if msg.from_ in admin:
                if msg.to in wait['ppict']:
                    cl.sendText(msg.to,"ƬƲƦƝЄƊ ƠƝ.")
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                    wait['ppict'][msg.to] = True
                    wait['pro_pict'][msg.to] = cl.getGroup(msg.to).name
            elif "Pictlock off" in msg.text:
              if msg.from_ in admin:
                if msg.to in wait['ppict']:
                    cl.sendText(msg.to,"ƬƲƦƝ ƠƑƑ.")
                    del wait['ppict'][msg.to]
                else:
                    cl.sendText(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
            elif msg.text in ["Protect off"]:
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Qrprotect off","qrprotect off"]:
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Inviteprotect off","inviteprotect off"]:
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Cancelprotect off","cancelprotect off"]:
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"hall ini sudah off ô€œ👈")
                    else:
                        cl.sendText(msg.to,"sudah dimatikan ô€œô€„‰👈")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already close")
                    else:
                        cl.sendText(msg.to,"It is already open ô€œ👈")
            elif msg.text in ["Simisimi on","Simisimi:on"]:
                settings["simiSimi"][msg.to] = True
                cl.sendText(msg.to,"「Success activated simisimi」")
                
            elif msg.text in ["Simisimi off","Simisimi:off"]:
                settings["simiSimi"][msg.to] = False
                cl.sendText(msg.to,"「Success deactive simisimi」")
            elif "Group cancel: " in msg.text:
                try:
                    strnum = msg.text.replace("Group cancel: ","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Itu off undangan ditolak👈\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan👈")
                        else:
                            cl.sendText(msg.to,"Off undangan ditolak👈Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis👈")
                        else:
                            cl.sendText(msg.to,strnum + "The team declined to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        kk.sendText(msg.to,"Nilai tidak benar👈")
                    else:
                        cl.sendText(msg.to,"Weird value🛡")
            elif msg.text in ["Leave on","Auto leave: on"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah terbuka 􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already open👈􀜁􀇔􏿿")
            elif msg.text in ["Leave off","Auto leave: off"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah off👈􀜁􀇔􏿿")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Is already close👈??􀇔􏿿")
            elif msg.text in ["TagBan on","Tagban on"]:
                if wait["TagBan"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"TagBan ON👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah ON 􀜁􀇔􏿿")
                else:
                    wait["TagBan"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"TagBan ON👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah ON👈􀜁􀇔􏿿")
            elif msg.text in ["TagBan off","Tagban off"]:
                if wait["TagBan"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"TagBan OFF👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah OFF👈􀜁􀇔􏿿")
                else:
                    wait["TagBan"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"TagBan OFF👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Sudah OFF👈􀜁􀇔􏿿")
            elif msg.text in ["Share on","share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done 􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah terbuka👈")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"on👈")
                    else:
                        cl.sendText(msg.to,"on👈")
            elif msg.text in ["Share off","share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done👈􀜁􀇔􏿿")
                    else:
                        cl.sendText(msg.to,"It is already turned off 􀜁􀇔􏿿👈")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"Off👈")
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        cl.sendText(msg.to,"「Target Saving To List」")
                        break
                    except:
                        cl.sendText(msg.to,"「Failed」")
                        break
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        cl.sendText(msg.to,"「Target Delete From List」")
                        break
                    except:
                        cl.sendText(msg.to,"「Gagal Menghapus Target」")
                        break
                    
            elif msg.text in ["Miclist"]:
                        if mimic["target"] == {}:
                            cl.sendText(msg.to,"「No Target」")
                        else:
                            mc = "Target Mimic User\n"
                            for mi_d in mimic["target"]:
                                mc += "• "+cl.getContact(mi_d).displayName + "\n"
                            cl.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                cl.sendText(msg.to,"Mimic Change To Me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                cl.sendText(msg.to,"Mimic Change To Target")
                            else:
                                cl.sendText(msg.to,"「Not Target」")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        cl.sendText(msg.to,"「Reply Message on」")
                    else:
                        cl.sendText(msg.to,"「Turned on」")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        cl.sendText(msg.to,"「Reply Message off」")
                    else:
                        cl.sendText(msg.to,"「Turned off」")
            elif "Tagvn " in msg.text:
                cmd = msg.text.replace("Tagvn ","")
                if cmd == "on":
                    if wait["tagVN"] == False:
                        wait["tagVN"] = True
                        cl.sendText(msg.to,"「Tag VN on」")
                    else:
                        cl.sendText(msg.to,"「Turned on」")
                elif cmd == "off":
                    if wait["tagVN"] == True:
                        wait["tagVN"] = False
                        cl.sendText(msg.to,"「Tag VN off」")
                    else:
                        cl.sendText(msg.to,"「Turned off」")
            elif "Removechat " in msg.text:
                cmd = msg.text.replace("Removechat ","")
                if cmd == "on":
                    if wait["removeChat"] == False:
                        wait["removeChat"] = True
                        cl.sendText(msg.to,"「Remove Chat on」")
                    else:
                        cl.sendText(msg.to,"「Turned on」")
                elif cmd == "off":
                    if wait["removeChat"] == True:
                        wait["removeChat"] = False
                        cl.sendText(msg.to,"「Remove Chat off」")
                    else:
                        cl.sendText(msg.to,"「Turned off」")
            elif msg.text.lower() == wait["settings"]:
                set = ""
                if wait["contact"] == True: set+="Dᴀғᴛᴀʀ Sᴇᴛᴛɪɴɢ\n\n▩ Cᴏɴᴛᴀᴄᴛ → ☻\n"
                else: set+="Dᴀғᴛᴀʀ Sᴇᴛᴛɪɴɢ\n\n▩ Cᴏɴᴛᴀᴄᴛ → ☹\n"
                if wait["autoJoin"] == True: set+="▩ Aᴜᴛᴏ ᴊᴏɪɴ → ☻\n"
                else: set+="▩ Aᴜᴛᴏ ᴊᴏɪɴ → ☹\n"
                if wait["autoCancel"]["on"] == True:set+="▩ ᴀᴜᴛᴏ ᴄᴀɴᴄᴇʟ: " + str(wait["autoCancel"]["members"]) + " → ☻\n"
                else: set+="▩ ᴀᴜᴛᴏ ᴄᴀɴᴄᴇʟ → ☹\n"
                if wait["leaveRoom"] == True: set+="▩ Aᴜᴛᴏ ʟᴇᴀᴠᴇ → ☻\n"
                else: set+="▩ Aᴜᴛᴏ ʟᴇᴀᴠᴇ → ☹\n"
                if wait["alwaysRead"] == True: set+="▩ Aᴜᴛᴏ ʀᴇᴀᴅ → ☻\n"
                else: set+="▩ Aᴜᴛᴏ ʀᴇᴀᴅ → ☹\n"
                if wait["removeChat"] == True: set+="▩ Rᴇᴍᴏᴠᴇᴄʜᴀᴛ → ☻\n"
                else: set+="▩ Rᴇᴍᴏᴠᴇᴄʜᴀᴛ → ☹\n"
                if wait["timeline"] == True: set+="▩ Sʜᴀʀᴇ → ☻\n"
                else:set+="▩ Sʜᴀʀᴇ → ☹\n"
                if wait["autoAdd"] == True: set+="▩ Aᴅᴅᴍsɢ → ☻\n"
                else:set+="▩ Aᴅᴅᴍsɢ → ☹\n"
                if wait["commentOn"] == True: set+="▩ Aᴜᴛᴏ ᴄᴏᴍᴍᴇɴᴛ→ ☻\n"
                else:set+="▩ Aᴜᴛᴏ ᴄᴏᴍᴍᴇɴᴛ → ☹\n"
                if wait["protect"] == True: set+="▩ Pʀᴏᴛᴇᴄᴛ → ☻\n"
                else:set+="▩ Pʀᴏᴛᴇᴄᴛ → ☹\n"
                if wait["linkprotect"] == True: set+="▩ ǫʀᴘʀᴏᴛᴇᴄᴛ → ☻\n"
                else:set+="▩ ǫʀᴘʀᴏᴛᴇᴄᴛ → ☹\n"
                if wait["inviteprotect"] == True: set+="▩ Iɴᴠɪᴛᴇᴘʀᴏᴛᴇᴄᴛ → ☻\n"
                else:set+="▩ Iɴᴠɪᴛᴇᴘʀᴏᴛᴇᴄᴛ → ☹\n"
                if wait["cancelprotect"] == True: set+="▩ Cᴀɴᴄᴇʟᴘʀᴏᴛᴇᴄᴛ → ☻\n"
                else:set+="▩ Cᴀɴᴄᴇʟᴘʀᴏᴛᴇᴄᴛ → ☹\n"
                if wait["welcomemsg"] == True: set+="▩ Wᴇʟᴄᴏᴍᴇᴍsɢ→ ☻\n"
                else:set+="▩ Wᴇʟᴄᴏᴍᴇᴍsɢ → ☹\n"
                if wait["autoLike"] == True: set+="▩ Aᴜᴛᴏ ʟɪᴋᴇ → ☻\n"
                else:set+="▩ Aᴜᴛᴏ Lɪᴋᴇ → ☹\n" 
                if wait["Sider"] == True: set+="▩ Cᴇᴋ sɪᴅᴇʀ → ☻\n"
                else:set+="▩ Cᴇᴋ sɪᴅᴇʀ → ☹\n" 
                if settings["simiSimi"] == True: set+="▩ Sɪᴍɪsɪᴍɪ → ☻\n"
                else:set+="▩ Sɪᴍɪsɪᴍɪ → ☹\n"
                if wait['sticker'] == True: set+="▩ Sᴛɪᴄᴋᴇʀ → ☻\n"
                else:set+="▩ Sᴛɪᴄᴋᴇʀ → ☹\n"
                if mimic["status"] == True: set+="▩ Mɪᴍɪᴄ → ☻\n"
                else:set+="▩ Mɪᴍɪᴄ → ☹\n" 
                if wait["detectAll"] == True: set+="▩ Dᴇᴛᴇᴄᴛᴀʟʟ → ☻\n"
                else:set+="▩ Dᴇᴛᴇᴄᴛᴀʟʟ → ☹\n"
                if tban["status"] == True: set+="▩ Tᴀʟᴋʙᴀɴ → ☻\n"
                else:set+="▩ Tᴀʟᴋʙᴀɴ → ☹\n" 
                if wait["TagBan"] == True: set+="▩ TᴀɢBᴀɴ → ☻\n"
                else:set+="▩ TᴀɢBᴀɴ → ☹\n" 
                if wait["tagfoto"] == True: set+="▩ Tᴀɢғᴏᴛᴏ → ☻\n" 
                else:set+="▩ Tᴀɢғᴏᴛᴏ → ☹\n" 
                if wait["tagVN"] == True: set+="▩ TᴀɢVN → ☻\n"
                else:set+="▩ TᴀɢVN → ☹\n"
                if wait["tag"] == True: set+="▩ Tᴀɢ → ☻" 
                else:set+="▩ Tᴀɢ → ☹" 
                cl.sendText(msg.to,set+"\n\nPᴏᴡᴇʀᴇᴅ ʙʏ:\nᎢ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞")
                #cl.sendText(msg.to,"ɪᴅ ʟɪɴᴇ: line://ti/p/~danrfq\n\nʙɪʟᴀ ᴀᴅᴀ ᴘᴇʀʟᴜ ᴘᴄ ᴋᴏɴᴛᴀᴋ ᴅɪʙᴀᴡᴀʜ 😁")
                msg.contentType = 13
                msg.contentMetadata = {'mid': admin}
                #cl.sendMessage(msg)
            elif "Set settings: " in msg.text:
                wait["settings"] = msg.text.replace("Set settings: ","")
                cl.sendText(msg.to,"Settings Key Berhasil Diubah Menjadi : 「"+wait["settings"]+"」")
            elif msg.text in ["Like on"]:
                if wait["autoLike"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["autoLike"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["いいね:オフ","Like off"]:
                if wait["autoLike"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Done。")
                else:
                    wait["autoLike"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already。")
            elif msg.text in ["Auto read on","auto read on","Read on","read on"]:
                wait["alwaysRead"] = True
                cl.sendText(msg.to,"「Auto Sider ON」")
            elif msg.text in ["Auto read off","auto read off","Read off","read off"]:
                wait["alwaysRead"] = False
                cl.sendText(msg.to,"「Auto Sider OFF」")
            elif msg.text in ["Detectall on","detectall on"]:
                wait["detectAll"] = True
                cl.sendText(msg.to,"「 Detect All ON」")
            elif msg.text in ["Detectall off","detectall off"]:
                wait["detectAll"] = False
                cl.sendText(msg.to,"「Detect All OFF」")
            elif msg.text in ["Tagfoto on","tagfoto on"]:
                wait["tagfoto"] = True
                cl.sendText(msg.to,"「 Tag Foto ON」")
            elif msg.text in ["Tagfoto off","tagfoto off"]:
                wait["tagfoto"] = False
                cl.sendText(msg.to,"「Tag Foto OFF」")
            elif msg.text.lower() in ['sticker:on','detectsticker:on','sticker on']:
              if msg.from_ in admin:
                if wait['sticker'] == True:
                    cl.sendText(msg.to, "Sticker id detect already ON.")
                else:
                    wait['sticker']=True
                    cl.sendText(msg.to, "Sticker id detect turned ON.")
            elif msg.text.lower() in ['sticker:off','detectsticker:off','sticker off']:
              if msg.from_ in admina:
                if wait['sticker'] == False:
                    cl.sendText(msg.to, "Sticker id detect already OFF.")
                else:
                    wait['sticker']=False
                    cl.sendText(msg.to, "Sticker id detect turned OFF.")
            elif msg.text in ["Welcomemsg on"]:
               if msg.from_ in admin:
                if wait["welcomemsg"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Turned To ON\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Turned To ON\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Turned To ON\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"Already ON")
            elif msg.text in ["Welcomemsg off"]:
              if msg.from_ in admin:
                if wait["welcomemsg"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                else:
                    wait["welcomemsg"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
                    else:
                        cl.sendText(msg.to,"welcome message off\n\n"+ datetime.today().strftime('%H:%M:%S'))
            elif msg.text in ["Addmsg on","Add auto on"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On")
                    else:
                        cl.sendText(msg.to,"Already On??")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already On👈")
                    else:
                        cl.sendText(msg.to,"Already On👈")
            elif msg.text in ["Addmsg off","Add auto off"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini sudah off👈")
                    else:
                        cl.sendText(msg.to,"Hal ini sudah dimatikan👈")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Already Off👈")
                    else:
                        cl.sendText(msg.to,"Untuk mengaktifkan-off👈")
            elif "Message set: " in msg.text:
                wait["message"] = msg.text.replace("Message set: ","")
                cl.sendText(msg.to,"We changed the message👈")
            elif "Pesan add: " in msg.text:
                wait["message"] = msg.text.replace("Pesan add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Pesan Telah Ditambahkan👇")
                else:
                    cl.sendText(msg.to,"Change information")
            elif msg.text in ["Pesan add cek","Message Confirmation"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"Pesan Auto Add Saat ini Adalah Sebagai Berikut👇 \n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif msg.text in ["Change","change"]:
                if wait["lang"] =="JP":
                    wait["lang"] = "TW"
                    cl.sendText(msg.to,"I changed the language to engglis👈")
                else:
                    wait["lang"] = "JP"
                    cl.sendText(msg.to,"I changed the language to indonesia👈")
            elif "Message set: " in msg.text:
                c = msg.text.replace("Message set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Is a string that can not be changed👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"This has been changed👈\n\n" + c)
            elif "Comment set: " in msg.text:
                c = msg.text.replace("Comment set: ","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"Merupakan string yang tidak bisa diubah👈")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"Ini telah diubah👈\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Aku berada di👈")
                    else:
                        cl.sendText(msg.to,"To open👈")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It is already turned on")
                    else:
                        cl.sendText(msg.to,"è¦äº†å¼€👈")
            elif msg.text in ["Flist"]:
				if msg.from_ in admin:
					if wait["teman"] == {}:
						cl.sendText(msg.to,"nothing")
					else:
						cl.sendText(msg.to,"Daftar teman teman ku ada dibawah ini")
						mc = ""
						for mi_d in wait["teman"]:
							mc += "->" +cl.getContact(mi_d).displayName + "\n"
						cl.sendText(msg.to,mc)
            elif msg.text in ["Com off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It is already turned off")
                    else:
                        cl.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Off👈")
                    else:
                        cl.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                cl.sendText(msg.to,"Auto Comment saat ini telah ditetapkan sebagai berikut:👈\n\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add to the banlist…”👈")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                cl.sendText(msg.to,"Please send contacts from the person you want to add from the banlist…”??")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"Nothing in the blacklistô€œ🛡")
                else:
                    cl.sendText(msg.to,"The following is a blacklistô€œ👈")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["clock"] == True:
                    cl.sendText(msg.to,"Jam already on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Jam set on")
            elif msg.text.lower() == 'jam off':
                if wait["clock"] == False:
                    cl.sendText(msg.to,"Jam already off")
                else:
                    wait["clock"] = False
                    cl.sendText(msg.to,"Jam set off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) > 30:
                    cl.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    cl.sendText(msg.to,"Nama Jam Berubah menjadi:" + n)
            elif msg.text.lower() == 'update':
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"“%H:%M”")
                    profile = cl.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Diperbarui")
                else:
                    cl.sendText(msg.to,"Silahkan Aktifkan Jam")
                    #BERBAHAYA START#
            elif "Woy @" in msg.text:
                _name = msg.text.replace("Woy @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(g.mid,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞ NIH CIKA~")
                       cl.sendText(msg.to,"Selesai Mengspam Akun Target")
                       #BERBAHAYA FINISH#

            elif msg.text == "ciduk":
                if msg.toType == 2:
                    cl.sendText(msg.to, "Mulai Menciduk Sider\nKetik 「intip」ntar gua intip Sidernya 😼\nBuat Yang liat Gausah Ketik intip\nPercuma, ga bakal muncul~\n\nPencidukan Dimulai Pada Tanggal dan Waktu:" + datetime.now().strftime('\n%Y/%m/%d %H:%M:%S'))
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait2
                        
            elif msg.text == "intip":
                if msg.toType == 2:
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "[PENGINTIPAN SIDER]\n---------------\nSider kntl:%s\n\n\n\nSider gblk:\n%s\n\n---------------\nDiintip pada Set Point terakhir pada:\n[%s]\n---------------\n\nJangan Sider Mulu Anjing~ \n\n[🐿️]➦Powered By: Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞\n\n•┅─────" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                        print "ReadPoint Set..."
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print wait
                        cl.sendText(msg.to, "Pengintipan Pada Tanggal dan Waktu:" + datetime.now().strftime('\n%Y-%m-%d %H:%M:%S'))
                    else:
                        cl.sendText(msg.to, "LO AJA BELOM KETIK CIDUK!")
                        
            elif "lurk on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to," 「Lurking already on」")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "「Set Reading Sider System」\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2
            elif "lurk off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to," 「Lurking Already off」")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "「Delete reading point」\n" + datetime.now().strftime('%H:%M:%S'))
            elif "lurkers" in msg.text:
                    if msg.to in wait2['readPoint']:
                        if wait2['ROM'][msg.to].items() == []:
                             cl.sendText(msg.to, "Lurkers:\nNone")
                        else:
                            chiya = []
                            for rom in wait2['ROM'][msg.to].items():
                                chiya.append(rom[1])

                            cmem = cl.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
			    xpesan = '「Lurkers Groups」\n'
                            for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                            msg.contentType = 0

                            print zxc
                            msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                            lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                            print lol
                            msg.contentMetadata = lol
                            try:
                              cl.sendMessage(msg)
                            except Exception as error:
                                  print error
                            pass
                    else:
                        cl.sendText(msg.to, "「Lurking has not been set」")
            elif "Cek sider on" in msg.text:
                try:
                    del cctv['point'][msg.to]
                    del cctv['sidermem'][msg.to]
                    del cctv['cyduk'][msg.to]
                except:
                    pass
                cctv['point'][msg.to] = msg.id
                cctv['sidermem'][msg.to] = ""
                cctv['cyduk'][msg.to]=True
                wait["Sider"] = True
                cl.sendText(msg.to,"Siap On Cek Sider")
                
            elif "Cek sider off" in msg.text:
                if msg.to in cctv['point']:
                    cctv['cyduk'][msg.to]=False
                    wait["Sider"] = False
                    cl.sendText(msg.to, "Cek Sider Off")
                else:
                    cl.sendText(msg.to, "Heh Belom Di Set")
#---------------------KEDAPKEDIP SECTION-------------------#

            elif "kedapkedip " in msg.text.lower():
                txt = msg.text.replace("kedapkedip ","")
                t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                cl.sendText(msg.to, t1 + txt + t2)							

#----------------------ADMIN COMMAND------------------------------#

            elif ("tampol " in msg.text):
                if msg.from_ in admin:
                    targets = []
                    key = eval(msg.contentMetadata["MENTION"])
                    key["MENTIONEES"][0]["M"]
                    for x in key["MENTIONEES"]:
                        targets.append(x["M"])
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                        except:
                            cl.sendText(msg.to,"Error")
                            
            elif "Sapu" in msg.text:
                if msg.toType == 2:
                    print "Cleanse is going."
                    _name = msg.text.replace("Sapu ","")
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"This group must be destroyed!")
                    cl.sendText(msg.to,"sᴀʏ ɢᴏᴏᴅ ʙʏᴇ ᴛᴏ ᴍᴇ.")
                    cl.sendText(msg.to,"Fuck you.")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Not found.")
                        cl.sendText(msg.to,"Not found.")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                                cl.sendText(msg.to,"ɢʀᴏᴜᴘ sᴜᴅᴀʜ ᴅɪʙᴇʀsɪʜᴋᴀɴ")
                            except:
                                cl.sendText(msg,to,"Group cleanse")
                                cl.sendText(msg,to,"Group cleanse")
                    
#-------------Fungsi Tag All Start---------------#
            elif msg.text in ["hai"]:
                if msg.from_ in admin:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "「 @dan」 \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
#-------------Fungsi Tag All Finish---------------#
            elif msg.text in ["Glid"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsJoined()
                    h = "===[List Groups]==="
                    total = str(len(gid))
                    for i in gid:
                        if i is not None:
                            try:
                                groups = cl.getGroup(i)
                                if groups.members is not None:
                                    members = str(len(groups.members))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                h += "\n[" + groups.name + "] ->(" + members +")\n ✒️ GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,h + "\n|[Total Groups]| : " + str(total))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup saat ini")
                    ginv = cl.getGroupIdsInvited()
                    j = "===[List Groups Invited]==="
                    totals = str(len(ginv))
                    for z in ginv:
                        if z is not None:
                            try:
                                groups = cl.getGroup(z)
                                if groups.members is not None:
                                    members = str(len(groups.mem1bers))
                                else:
                                    members = "0"
                                if groups.invitee is not None:
                                    pendings = str(len(groups.invitee))
                                else:
                                    pendings = "0"
                                j += "\n[" + groups.name + "] ->(" + members + ")\n ✒️ GroupID : " + i
                            except:
                                break
                        else:
                            break
                    if ginv is not None:
                        cl.sendText(msg.to,j + "\n|[Total Groups Invited]| : " + str(totals))
                    else:
                        cl.sendText(msg.to,"Tidak ada grup tertunda saat ini")
                        
            elif "Info grup: " in msg.text:
                if msg.from_ in admin:
                    gid = msg.text.replace("Info grup: ","")
                    if gid in [""," "]:
                        cl.sendText(msg.to,"GID tidak valid")
                    else:
                        try:
                            groups = cl.getGroup(gid)
                            if groups.members is not None:
                                members = str(len(groups.members))
                            else:
                                members = "0"
                            if groups.invitee is not None:
                                pendings = str(len(groups.invitee))
                            else:
                                pendings = "0"
                            h = "[Nama Grup: " + groups.name + "]\n\n ✒️ GID : " + gid + "\n\n ✒️ Anggota : " + members + "\n\n ✒️ Anggota Pending : " + pendings + "\n\n ✒️ Pembuat Grup : " + groups.creator.displayName + "\n\n ✒️ Foto Grup : http://dl.profile.line.naver.jp/" + groups.pictureStatus
                            cl.sendText(msg.to,h)
                        except Exception as error:
                            cl.sendText(msg.to,(error))
                            
            elif msg.text.lower() == '.gid':
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
                
            elif msg.text in ["Tag me"]:
                            profile = cl.getProfile()
                            xname = profile.displayName
                            xlen = str(len(xname)+1)
                            msg.contentType = 0
                            msg.text = "@"+xname+" 👍"
                            msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mid)+'}]}','EMTVER':'4'}
                            cl.sendMessage(msg)

            elif "Cancel invite: " in msg.text:
                if msg.from_ in admin:
                    gids = msg.text.replace("Cancel invite: ","")
                    gid = cl.getGroup(gids)
                    for i in gid:
                        if i is not None:
                            try:
                                cl.rejectGroupInvitation(i)
                            except:
                                cl.sendText(msg.to,"Error!")
                                break
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil tolak undangan dari grup " + gid.name)
                    else:
                        cl.sendText(msg.to,"Grup tidak ditemukan")
            
            elif msg.text in ["Accept invite"]:
                if msg.from_ in admin:
                    gid = cl.getGroupIdsInvited()
                    _list = ""
                    for i in gid:
                        if i is not None:
                            gids = cl.getGroup(i)
                            _list += gids.name
                            cl.acceptGroupInvitation(i)
                        else:
                            break
                    if gid is not None:
                        cl.sendText(msg.to,"Berhasil terima semua undangan dari grup :\n" + _list)
                    else:
                        cl.sendText(msg.to,"Tidak ada grup yang tertunda saat ini")
            
            elif "Myname " in msg.text:
                string = msg.text.replace("Myname ","")
                if len(string.decode('utf-8')) <= 200000:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Nama Telah Diubah Menjadi 「" + string + "」")

            elif "Mybio " in msg.text:
                string = msg.text.replace("Mybio ","")
                if len(string.decode('utf-8')) <= 500000:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"Bio Telah Diubah Menjadi 「" + string + "」")
                    
            elif "tgb" in msg.text:
            	cl.sendText(msg.to,"Ꭲ̡̦͎͇͈̘̻̎̉̅́̒͗ͅϵѧᴍ̸̩̟̗͎̯͙̺̺̜̬̙̟̀̑̓͋̐͆͌̓̒́̒͗͒͑̚͟͜ᎶʀҽѧᴛᏴøᴛ̢͓̹̗̘̠̪̖͗̃̄̅̆̽̀̕͜͞")
            elif "Foto" in msg.text:
                linkfoto = msg.text.replace("Foto ","")
                cl.sendImageWithURL(msg.to, linkfoto)
            elif "Vn" in msg.text:
                linkvn = msg.text.replace("Vn ","")
                cl.sendAudioWithURL(msg.to, linkvn)
            elif "Video" in msg.text:
                 linkvid = msg.text.replace("Video ","")
                 cl.sendVideoWithURL(msg.to, linkvid)
            elif ("Gn " in msg.text):
              if msg.from_ in admin:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                    cl.sendText(msg.to,"Sukses mengganti nama grup menjadi "+X.name+"~")
                else:
                    pass
                    
            elif msg.text == "Steal gn":
                    group = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"「"+group.name+"」")
                    
            elif "gid" in msg.text:
                    cl.sendText(msg.to, msg.to)
                    
            elif "Mypict" in msg.text:
                    me = cl.getContact(mid)
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + me.pictureStatus)
            elif "Mycover" in msg.text:
                    me = cl.getContact(mid)
                    cover = cl.channel.getCover(mid)          
                    path = str(cover)
                    cl.sendImageWithURL(msg.to, path)
#-------------------------------------------------
            elif msg.text in ["today"]:
	    	      wait2['setTime'][msg.to] = datetime.today().strftime('Date : %Y-%m-%d \nDay : %A \nTime : %H:%M:%S')
	              cl.sendText(msg.to, "「Kalender」\n\n" + (wait2['setTime'][msg.to]))
#-----------------------------------------------

            elif "tampol: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("tampol: ","")
                cl.kickoutFromGroup(msg.to,[midd])
                
            elif "Invite: " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite: ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])

            elif "C @" in msg.text:
                if msg.toType == 2:
                    if msg.from_ in admin:
                        print "[COPY] Ok"
                        _name = msg.text.replace("C @","")
                        _nametarget = _name.rstrip('  ')
                        gs = cl.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to, "Not Found...")
                        else:
                            for target in targets:
                                try:
                                    cl.cloneContactProfile(target)
                                    cl.sendText(msg.to, "Sukses Copy Profilenya "+_name+"~")
                                    msg.contentType = 13
                                    msg.contentMetadata = {'mid': admin}
                                    cl.sendMessage(msg)
                                except Exception as e:
                                    print e
                                    
    #==============================================================================#
                #               T E X T     T O     S P E E C H             #
                
            elif "say-" in msg.text.lower():
                    sep = msg.text.split("-")
                    sep = sep[1].split(" ")
                    lang = sep[0]
                    say = msg.text.lower().replace("say-" + lang + " ","")
                    tts = gTTS(text=say, lang=lang)
                    tts.save("hasill.mp3")
                    cl.sendAudio(msg.to, "hasill.mp3")
    #==============================================================================#
            #                   T R A N S L A T E                   #
            elif ".tr-" in msg.text.lower():
                    sep = msg.text.split("-")
                    sep = sep[1].split(" ")
                    lang = sep[0]
                    text_ = msg.text.lower().replace(".tr-" + lang + " ","")
                    translator = Translator()
                    hasil = translator.translate(text_, dest=lang)
                    hasil = hasil.text.encode('utf-8')
                    cl.sendText(msg.to, str(hasil))
    #==============================================================================#
            elif "Meme: " in msg.text:  
                code = msg.text.split(" ")
                txt = msg.text.replace(code[0] + "/" + " ","")
                txt2 = msg.text.replace(txt[0] + "/" + " ","")
                naena = "https://memegen.link/"+txt2+".jpg"
                try:
                    cl.sendImageWithURL(msg.to, naena)
                except Exception as error:
                    cl.sendText(msg.to, str(error))
            elif "gblk" in msg.text:
                x = ("goblok lo asu")
                lang = 'id'
                tts = gTTS(text=x, lang=lang)
                tts.save("x.mp3")
                cl.sendAudio(msg.to,"x.mp3")
            elif "kerad" in msg.text:
                kerad = ("kerad juga kamu ea","kerad sangad kamu bangsad","alamak, kerad juga kamu ea")
                asu = random.choice(kerad)
                lang = 'id'
                tts = gTTS(text=asu, lang=lang)
                tts.save("krd.mp3")
                cl.sendAudio(msg.to,"krd.mp3")
            elif "Meme: " in msg.text:  
                code = msg.text.split(" ")
                txt = msg.text.replace(code[0] + "/" + " ","")
                txt2 = msg.text.replace(txt[0] + "/" + " ","")
                naena = "https://memegen.link/"+txt2+".jpg"
                try:
                    cl.sendImageWithURL(msg.to, naena)
                except Exception as error:
                    cl.sendText(msg.to, str(error))
            elif ".id " in msg.text:
                 msgg = msg.text.replace('.id ','')
                 conn = cl.findContactsByUserid(msgg)
                 if False:
                 	cl.sendText(msg.to,"Gaada ID kayak gitu anjeng!")
                 if True:
                     msg.contentType = 13
                     msg.contentMetadata = {'mid': conn.mid}
                     cl.sendText(msg.to,"[ Nama Profil ]\n"+conn.displayName+"\n\n[ Status Profil ]\n"+conn.statusMessage+"\n\n[ Mid Profil ]\n"+conn.mid+"\n\n[ URL Foto Profil ]\nhttp://dl.profile.line-cdn.net/"+conn.pictureStatus+"\n\nKepoin lebih lanjut?\nKlik line://ti/p/~"+msgg)
                     cl.sendMessage(msg)
            elif msg.text in ["Backup"]:
                try:
                    cl.updateDisplayPicture(mybackup.pictureStatus)
                    cl.updateProfile(mybackup)
                    cl.sendText(msg.to, "Sukses Backup Profile~")
                    msg.contentType = 13
                    msg.contentMetadata = {'mid': admin}
                    cl.sendMessage(msg)
                except Exception as e:
                    cl.sendText(msg.to, str (e))
            elif "Bc " in msg.text:
                bctxt = msg.text.replace("Bc ", "")
                a = cl.getGroupIdsJoined()
                b = cl.getAllContactIds()
                for manusia in a:
                    cl.sendText(manusia, "☢ ɮʀօǟɖċǟֆt ☢\n\n"+(bctxt)+"\n\n☢ ɮʀօǟɖċǟֆtɛɖ ɮʏ: "+cl.getProfile().displayName+" ☢")
                for orang in b:
                    cl.sendText(orang, "☢ ɮʀօǟɖċǟֆt ☢\n\n"+(bctxt)+"\n\n☢ ɮʀօǟɖċǟֆtɛɖ ɮʏ: "+cl.getProfile().displayName+" ☢")
                cl.sendText(msg.to,"Sukses membroadcast "+bctxt+" ke "+str(len(a))+" grup dan "+str(len(b))+" kontak!")
            elif "Bcc " in msg.text:
                bctxt = msg.text.replace("Bcc ", "")
                a = cl.getAllContactIds()
                for manusia in a:
                    cl.sendText(manusia, "☢ ɮʀօǟɖċǟֆt ☢\n\n"+(bctxt)+"\n\n☢ ɮʀօǟɖċǟֆtɛɖ ɮʏ: "+cl.getProfile().displayName+" ☢")
                cl.sendText(msg.to,"Sukses membroadcast "+bctxt+" ke "+str(len(a))+" teman!")
            elif "Bcg " in msg.text:
                bctxt = msg.text.replace("Bcg ", "")
                a = cl.getGroupIdsJoined()
                for manusia in a:
                    cl.sendText(manusia, "☢ ɮʀօǟɖċǟֆt ☢\n\n"+(bctxt)+"\n\n☢ ɮʀօǟɖċǟֆtɛɖ ɮʏ: "+cl.getProfile().displayName+" ☢")
                cl.sendText(msg.to,"Sukses membroadcast "+bctxt+" ke "+str(len(a))+" grup!")
            elif ".rc" in msg.text.lower():
                if msg.from_ in admin:
                    try:
                        cl.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        cl.sendText(msg.to,"Sukses Menghapus Chat")
                    except Exception as error:
                        print error
                        cl.sendText(msg.to,"Error Menghapus Chat")
                        
            elif msg.text.lower() == '.rs':
              if msg.from_ in admin:
                    print "[Command] RESTART BOT"
                    try:
                        cl.sendText(msg.to,"[√] яєѕтαят вσт ѕυкѕєѕ")
                        restart_program()
                    except:
                        cl.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
                        
            elif ".to" in msg.text:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass
#-----------------------------------------------
            elif msg.text in [".gc"]:
              if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                        
                    except:
                        gCreator = "Error"
                    cl.sendText(msg.to, "「Pembuat Grup」\n" + gCreator1)
                    cl.sendMessage(msg)
            elif msg.text in ["Inv:.gc"]:
	           if msg.from_ in admin:
                    ginfo = cl.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                       cl.findAndAddContactsByMid(gCreator)
                       cl.inviteIntoGroup(msg.to,[gCreator])
                       cl.sendText(msg.to,"Sukses menginvite pembuat grup\n▶"+ginfo.creator.displayName)
                       print "success inv gCreator"
                    except:
                       pass
#-----------------------------------------------
            elif "Spam " in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                #Vicky Kull~
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           cl.sendText(msg.to, teks)
                    else:
                       cl.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        cl.sendText(msg.to, tulisan)
                    else:
                        cl.sendText(msg.to, "Out Of Range!")
                        
            elif "Spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "+wait["sttext"]
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendMessage(msg)
                        cl.sendText(msg.to,"Berhasil spamtag 1 orang dengan total 20 tag!\nKorban spamtag: "+xname+"\nSpamtag text: "+wait["sttext"])
                    else:
                        pass
            elif "Spamtag pc @" in msg.text:
                _name = msg.text.replace("Spamtag pc @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xmid = g.mid
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "+wait["sttext"]
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        c = Message(to=xmid, from_=None, text=msg.text, contentType=0)
                        c.contentMetadata={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(msg.from_)+'}]}','EMTVER':'4'}
                        cl.sendText(xmid,"Sorry "+xname+" gua spamtag :v")
                        cl.sendMessage(c)
                        cl.sendMessage(c)
                        cl.sendMessage(c)
                        cl.sendMessage(c)
                        cl.sendMessage(c)
                        cl.sendMessage(c)
                        cl.sendMessage(c)
                        cl.sendMessage(c)
                        cl.sendMessage(c)
                        cl.sendMessage(c)
                        cl.sendMessage(c)
                        cl.sendMessage(c)
                        cl.sendMessage(c)
                        cl.sendMessage(c)
                        cl.sendMessage(c)
                        cl.sendMessage(c)
                        cl.sendMessage(c)
                        cl.sendMessage(c)
                        cl.sendText(msg.to,"Berhasil spamtag pc 1 orang dengan total 20 tag!\nKorban spamtag: "+xname+"\nSpamtag text: "+wait["sttext"])
                    else:
                        pass
            elif "Set spamtag text: " in msg.text:
                wait["sttext"] = msg.text.replace("Set spamtag text: ","")
                cl.sendText(msg.to,"Spamtag Text Key Berhasil Diubah Menjadi : 「"+wait["sttext"]+"」")
            elif "Set tag text: " in msg.text:
                wait["tagtext"] = msg.text.replace("Set tag text: ","")
                cl.sendText(msg.to,"Tag Text Key Berhasil Diubah Menjadi : 「"+wait["tagtext"]+"」")
            elif msg.text in ["Dan sp","dsp"]:
                print ("ADA YANG CEK SPEED NIH :3")
                start = time.time()
                cl.sendText(msg.to, "「 Debug Speed」\nSpeed on Progress♪")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "「 Debug Speed」\nSpeed is here♪\n%s seconds" % (elapsed_time))
            elif msg.text.lower() == wait["me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                cl.sendMessage(msg)
                profile = cl.getProfile()
                xname = profile.displayName
                xlen = str(len(xname)+1)
                msg.contentType = 0
                msg.text = "@"+xname+" :)"
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mid)+'}]}','EMTVER':'4'}
                cl.sendMessage(msg)
            elif "Set me: " in msg.text:
                wait["me"] = msg.text.replace("Set me: ","")
                cl.sendText(msg.to,"Me Key Berhasil Diubah Menjadi : 「"+wait["me"]+"」")
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'u577d79f51412f92e7a28d360ca351ae4'}
                cl.sendMessage(msg)
            elif wait["crash"] in msg.text:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "u577d79f51412f92e7a28d360ca351ae4','"}
                cl.sendMessage(msg)
            elif "Set crash: " in msg.text:
                wait["crash"] = msg.text.replace("Set crash: ","")
                cl.sendText(msg.to,"Crash Key Berhasil Diubah Menjadi : 「"+wait["crash"]+"」")
            elif "Crash @" in msg.text:
                _name = msg.text.replace("Crash @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                      c = Message(to=g, from_=None, text=None, contentType=13)
                      c.contentMetadata={'mid': "u577d79f51412f92e7a28d360ca351ae4','"}
                      cl.sendMessage(c)
            
#================================================
            elif "Inviteme: " in msg.text:
              if msg.from_ in admin:
                gid = msg.text.replace("Inviteme: ","")
                if gid == "":
                    cl.sendText(msg.to,"Invalid group id")
                else:
                    try:
                        cl.findAndAddContactsByMid(msg.from_)
                        cl.inviteIntoGroup(gid,[msg.from_])
                    except:
                        cl.sendText(msg.to,"Mungkin saya tidak di dalaam grup itu")
            elif msg.text in ["Outall"]:
              if msg.from_ in admin:
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    cl.leaveGroup(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"")
                else:
                    cl.sendText(msg.to,"He declined all invitations")

            elif "Ginfo" in msg.text:
                    group = cl.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Tidak ditemukan"
                    if group.invitee is None:
                        gPending = "0"
                    else:
                        gPending = str(len(group.invitee))
                    if group.preventJoinByTicket == True:
                        gQr = "Tertutup"
                        gTicket = "Tidak ada"
                    else:
                        gQr = "Terbuka"
                        gTicket = "https://line.me/R/ti/g/{}".format(str(cl.reissueGroupTicket(group.id)))
                    ret_ = "╔════════Grup Info═════════"
                    ret_ += "\n╠Nama Grup : {}".format(group.name)
                    ret_ += "\n╠ID Grup : {}".format(group.id)
                    ret_ += "\n╠Pembuat Grup : {}".format(gCreator)
                    ret_ += "\n╠Jumlah Member : {}".format(str(len(group.members)))
                    ret_ += "\n╠Jumlah Pending : {}".format(gPending)
                    ret_ += "\n╠Grup QR : {}".format(gQr)
                    ret_ += "\n╠Grup URL : {}".format(gTicket)
                    ret_ += "\n╚════════Grup Info═════════"
                    cl.sendText(msg.to, str(ret_))
                    cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
            elif msg.text == "Uni":
	            cl.sendText(msg.to,"JANGAN DI BUKA 😘\n\nHai Perkenalkan.....\nNama saya siapa ya?\n\n1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1.1\n\nMakasih Sudah Dilihat :)\nJangan Dikick ampun mzz :v")
#----------------SEARCH SECTION----------------------------------------
	    elif ".ms " in msg.text:
					songname = msg.text.replace(".ms ","")
					params = {"songname": songname}
					r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
					data = r.text
					data = json.loads(data)
					for song in data:
						abc = song[3].replace('https://','http://')
						cl.sendText(msg.to, "Title : " + song[0] + "\nLength : " + song[1] + "\nLink download : " + song[4])
						cl.sendText(msg.to, "Lagu " + song[0] + "\nSedang Di Prosses... Tunggu Sebentar ^_^ ")
						cl.sendAudioWithURL(msg.to,abc)
						cl.sendText(msg.to, "Selamat Mendengarkan Lagu " + song[0])
            elif ".lr" in msg.text.lower():
                    sep = msg.text.split(" ")
                    search = msg.text.replace(sep[0] + " ","")
                    params = {'songname': search}
                    with requests.session() as web:
                        web.headers["User-Agent"] = random.choice(wait["userAgent"])
                        r = web.get("https://ide.fdlrcn.com/workspace/yumi-apis/joox?" + urllib.urlencode(params))
                        try:
                            data = json.loads(r.text)
                            for song in data:
                                songs = song[5]
                                lyric = songs.replace('ti:','Title - ')
                                lyric = lyric.replace('ar:','Artist - ')
                                lyric = lyric.replace('al:','Album - ')
                                removeString = "[1234567890.:]"
                                for char in removeString:
                                    lyric = lyric.replace(char,'')
                                ret_ = "╔══[ Lyric ]"
                                ret_ += "\n╠ Nama lagu : {}".format(str(song[0]))
                                ret_ += "\n╠ Durasi : {}".format(str(song[1]))
                                ret_ += "\n╠ Link : {}".format(str(song[3]))
                                ret_ += "\n╚══[ Finish ]\n{}".format(str(lyric))
                                cl.sendText(msg.to, str(ret_))
                        except:
                            cl.sendText(to, "Lirik tidak ditemukan")
            elif ".yt " in msg.text:
                query = msg.text.replace(".yt ","")
                with requests.session() as s:
                    s.headers['user-agent'] = 'Mozilla/5.0'
                    url = 'http://www.youtube.com/results'
                    params = {'search_query': query}
                    r = s.get(url, params=params)
                    soup = BeautifulSoup(r.content, 'html5lib')
                    hasil = ""
                    for a in soup.select('.yt-lockup-title > a[title]'):
                        if '&list=' not in a['href']:
                            hasil += ''.join((a['title'],'\nhttp://www.youtube.com' + a['href'],'\n\n'))
                    cl.sendText(msg.to,hasil)
                    print '[Command] Youtube Search'
            elif 'Youtubemp4 ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('Youtubemp4 ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'class': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com/' + results['href'])
                        cl.sendVideoWithURL(msg.to, ght)
                    except:
                        cl.sendText(msg.to, "Could not find it")
            elif '.wp ' in msg.text.lower():
              if msg.from_ in admin:
                  try:
                      wiki = msg.text.lower().replace(".wp ","")
                      wikipedia.set_lang("id")
                      pesan="「 "
                      pesan+=wikipedia.page(wiki).title
                      pesan+=" 」\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n「 "
                      pesan+=wikipedia.page(wiki).url
                      pesan+=" 」"
                      cl.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Jumlah text kebanyakan~\nUntuk info lebih lanjut silahkan klik link dibawah ini.\n"
                              pesan+="「 "+wikipedia.page(wiki).url+" 」"
                              cl.sendText(msg.to, pesan)
                          except Exception as e:
                              cl.sendText(msg.to, str(e))
            elif ".ig " in msg.text:
                    try:
                        instagram = msg.text.replace(".ig ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBio : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        cl.sendImageWithURL(msg.to, profileIG)
                        cl.sendText(msg.to, str(text))
                    except Exception as e:
                        cl.sendText(msg.to, str(e))
            elif ".lc " in msg.text.lower():
                            pisah = msg.text.split("c ")
                            location = msg.text.replace(pisah[0]+"c ","")
                            params = {'lokasi':location}
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(wait["userAgent"])
                                r = requests.get("http://api.corrykalam.net/apiloc.php?"+ urllib.urlencode(params))
                                data = r.text
                                data = json.loads(data)
                                if data[0] != "" and data[1] != "" and data[2] != "":
                                    link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                    ret_ = "╔══『 Detail Location 』"
                                    ret_ += "\n╠ ⌬「 Lokasi」: " + data[0]
                                    ret_ += "\n╠ ⌬「 Google Maps 」: " + link
                                    ret_ += "\n╚══『 Detail Location 』"
                                else:
                                    ret_ = "[ Details Location ] Error : Location not found"
                                cl.sendText(msg.to, str(ret_))
            elif ".pt " in msg.text.lower():
                            pisah = msg.text.split("t ")
                            location = msg.text.replace(pisah[0]+"t ","")
                            params = {'lokasi':location}
                            with requests.session() as web:
                                r = requests.get("http://api.corrykalam.net/apisholat.php?" + urllib.urlencode(params))
                                data = r.text
                                data = json.loads(data)
                                if data[1] != "╠ ⌬「 Subuh」: " and data[2] != "╠ ⌬「 Dzuhur」: " and data[3] != "╠ ⌬「 Ashar」: " and data[4] != "╠ ⌬「 Maghrib」: " and data[5] != "╠ ⌬「 Isya」: ":
                                    ret_ = "╔══『 Jadwal Sholat 』"
                                    ret_ += "\n╠ ⌬「 Lokasi 」: " + data[0]
                                    ret_ += "\n" + data[1]
                                    ret_ += "\n" + data[2]
                                    ret_ += "\n" + data[3]
                                    ret_ += "\n" + data[4]
                                    ret_ += "\n" + data[5]
                                    ret_ +=  "\n╚══『 Jadwal Sholat 』"
                                else:
                                    ret_ = "[ Prayer Schedule ] Error : Location not found" 
                                cl.sendText(msg.to, str(ret_))
            elif msg.text.lower().startswith(".cw "):
                            sep = msg.text.split(" ")
                            location = msg.text.lower().replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(wait["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                if "result" not in data:
                                    ret_ = "╔══[ Weather Status ]"
                                    ret_ += "\n╠ Lokasi : " + data[0].replace("Temperatur di kota ","")
                                    ret_ += "\n╠ " + data[1]+"°C"
                                    ret_ += "\n╠ " + data[2] + "%"
                                    ret_ += "\n╠ " + data[3] + " milibar"
                                    ret_ += "\n╠ " + data[4] +"km/jam"
                                    ret_ += "\n╚══[ Complete ]"
                                else:
                                    ret_ = "[ Weather Status ] Error : Lokasi tidak ditemukan"
                                cl.sendText(msg.to, str(ret_))
            elif msg.text.lower().startswith("imagetext "):
                sep = msg.text.split(" ")
                textnya = msg.text.replace(sep[0] + " ","")
                urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                cl.sendImageWithURL(msg.to, urlnya)
            elif ".ps " in msg.text.lower():
                tob = msg.text.lower().replace(".ps ","")
                dan = urllib.quote(tob)
                cl.sendText(msg.to,"「 Searching 」\n" "Type: Play Store Search\nStatus: Processing...")
                cl.sendText(msg.to,"Title : "+tob+"\nhttps://play.google.com/store/search?q=" + dan)
                cl.sendText(msg.to,"「 Searching 」\n" "Type: Play Store Search\nStatus: Success")
            elif ".gl " in msg.text:
                    a = msg.text.replace(".gl ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type: Google Search\nStatus: Processing...")
                    cl.sendText(msg.to,"Title: " + a + "\nhttps://google.co.id/search?dcr=0&source=hp&ei=iysxWvH4JcbwvgSa5IqYDg&q=" + b + "&oq=" + b + "&gs_l=mobile-gws-hp.3..0i203k1l3j0j0i203k1.2672.5074.0.5502.18.11.2.5.6.0.190.1542.0j10.10.0....0...1c.1j4.64.mobile-gws-hp..3.15.1347.3..35i39k1j0i131k1j0i10i203k1j0i10k1.140.cERNZUVYbV8#scso=uid_WjEr7gABqeYKj7vFEw8Fug_7:228")
                    cl.sendText(msg.to,"「 Searching 」\n" "Type: Google Search\nStatus: Success")
            elif ".fb" in msg.text:
                    a = msg.text.replace(".fb","")
                    replace = urllib.quote(a)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type: Facebook Search\nStatus: Processing...")
                    cl.sendText(msg.to, "Title: " + a + "\nhttps://m.facebook.com/search/top/?q="+replace+"&ref=content_filter&tsid=0.7682944806717842&source=typeahead")
                    cl.sendText(msg.to,"「 Searching 」\n" "Type: Search Info\nStatus: Success")
            elif ".gt " in msg.text:
                    a = msg.text.replace(".gt ","")
                    b = urllib.quote(a)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type: GitHub Search\nStatus: Processing...")
                    cl.sendText(msg.to, "Title: " + a + "\nhttps://github.com/search?utf8=✓&q="+b)
                    cl.sendText(msg.to,"「 Searching 」\n" "Type: GitHub Search\nStatus: Success")
            elif ".gi" in msg.text.lower():
                    start = time.time()
                    separate = msg.text.split(" ")
                    search = msg.text.replace(separate[0] + " ","")
                    url = 'https://www.google.com/search?q=' + search.replace(" ","+") +  '&espv=2&biw=1366&bih=667&site=webhp&source=lnms&tbm=isch&sa=X&ei=XosDVaCXD8TasATItgE&ved=0CAcQ_AUoAg'
                    raw_html = (download_page(url))
                    items = []
                    items = items + (_images_get_all_items(raw_html))
                    path = random.choice(items)
                    cl.sendImageWithURL(msg.to,path)
                    a = items.index(path)
                    b = len(items)
                    elapsed_time = time.time() - start
                    cl.sendText(msg.to,"Gambar #%s dari #%s gambar.\nMendapatkan gambar selama %s detik." %(str(a), str(b), elapsed_time))
#----------------SEARCH SECTION----------------------------------------
            elif "Steal gpict" in msg.text:
					group = cl.getGroup(msg.to)
					cl.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + group.pictureStatus)
            elif "Steal gpic:" in msg.text:
                saya = msg.text.replace('Steal gpic: ','')
                gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
                    gna = cl.getGroup(i)
                    if h == saya:
                        cl.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
#----------------------------------------------------------------------------
            elif msg.text in ["Glist"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "%s\n" % (cl.getGroup(i).name +" ["+str(len(cl.getGroup(i).members))+"]")
                cl.sendText(msg.to,"「List Groups」\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
                
            elif msg.text in ["Mlist"]:   
                kontak = cl.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="「List Member」"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n「List Member」\n\nTotal Members : %i" % len(group)
                cl.sendText(msg.to, msgs)

            elif msg.text in ["Invite"]:
              if msg.from_ in admin:
                wait["ricoinvite"] = True
                random.choice(KAC).sendText(msg.to,"Mana kontaknya?")
                
            elif ("Cek " in msg.text):
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   mi = cl.getContact(key1)
                   cl.sendText(msg.to,"" +  key1)

            elif "Steal mid @" in msg.text:
                _name = msg.text.replace("Steal mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        cl.sendText(msg.to, g.mid)
                    else:
                        pass
                        
            #elif "Invite gcall" in msg.text:
            	#t = msg.text.replace("Invite gcall ","")
                #korban2 = t.split()
                #midd = korban2[0]
                #jumlah = int(korban2[1])
                #thisgroup = cl.getGroups(msg.to)
		            #Mids = [contact.mid for contact in thisgroup[0].members]
		        	#mi_d = Mids[:33]
                	#if jumlah <= 500:
                		#for var in range(0,jumlah)
		        		#cl.inviteGroupCall(msg.to, mi_d)
		        		#cl.sendText(msg.to,"Success")
            elif "mid" == msg.text:
                cl.sendText(msg.to,mid)
            elif msg.text in ["bqr"]:
              if msg.from_ in admin:  
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sukses Membuka QR")
                    else:
                        cl.sendText(msg.to,"Sukses Membuka QR")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group ô€œô€„‰👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œô€„‰")
            
            elif msg.text in ["tqr"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    cl.updateGroup(group)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Sukses Menutup QR")
                    else:
                        cl.sendText(msg.to,"Sukses Menutup QR")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"It can not be used outside the group  👈")
                    else:
                        cl.sendText(msg.to,"Can not be used for groups other than ô€œ")
                        
            elif "Steal info @" in msg.text:
              if msg.from_ in admin:
                nama = msg.text.replace("Steal info @","")
                target = nama.rstrip(' ')
                tob = cl.getGroup(msg.to)
                for g in tob.members:
                    if target == g.displayName:
                        gjh = cl.getContact(g.mid)
                        try:
                            cover = cl.channel.getCover(g.mid)
                        except:
                            cover = ""
                        cl.sendText(msg.to,"[NamaNya]:\n" + gjh.displayName + "\n[MidNya]:\n" + gjh.mid + "\n[BioNya]:\n" + gjh.statusMessage + "\n[Foto Profil Nya]:\nhttp://dl.profile.line-cdn.net/" + gjh.pictureStatus + "\n[CoverNya]:\n" + str(cover))
                    else:
                        pass

            elif msg.text in ["url","Url"]:
                if msg.toType == 2:
                    g = cl.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        cl.updateGroup(g)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"Link QR Grup : \n line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Hal ini tidak dapat digunakan di luar kelompok")
                    else:
                        cl.sendText(msg.to,"Tidak dapat digunakan untuk kelompok selain")
                        
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.id,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))

            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"Link QR Grup : \n line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in [".rj"]:
                    gid = cl.getGroupIdsInvited()
                    for i in gid:
                        cl.rejectGroupInvitation(i)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Semua Undangan sudah di Batalkan Boss 😉")
                    else:
                        cl.sendText(msg.to,"Done 😉")
#-----------------------------------------------------------#
            elif "#leave" in msg.text:
                try:
                    import sys
                    sys.exit()
                except:
                    pass
#-----------------------------------------------------------#
                
#-----------------TOKEN,NAMA,BIO,NAMABIO-------------#
            
            elif "Myn" in msg.text:
                profile = cl.getProfile()
                text = profile.displayName
                cl.sendText(msg.to, text)
                
            elif "Myb" in msg.text:
                profile = cl.getProfile()
                text = profile.statusMessage
                cl.sendText(msg.to, text)
                
            elif "Mynb" in msg.text:
                profile = cl.getProfile()
                text = profile.displayName
                cl.sendText(msg.to, text)
                tixt = profile.statusMessage
                cl.sendText(msg.to, tixt)

            elif msg.text in ["Myt"]:
              if msg.from_ in admin:
                cl.sendText(msg.to,cl.authToken)
                
#-----------------TOKEN,NAMA,BIO,NAMABIO-------------#

#------------------------------------------------------------------#	

#-----------------_SCRIPT ULTI BY CORRY_------------------#
            elif "Slain " in msg.text:
               if msg.from_ in admin:
                remove0 = msg.text.replace("Slain ","")
                remove1 = remove0.lstrip()
                remove2 = remove1.replace("@","")
                remove3 = remove2.rstrip()
                _name = remove3
                groups = cl.getGroup(msg.to)
                targets = []
                for s in groups.members:
                    if _name == s.displayName:
                        targets.append(s.mid)
                if targets == []:
                    pass
                else:
                    for target in targets:
                        try:
                            cl.kickoutFromGroup(msg.to,[target])
                            cl.findAndAddContactsByMid(target)
                            cl.inviteIntoGroup(msg.to,[target])
                            cl.cancelGroupInvitation(msg.to,[target])
                            cl.inviteIntoGroup(msg.to,[target])
                            cl.sendText(msg.to,"You have been slain!")
                        except:
                            cl.sendText(msg.to,"Error, your account limit.")
                            break
                      
            elif "tampol " in msg.text:
             if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      cl.kickoutFromGroup(msg.to,[target])
                      cl.sendText(msg.to,"Sukses Menampol Dia!")
                   except:
                      pass
                      
#===============STEAL================
            elif "Steal cover " in msg.text:
                mention = eval(msg.contentMetadata["MENTION"])
                mention1 = mention["MENTIONEES"][0]["M"]
                contact = cl.getContact(mention1)
                cu = cl.channel.getCover(mention1)
                path = str(cu)
                try:
                    cl.sendImageWithURL(msg.to,path)
                except:
                    pass
                
            elif "Steal vid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal vid @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            path = str(cu)
                            cl.sendVideoWithURL(msg.to,path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Midpict:" in msg.text:
              if msg.from_ in admin:
                umid = msg.text.replace("Midpict:","")
                contact = cl.getContact(umid)
                try:
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                except:
                    image = "https://www.1and1.co.uk/digitalguide/fileadmin/DigitalGuide/Teaser/not-found-t.jpg"
                try:
                    cl.sendImageWithURL(msg.to,image)
                except Exception as error:
                    cl.sendText(msg.to,(error))
                    pass

            elif "Steal dp @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal dp @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    cl.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = cl.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            cl.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
 #------------------------------------------------------------------#
            elif ("ban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Sukses Banned!")
                   except:
                      pass

            elif ("unban " in msg.text):
              if msg.from_ in admin:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      del wait["blacklist"][target]
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f,sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Sukses UnBanned!")
                   except:
                      pass
                                
            elif "Ban all" in msg.text:
              if msg.from_ in admin:
                  if msg.toType == 2:
                       print "ok"
                       _name = msg.text.replace("Ban all","")
                       gs = cl.getGroup(msg.to)
                       cl.sendText(msg.to,"Tunggu....")
                       targets = []
                       for g in gs.members:
                           if _name in g.displayName:
                                targets.append(g.mid)
                       if targets == []:
                            cl.sendText(msg.to,"Maaf")
                       else:
                           for target in targets:
                               if not target in Bots:
                                   try:
                                       wait["blacklist"][target] = True
                                       f=codecs.open('st2__b.json','w','utf-8')
                                       json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                       cl.sendText(msg.to,"Sukses Banned!")
                                   except:
                                       cl.sentText(msg.to,"Berhasil Dihapus")

            elif "ban: " in msg.text:       
             if msg.from_ in admin:           
                       nk0 = msg.text.replace("ban: ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Target Locked")
                                except:
                                    cl.sendText(msg.to,"Error")

            elif "unban: " in msg.text:             
              if msg.from_ in admin:     
                       nk0 = msg.text.replace("unban: ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    cl.sendText(msg.to,"Target Unlocked")
                                except:
                                    cl.sendText(msg.to,"Error")
                                    
            elif msg.text in ["Clear ban"]:
              if msg.from_ in admin:
                wait["blacklist"] = {}
                cl.sendText(msg.to,"Sukses Membersihkan Daftar Penjahat")
 
            elif msg.text in ["ban"]:
				if msg.from_ in admin:
					wait["wblacklist"] = True
					cl.sendText(msg.to,"send contact")	
				
            elif msg.text in ["unban"]:
				if msg.from_ in admin:
					wait["dblacklist"] = True
					cl.sendText(msg.to,"send contact")
            
            elif msg.text in ["banlist"]:   
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Banlist")
                else:
                    num=1
                    msgs="「Daftar Penjahat」"
                    for mi_d in wait["blacklist"]:
                        msgs+="\n[%i] %s" % (num, cl.getContact(mi_d).displayName)
                        num=(num+1)
                    msgs+="\n⬜◼◻◼◻◼◻◼◻◼◻◼◻◼◻◼◻⬛\n\n「Total Penjahat」: %i" % len(wait["blacklist"])
                    cl.sendText(msg.to, msgs)
                
            elif msg.text in ["Midban",".bm"]:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    num=1
                    cocoa = "「List Blacklist」"
                    for mm in matched_list:
                        cocoa+="\n[%i] %s" % (num, mm)
                        num=(num+1)
                        cocoa+="\n「Daftar Mid Penjahat」\n\nTotal Blacklist : %i" % len(matched_list)
                    cl.sendText(msg.to,cocoa)
            elif msg.text.lower() == 'tampol':
              if msg.from_ in admin:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"Tidak ada Daftar Banlist")
                        return
                    for jj in matched_list:
                        try:
                            cl.kickoutFromGroup(msg.to,[jj])
                            cl.kickoutFromGroup(msg.to,"Untung ada gue, kalo gak grup lu bisa kena kicker")
                            print (msg.to,[jj])
                        except:
                            pass
            elif "Nuck" in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Nuck","")
                    gs = cl.getGroup(msg.to)
                    cl.sendText(msg.to,"BYE BYE BITCHES~")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak ada Member")
                        cl.sendText(msg.to,"Nothing Bosqu")
                    else:
                        for target in targets:
                          if not target in Bots:
                            try:
                                klist=[cl]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                cl.sendText(msg,to,"Hahaha")
                                cl.sendText(msg,to,"Fakyu Sundala")
#-----------------------------------------------
            elif msg.text in ["Out","out"]:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        cl.sendText(msg.to,"Bye Bye "  +  str(ginfo.name)  + " 😘")
                        cl.leaveGroup(msg.to)
                    except:  
											pass
#-----------------------------------------------
#--------------------------------------------------------
	    elif "Out: " in msg.text:
		ng = msg.text.replace("Out: ","")
		gid = cl.getGroupIdsJoined()
                for i in gid:
                    h = cl.getGroup(i).name
		    if h == ng:
			cl.sendText(i,"Bye "+h+"~")
		        cl.leaveGroup(i)
			cl.sendText(msg.to,"Sukses Keluar Dari Grup ["+ h +"] ~")
		    else:
			pass
#-----------------------------------------------
	#------------------NOTIFIED_KICKOUT_FROM_GROUP-----------------
        if op.type == 19:
		if wait["protect"] == True:
                    if op.param2 in admin:
                        pass
                    try:
                        cl.kickoutFromGroup(op.param1,[op.param2])
			cl.inviteIntoGroup(op.param1,[op.param3])
                    except:
                        try:
			    cl.kickoutFromGroup(op.param1,[op.param2])
			    cl.inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group\ngid=["+op.param1+"]\nmid=["+op.param2+"]")
                        if op.param2 in wait["blacklist"]:
                            pass
                        else:
			    if op.param2 in admin:
			        pass
			    else:
                                wait["blacklist"][op.param2] = True
                    if op.param2 in wait["blacklist"]:
                        pass
                    else:
		        if op.param2 in admin:
			    pass
		        else:
                            wait["blacklist"][op.param2] = True
#--------------------------NOTIFIED_UPDATE_GROUP---------------------
	if op.type == 13:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["inviteprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["cancelprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    cl.cancelGroupInvitation(op.param1,[op.param3])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
	if op.type == 11:
	    if op.param2 not in Bots:
		if op.param2 in Bots:
		    pass
		elif wait["linkprotect"] == True:
		    wait ["blacklist"][op.param2] = True
		    G = cl.getGroup(op.param1)
		    G.preventJoinByTicket = True
		    cl.updateGroup(G)
		    random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
		else:
		    cl.sendText(op.param1,"")
	    else:
		cl.sendText(op.param1,"")
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
                    c = Message(to=op.param1, from_=None, text=None, contentType=7)
                    c.contentMetadata={"STKID":153359,"STKPKGID":2000006,"STKVER":1}
                    cl.sendMessage(c)
                    
                    
#------Open QR Kick start------#
        if op.type == 11:
            if wait["linkprotect"] == True:
		if op.param2 in admin:
		    pass
		else:
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = True
                    cl.updateGroup(G)
                    cl.sendText(op.param1, "Mau ngapain bang "+cl.getProfile(op.param3).displayName+"?")
                    cl.kickoutFromGroup(op.param1,[op.param3])
            else:
                pass
        #------Open QR Kick finish-----#
#------------------------------------------------------------------------------------
        if op.param3 == "1":
            if op.param1 in protectpict:
                group = cl.getGroup(op.param1)
                try:
					group.pictureStatus = wait["pro_pict"][op.param1]
					cl.updateGroup(group)
					cl.sendText(op.param1, "Grouppict protect now")
					wait["blacklist"][op.param2] = True
					f=codecs.open('st2__b.json','w','utf-8')
					json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                except Exception as e:
                    print e
                    pass
        if op.type == 55:
            print "[NOTIFIED_READ_MESSAGE]"
            try:
                if op.param1 in wait2['readPoint']:
                    Nama = cl.getContact(op.param2).displayName
                    if Nama in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n🐶 " + Nama
                        wait2['ROM'][op.param1][op.param2] = "🐷 " + Nama
                        wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                else:
                    cl.sendText
            except:
                pass
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                            Name = cl.getContact(op.param2).displayName
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        cl.sendText(op.param1, "Haii " + "☞ " + nick[0] + " ☜" + "\nNgintip Aja Niih. . .\nChat Kek Idiih (-__-)   ")
                                    else:
                                        cl.sendText(op.param1, "Haii " + "☞ " + nick[1] + " ☜" + "\nBetah Banget Jadi Pengacang. . .\nChat Dong (-,-)   ")
                                else:
                                    cl.sendText(op.param1, "Haii " + "☞ " + Name + " ☜" + "\nAda Yang Buka GC Nih???\nSini Gabung Chat...   ")
                        else:
                            pass
                    else:
                        pass
                except:
                    pass

        else:
            pass
        if op.type == 59:
            print op

    except Exception as error:
        print error
#==============================================================================#
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                        json.dump(read, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass
                
        if op.type == 59:
            print op
    except Exception as error:
        print error

def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True
def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"『%H:%M』")
                profile = cl.getProfile()
                profile.displayName = wait["cName"] + nowT
                cl.updateProfile(profile)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()
#-------------------------------------------------------------------------------------------#
while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)
#------------------------------------------------------------------------------------------