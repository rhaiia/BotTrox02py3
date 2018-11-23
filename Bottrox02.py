from linepy import *
from akad.ttypes import *
from multiprocessing import Pool, Process
from akad.ttypes import ContentType as Type
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,os,subprocess
from bs4 import BeautifulSoup
from humanfriendly import format_timespan, format_size, format_number, format_length
import time, random, sys, json, codecs, threading, glob, re, string, os, requests, subprocess, six, ast, pytz, urllib, urllib.parse
from gtts import gTTS
from googletrans import Translator
botStart = time.time()
#================
readOpen = codecs.open("read.json","r","utf-8")
settingsOpen = codecs.open("temp.json","r","utf-8")
imagesOpen = codecs.open("image.json","r","utf-8")
stickersOpen = codecs.open("sticker.json","r","utf-8")
read = json.load(readOpen)
settings = json.load(settingsOpen)
images = json.load(imagesOpen)
stickers = json.load(stickersOpen)
#===========
print ("================================")
print ("====WELCOME TO BOTTROX BOT====")
print ("Memuat Akun BOT 1")
k1 = LINE() #Login Via QR
#k1 = LINE("SIMPAN TOKEN KAMU DI SINI")
k1.log("\nToken BOT1=> " + str(k1.authToken))
print ("Sukses Login Akun BOT")
#===========

print ("Sukses Menjalankan BOT !!!")
print ("╭━━━━━━━━━━━━━━━━━━━")
print ("┣━━━━━━━━━━━━━━━━━━━")
print ("┣ 🇲🇨BOTTROX BOT🇲🇨")
print ("┣━━━━━━━━━━━━━━━━━━━")

MMenu ="""╭━━━━━━━━━━━━━━━
┣━━━━━━━━━━━━━
┣      ✰Self Menu✰
┣━━━━━━━━━━━━━
┣╔════════════
┣╠[🇲🇨]Respon
┣╠[🇲🇨]woy
┣╠[🇲🇨]Sider on/off
┣╠[🇲🇨]My
┣╠[🇲🇨]Gn <Nama Group>
┣╠[🇲🇨]Speed
┣╠[🇲🇨]Ginfo
┣╠[🇲🇨]Memberlist
┣╠[🇲🇨]Getpict @Tag
┣╠[🇲🇨]Getvideo @Tag
┣╠[🇲🇨]Getname @Tag
┣╠[🇲🇨]Getstatus @Tag
┣╠[🇲🇨]Getcontact @Tag
┣╠[🇲🇨]Getmid @Tag
┣╠[🇲🇨]Add @Tag
┣╠[🇲🇨]Friend on
┣╠[🇲🇨]Abouts
┣╠[🇲🇨]@restart
┣╠[🇲🇨]Runtime
┣╠[🇲🇨]Mymid
┣╠[🇲🇨]Botmid
┣╠[🇲🇨]Gid
┣╠[🇲🇨]Gurl
┣╠[🇲🇨]Gruplist
┣╠[🇲🇨]Gpict
┣╠[🇲🇨]Gname
┣╠[🇲🇨]Buka/Tutup qr
┣╠[🇲🇨]Link group
┣╚════════════
┣→Perintah Hiburan←
┣🇮🇩Smule <id>
┣🇮🇩Smuledown <link oc>
┣━━━━━━━━━━━━━━━
┣━━━━━━━━━━━━━━━
┣ 🇮🇩 BotTrox team 🇮🇩
┣━━━━━━━━━━━━━━━
┣https://line.me/ti/p/~iia008
┣━━━━━━━━━━━━━━━"""

MVps ="""╭━━━━━━━━━━━━━━━━━━━
┣═══════𖤓Ready𖤓════════
┣>•TERIMA JASA VIP SMULE
┣ANDROID :
┣>•25rb 1 thn
┣IPHONE : 
┣>•200rb
┣>•Via bank BCA
┣
┣>•Minat hubungi saya 
┣>•
┣Kontak :
┣https://line.me/ti/p/~iia008
┣━━━━━━━━━━━━━━━━━━━"""

MBca ="""╭━━━━━━━━━━━━━━━━━━━
┣═══════𖤓My Rekening𖤓══
┣ Rekening : 1390202012
┣Atas Nama : Derri pirman
┣━━━━━━━━━━━━━━━━━━━"""

MAdmin = """╭━━━━━━━━━━━━━━━━━━━
┣═══════𖤓Price𖤓════════
┣𖤓Bot Protect Group𖤓
┣→Indonesia←
┣[★]Registrasi 250K
┣[★]Bulan Selanjutnya 150K/Bulan
┣
┣Total Bots → 10 Bots + 1 Backup
┣1 Group → 2 Admin & 2 Staff
┣→Admin & Staff Sama² Bisa Undang Member
┣Bedanya Admin Bisa Perintah Bot
┣Dan Staff Tidak Bisa Perintah Bot
┣
┣Pembayaran Via :
┣[★]Bank BCA (Bank Central Asia)
┣
┣Kontak :
┣https://line.me/ti/p/~iia008
┣━━━━━━━━━━━━━━━━━━━
┣__[★]B o t T r o x   Ｔｅａｍ[★]__
┣━━━━━━━━━━━━━━━━━━━"""
#================ 
oepoll = OEPoll(k1)
k1Profile = k1.getProfile()
k1Settings = k1.getSettings()
k1MID = k1.getProfile().mid
#================
KAC = [k1]
Bots = [k1MID]

OWNER=["u303c7b0e45475464c6e2e74a82137ed0"] #BotTrox
admin=["u303c7b0e45475464c6e2e74a82137ed0","u1608ae21e5de2547b5fa8707b21ca220"] #BotTrox
  
staff=[
  "u303c7b0e45475464c6e2e74a82137ed0", #staff 1
  "u1608ae21e5de2547b5fa8707b21ca220", #staff 2
  "u1608ae21e5de2547b5fa8707b21ca220", #staff 3
  "u1608ae21e5de2547b5fa8707b21ca220", #staff 4
  "u1608ae21e5de2547b5fa8707b21ca220", #staff 5
  "u1608ae21e5de2547b5fa8707b21ca220", #staff 6
  "u1608ae21e5de2547b5fa8707b21ca220"] #staff 7
#================
msg_dict = {}
cctv = {
    "cyduk":{},
    "point":{},
    "sidermem":{}
}

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time()

wait={
    "lang":"JP",
    "limit": 10,
    "contact":False,
    "AddFriend":False,
    "detectMention":False,
    "autoJoin":False,
    "autoAdd":False,
    "Protectkick":False,
    "pname":{},
    "pro_name":{},
    "ProtectInvite":False,
    "ProtectQR":False,
    "Protectcancel":False,
    "checkContact": False,
    "myProfile": {
        "displayName": "",
        "pictureStatus": "",
        "statusMessage": ""
    },
    "addadmin":False,
    "delladmin":False,
    "banAdd":False,
    "banDel":False,
    "Sider":{},
    "blacklist":{}
}
wait["myProfile"]["displayName"] = k1Profile.displayName
wait["myProfile"]["statusMessage"] = k1Profile.statusMessage
wait["myProfile"]["pictureStatus"] = k1Profile.pictureStatus

def mention(self, to, nama):
        aa = ""
        bb = ""
        strt = int(0)
        akh = int(0)
        nm = nama
        myid = self.talk.getProfile().mid
        if myid in nm:    
            nm.remove(myid)
        for mm in nm:
          akh = akh + 6
          aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
          strt = strt + 7
          akh = akh + 1
          bb += "@nrik \n"
        aa = (aa[:int(len(aa)-1)])
        text = bb
        try:
            msg = Message()
            msg.to = to
            msg.text = text
            msg.contentMetadata = {'MENTION':'{"MENTIONEES":['+aa+']}'}
            msg.contentType = 0
            self.talk.sendMessage(0, msg)
        except Exception as error:
           print(error, 'def Mention')
           
def summon(to, mid):
    try:
        arrData = ""
        ginfo = k1.getGroup(to)
        textx = " ┣❥•  1. "
        arr = []
        no = 1
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "┣❥•   {}. ".format(str(no))
            else:
            	textx += "「❥• "+ datetime.now().strftime('%H:%M:%S').format(str(len(mid)))
        k1.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        k1.sendMessage(to, "[ INFO ] Error :\n" + str(error))

def backupData():
    try:
        backup = settings
        f = codecs.open('temp.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = read
        f = codecs.open('read.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = stickers
        f = codecs.open('sticker.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        backup = images
        f = codecs.open('image.json','w','utf-8')
        json.dump(backup, f, sort_keys=True, indent=4, ensure_ascii=False)
        return True
    except Exception as error:
        logError(error)
        return False
            
def restartBot():
    print ("[ INFO ] BOT RESETTED")
    backupData()
    time.sleep(5)
    python = sys.executable
    os.execl(python, python, *sys.argv)

def logError(text):
    k1.log("[ ERROR ] " + str(text))
    time_ = datetime.now()
    with open("errorLog.txt","a") as error:
        error.write("\n[%s] %s" % (str(time), text))
        
def load():
    global images
    global stickers
    with open("image.json","r") as fp:
        images = json.load(fp)
    with open("sticker.json","r") as fp:
        stickers = json.load(fp)
def translate(to_translate, to_language="auto"):
    bahasa_awal = "auto"
    bahasa_tujuan = to_language
    kata = to_translate
    url = 'https://translate.google.com/m?sl=%s&tl=%s&ie=UTF-8&prev=_m&q=%s' % (bahasa_awal, bahasa_tujuan, kata.replace(" ", "+"))
    agent = {'User-Agent':random.choice(settings["userAgent"])}
    cari_hasil = 'class="t0">'
    request = urllib.parse.Request(url, headers=agent)
    page = urllib.parse.urlopen(request).read()
    result = page[page.find(cari_hasil)+len(cari_hasil):]
    result = result.split("<")[0]
    return result
def sendMention(to, mid, firstmessage, lastmessage):
    try:
        arrData = ""
        text = "%s " %(str(firstmessage))
        arr = []
        mention = "@x "
        slen = str(len(text))
        elen = str(len(text) + len(mention) - 1)
        arrData = {'S':slen, 'E':elen, 'M':mid}
        arr.append(arrData)
        text += mention + str(lastmessage)
        k1.sendMessage(to, text, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        logError(error)
        k1.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def mentionMembers(to, mid):
    try:
        arrData = ""
        textx = "Total User「{}」\n\n  [•√]\n1. ".format(str(len(mid)))
        arr = []
        no = 1
        num = 2
        for i in mid:
            mention = "@x\n"
            slen = str(len(textx))
            elen = str(len(textx) + len(mention) - 1)
            arrData = {'S':slen, 'E':elen, 'M':i}
            arr.append(arrData)
            textx += mention
            if no < len(mid):
                no += 1
                textx += "%i. " % (num)
                num=(num+1)
            else:
                try:
                    no = "\n╚══[ {} ]".format(str(k1.getGroup(to).name))
                except:
                    no = "\n╚══[ Success ]"
        k1.sendMessage(to, textx, {'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
    except Exception as error:
        k1.sendMessage(to, "[ INFO ] Error :\n" + str(error))
        
def sendSticker(to, version, packageId, stickerId):
    contentMetadata = {
        'STKVER': version,
        'STKPKGID': packageId,
        'STKID': stickerId
    }
    k1.sendMessage(to, '', contentMetadata, 7)
    
def sendImage(to, path, name="image"):
    try:
        k1.sendImageWithURL(to, str(path))
    except Exception as error:
        logError(error)
def sendMessageWithFooter(to, text):
	ticket = settings["idline"]
	h = k1.getContact(k1MID)
	pict = "http://dl.profile.line-cdn.net/" + h.pictureStatus
	mecin = k1Profile.displayName
	garam = {"AGENT_ICON": pict,
	    "AGENT_NAME": mecin,
	    "AGENT_LINK": ticket
	}
	k1.sendMessage(to, text, contentMetadata=garam)
def sendMentionFooter(to, text="", mids=[]):
    arrData = ""
    arr = []
    mention = "@Meka Finee "
    if mids == []:
        raise Exception("Invalid mids")
    if "@!" in text:
        if text.count("@!") != len(mids):
            raise Exception("Invalid mids")
        texts = text.split("@!")
        textx = ""
        for mid in mids:
            textx += str(texts[mids.index(mid)])
            slen = len(textx)
            elen = len(textx) + 15
            arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mid}
            arr.append(arrData)
            textx += mention
        textx += str(texts[len(mids)])
    else:
        textx = ""
        slen = len(textx)
        elen = len(textx) + 15
        arrData = {'S':str(slen), 'E':str(elen - 4), 'M':mids[0]}
        arr.append(arrData)
        textx += mention + str(text)
    k1.sendMessage(to, textx, {'AGENT_NAME': k1Profile.displayName, 'AGENT_LINK': settings["idline"],'AGENT_ICON': "http://dl.profile.line-cdn.net/0h6wkn-ZTOaVhWF0QWcOQWD2pSZzUhOW8QLiMubCQQNG8vdCcObiEgPyYTPzpycygOPXlxayMSPm54", 'MENTION': str('{"MENTIONEES":' + json.dumps(arr) + '}')}, 0)
def dt_to_str(dt):
    return dt.strftime('%H:%M:%S')
def cTime_to_datetime(unixtime):
    return datetime.fromtimestamp(int(str(unixtime)[:len(str(unixtime))-3]))
def delExpire():
    if temp_flood != {}:
        for tmp in temp_flood:
            if temp_flood[tmp]["expire"] == True:
                if time.time() - temp_flood[tmp]["time"] >= 1*10:
                    temp_flood[tmp]["expire"] = False
                    temp_flood[tmp]["time"] = time.time()
                    try:
                        k1.sendMessage(tmp, "Bot active again.!")
                    except Exception as error:
                        logError(error)
def command(text):
    pesan = text.lower()
    if settings["setKey"] == True:
        if pesan.startswith(settings["keyCommand"]):
            satria = pesan.replace(settings["keyCommand"],"")
        else:
            satria = "Undefined command"
    else:
        satria = text.lower()
    return satria
    
def bot(op):
    global time
    global ast
    global groupParam
    try:
        if op.type == 0:
            return
        if op.type == 5:
          if wait["autoAdd"] == False:
            #if op.param3 in k4MID:
              k1.findAndAddContactsByMid(op.param1)
              k1.sendMessage(op.param1, "MAKASIH UDAH DI ADD")
              k1.sendContact(op.param1, 'u1608ae21e5de2547b5fa8707b21ca220')
                
        if op.type == 13:
          if k1MID in op.param3:
            if wait["autoJoin"] == True:
              k1.acceptGroupInvitation(op.param1)
            else:
              try:
                k1.acceptGroupInvitation(op.param1)
                k1.sendMessage(op.param1, "assalamualaikum wr.wb\nsalken all....🤗🤗")
                #k1.leaveGroup(op.param1)
              except:
                pass
                        
        if op.type == 25:
            msg = op.message
            text = msg.text
            msg_id = msg.id
            receiver = msg.to
            sender = msg._from
            to = msg.to
            if msg.toType == 0 or msg.toType == 1 or msg.toType == 2:
                if msg.toType == 0:
                    if sender != k1.profile.mid:
                        to = sender
                    else:
                        to = receiver
                elif msg.toType == 1:
                    to = receiver
                elif msg.toType == 2:
                    to = receiver
                if msg.contentType == 13:
                  if wait["contact"] == True:
                    msg.contentType = 0
                    k1.sendMessage(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                      contact = k1.getContact(msg.contentMetadata["mid"])
                      try:
                        cu = k1.channel.getCover(msg.contentMetadata["mid"])
                      except:
                        pass
                    else:
                      contact = k1.getContact(msg.contentMetadata["mid"])
                      try:
                        cu = k1.channel.getCover(msg.contentMetadata["mid"])
                      except:
                        pass
                        
                  elif wait["AddFriend"] == True:
                  #if msg._from in owner:
                    _name = msg.contentMetadata["displayName"]
                    invite = msg.contentMetadata["mid"]
                    groups = k1.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                      if _name in s.displayName:
                        k1.sendMessage(msg.to,"-> " + _name + " was here")
                        break
                      elif invite in wait["blacklist"]:
                        k1.sendMessage(msg.to,"Sorry, " + _name + " On Blacklist")
                        k1.sendMessage(msg.to,"Remove User From Blacklist Boss !!!" + invite)
                        break
                      else:
                        targets.append(invite)
                    if targets == []:
                      pass
                    else:
                      for target in targets:
                        try:
                          k1.findAndAddContactsByMid(target)
                          k1.inviteIntoGroup(msg.to,[target])
                          k1.sendMessage(msg.to,"Already Invited Boss 💋: \n➡" + _name)
                          wait["AddFriend"] = False
                          break
                        except:
                          try:
                            k1.findAndAddContactsByMid(invite)
                            k1.inviteIntoGroup(op.param1,[invite])
                            wait["AddFriend"] = False
                          except:
                            try:
                              k1.findAndAddContactsByMid(invite)
                              k1.inviteIntoGroup(op.param1,[invite])
                              wait["AddFriend"] = False
                              k1.sendMessage(msg.to,"Suck`es hahahahaha💋: \n➡" + _name)
                              break
                            except:
                              try:
                                k1.findAndAddContactsByMid(invite)
                                k1.inviteIntoGroup(op.param1,[invite])
                                wait["AddFriend"] = False
                                k1.sendMessage(msg.to,"Done ✔ Boss 💋 \n➡" + _name)
                                break
                              except:
                                k1.sendMessage(msg.to,"Negative, Error detected")
                                wait["AddFriend"] = False
                                break
                                
                if msg.contentType == 0:
                    if text is None:
                        return
                    else:
                        satria = command(text)
                        if msg.text in ["Absen","Absen bot","Absen dulu","Respon"]:
                         if msg._from in admin:
                          k1.sendMessage(msg.to,"Hadir...")
                         # k1.sendMessage(msg.to,"Semua Sudah Hadir Boss\nSiap Protect Group")
                  
                        if satria == "help":
                            if wait["lang"] == "JP":
                              k1.sendMessage(msg.to,MMenu)
                              k1.sendContact(to, k1MID)
                            else:
                              k1.sendMessage(msg.to,MMenu)
                              k1.sendContact(to, k1MID)
                              
                        elif msg.text in ["My BCA","my bca"]:
                         if msg._from in OWNER:
                           if wait["lang"] == "JP":
                              k1.sendMessage(msg.to,MBca)
                           else:
                              k1.sendMessage(msg.to,MBca)
                              
                        elif msg.text in ["Open","Order"]:
                         if msg._from in OWNER:
                           if wait["lang"] == "JP":
                              k1.sendMessage(msg.to,MVps)
                              k1.sendContact(to, k1MID)
                           else:
                              k1.sendMessage(msg.to,MVps)
                              k1.sendContact(to, k1MID)
                              
                        elif msg.text in ["Price admin","price admin"]:
                         if msg._from in OWNER:
                           if wait["lang"] == "JP":
                              k1.sendMessage(msg.to,MAdmin)
                              k1.sendContact(to, k1MID)
                           else:
                              k1.sendMessage(msg.to,MAdmin)
                              k1.sendContact(to, k1MID)
                              
                        elif satria.startswith("tagme "):
                          if sender in OWNER:
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            settings["tag"] = str(key).lower()
                            k1.sendMessage(to, "Berhasil mengganti Auto Respon")
                        elif satria == "spamcall":
                          if msg.toType == 2:
                            group = k1.getGroup(to)
                            members = [mem.mid for mem in group.members]
                            jmlh = int(wait["limit"])
                            k1.sendMessage(msg.to, "Spam Call Grup {} Done ".format(str(wait["limit"])))
                            if jmlh <= 1000:
                              for x in range(jmlh):
                                 try:
                                    k1.acquireCallRoute(to)
                                    k1.inviteIntoGroupCall(to, contactIds=members)
                                 except Exception as e:
                                    k1.sendMessage(msg.to,str(e))
                            else:
                                k1.sendMessage(msg.to,"Error out off range")
                            
                        elif satria.startswith("sendmp4 "): 
                          if sender in OWNER:
                            separate = text.split(" ")
                            linknya = text.replace(separate[0] + " ","")
                            k1.sendVideoWithURL(to, linknya)
                        elif satria.startswith("sendmp3 "): 
                          if sender in OWNER:
                            separate = text.split(" ")
                            linknya = text.replace(separate[0] + " ","")
                            k1.sendAudioWithURL(to, linknya)
                        elif satria.startswith("smuledown "): 
                          if sender in OWNER:
                            separate = text.split(" ")
                            linknya = text.replace(separate[0] + " ","")
                            k1.sendMessage(to, "https://sing.salon/smule-downloader/?url="+linknya)
                        elif satria == "abouts":
                          if sender in admin:
                            k1.sendMessage(to,"Waiting..")
                            h = k1.getContact(sender)
                            timeNow = time.time()
                            runtime = timeNow - botStart
                            runtime = format_timespan(runtime)
                            start = time.time()
                            elapsed_time = time.time() - start
                            owner = "u1608ae21e5de2547b5fa8707b21ca220"
                            creator = k1.getContact(owner)
                            grouplist = k1.getGroupIdsJoined()
                            contactlist = k1.getAllContactIds()
                            blockedlist = k1.getBlockedContactIds()
                            CVU = ["0.9℃","1.1℃","1.0℃","1.2℃","1.3℃","1.4℃","1.5℃","1.6℃","0.8℃"]
                            resultCvu = random.choice(CVU)
                            aboter = "╔╦━━━[ABOUT BOTS]━━━╦━━╮"
                            aboter += "\n║╠ Nama BOT: B O T T R O X   B O T"
                            aboter += "\n║╠ Bot active: {}".format(str(runtime))
                            aboter += "\n║╠ Bot version: *Python3"
                            aboter += "\n║╠ Thrift version: 0.11.0"
                            aboter += "\n║╠ Runner cvu: "+resultCvu
                            aboter += "\n║╠ Version bots: Versi 2.4"
                            #aboter += "\n║╠ Expt Bots: "+settings["EXPT"]
                            aboter += "\n║╠ SpeedBots: {}".format(str(elapsed_time))
                            aboter += "\n║╠══════════════════"
                            aboter += "\n║╠ Creator name : {}".format(creator.displayName)
                            aboter += "\n║╠ Creator id :  https://line.me/ti/p/Yd11Ktsd4V "
                            aboter += "\n╚╩━━[Succes]━━╩━╯"
                            #cover = "http://oi65.tinypic.com/vrwugj.jpg"
                            #k1.sendImageWithURL(to, "http://oi65.tinypic.com/vrwugj.jpg")
                            k1.sendMessage(to, aboter)
                            k1.sendContact(to, k1MID)
#======================================
                        elif satria == "@restart":
                          if sender in OWNER:
                            k1.sendMessage(to, "Sebentar...")
                            k1.sendMessage(to, "Selesai.!!\n\nSilahkan command 1x ktik me\ntunggu beberapa saat skitar 1-2 mnt\njika respon command me lagi 1x\ntunggu respon (DONE NORMAL)")
                            settings["restartPoint"] = to
                            restartBot()
                        elif satria == "runtime":
                          if sender in OWNER:
                            timeNow = time.time()
                            runtime = timeNow - botStart
                            runtime = format_timespan(runtime)
                            k1.sendMessage(to, "┣━━━╦RUNTIME BOTS╦━━━╣\n ┣━╦{}╦━╣".format(str(runtime)))
                        elif satria == "unsend":
                          if sender in OWNER:
                            k1.unsendMessage(msg_id)
                        elif satria == "speed":
                          if sender in admin:
                            start = time.time()
                            k1.sendMessage(to, "Tunggu.......")
                            elapsed_time = time.time() - start
                            k1.sendMessage(to,format(str(elapsed_time)))
#==============================================================================#
#==============================================================================#
                        elif satria.startswith("b1name "):
                          if sender in OWNER:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 20:
                                profile = k1.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k1.sendMessage(to,"┣━━━╦NAMA PROFILE DIUBAH MENJADI╦━━━╣\n{}".format(str(string)))
                        elif satria.startswith("allname "):
                          if sender in OWNER:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 20:
                                profile = k1.getProfile()
                                profile.displayName = string
                                k1.updateProfile(profile)
                                k1.sendMessage(to,"{}".format(str(string)))
                        elif satria.startswith("botstatus "):
                          if sender in OWNER:
                            separate = msg.text.split(" ")
                            string = msg.text.replace(separate[0] + " ","")
                            if len(string) <= 500:
                                profile = k1.getProfile()
                                profile.statusMessage = string
                                k1.updateProfile(profile)
                                k1.sendMessage(to,"┣━━━╦STATUS PROFILE DIUBAH MENJADI╦━━━╣\n {}".format(str(string)))
                                
                        elif satria == "me":
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            k1.sendMessage(to,"┣━━╦KONTAK PROFILE╦━━╣\n " + readTime)
                            sendMentionFooter(to, "@!", [sender])
                            k1.sendContact(to, sender)
                        elif satria == "mybots":
                          if sender in OWNER:
                            k1.sendMessage(to,"┣━━╦━━━━━━━━━━━╦━━╣")
                            k1.sendContact(to, k1MID)
                            k1.sendMessage(to,"┣━━╦━━━KONTAK BOTS━━━╦━━╣")
                        elif satria == "mymid":
                            h = k1.getContact(sender)
                            k1.sendMessage(to,h.mid)
                        elif satria == "botmid":
                          if sender in OWNER:
                            h = k1.getContact(k1MID)
                            k1.sendMessage(to,h.mid)
                            
                        elif satria == "myinfo":
                          if sender in admin:
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            h = k1.getContact(sender)
                            k1.sendMessage(to,"┣━━╦━━INFO KONTAK━━╦━━╣")
                            k1.sendContact(to, sender)
                            k1.sendMessage(to,"┣━━╦━━━INFO MID━━━╦━━╣\n" + h.mid)
                            k1.sendMessage(to,"┣━━╦━━INFO NAMA━━╦━━╣\n" + h.displayName)
                            k1.sendMessage(to,"┣━━╦━━INFO STATUS━━╦━━╣\n" + h.statusMessage)
                            k1.sendMessage(to,"┣━━╦━━FOTO PROFILE━━╦━━╣")
                            k1.sendImageWithURL(to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            k1.sendMessage(to,"Success..\n" + readTime)
                        elif satria == "myvideo":
                          if sender in admin:
                            h = k1.getContact(sender)
                            k1.sendVideoWithURL(to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                        elif satria.startswith("getmid "):
                          if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                ret_ = ""
                                for ls in lists:
                                    ret_ += "{}".format(str(ls))
                                k1.sendMessage(to, str(ret_))
                        elif satria.startswith("getpict "):
                          if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.k1.naver.jp/" + k1.getContact(ls).pictureStatus
                                    k1.sendImageWithURL(to, str(path))
                        elif satria.startswith("getvideo "):
                          if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    path = "http://dl.profile.k1.naver.jp/" + k1.getContact(ls).pictureStatus
                                    k1.sendVideoWithURL(to, str(path))
                        elif satria.startswith("getname "):
                          if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = k1.getContact(ls)
                                    k1.sendMessage(to, "┣━━NAMA DI TAMPILKAN━━╣\n{}".format(str(contact.displayName)))
                        elif satria.startswith("getstatus "):
                          if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = k1.getContact(ls)
                                    k1.sendMessage(to, "┣━━╦━━STATUS DI TAMPILKAN━━╦━━╣\n{}".format(str(contact.statusMessage)))
                        elif satria.startswith("getcontact "):
                          if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    contact = k1.getContact(ls)
                                    mi_d = contact.mid
                                    k1.sendContact(to, mi_d)
                        elif satria.startswith("copy "):
                          if sender in OWNER:
                                if 'MENTION' in msg.contentMetadata.keys()!= None:
                                    names = re.findall(r'@(\w+)', text)
                                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                    mentionees = mention['MENTIONEES']
                                    for mention in mentionees:
                                        contact = mention["M"]
                                        break
                                    try:
                                        k1.cloneContactProfile(contact)
                                        k1.sendMessage(msg.to, "Success.!!")
                                    except:
                                        k1.sendMessage(to, "Gagal..")
                        elif satria == "recopy":
                          if sender in OWNER:
                            try:
                                k1Profile = k1.getProfile()
                                k1Profile.displayName = str(settings["myProfile"]["displayName"])
                                k1Profile.statusMessage = str(settings["myProfile"]["statusMessage"])
                                k1Profile.pictureStatus = str(settings["myProfile"]["pictureStatus"])
                                coverId = str(settings["myProfile"]["coverId"])
                                k1.updateProfileAttribute(8, k1Profile.pictureStatus)
                                k1.updateProfileCoverById(coverId)
                                k1.updateProfile(k1Profile)
                                k1.sendContact(to, sender)
                                k1.sendMessage(to, "Success.!!")
                            except Exception as e:
                                k1.sendMessage(to, "Tidak ada backupan kontak profile\nlain di backup dulu..")
                                k1.sendMessage(to, str(e))
                        elif satria == "mybackup":
                          if sender in OWNER:
                            try:
                                profile = k1.getProfile()
                                settings["myProfile"]["displayName"] = str(profile.displayName)
                                settings["myProfile"]["statusMessage"] = str(profile.statusMessage)
                                settings["myProfile"]["pictureStatus"] = str(profile.pictureStatus)
                                coverId = k1.getProfileDetail()["result"]["objectId"]
                                settings["myProfile"]["coverId"] = str(coverId)
                                k1.sendMessage(to, "Berhasil backup profile")
                            except Exception as e:
                                k1.sendMessage(to, "Gagal backup profile")
                                k1.sendMessage(to, str(e))
#======================================================
                        elif satria.startswith("music "):
                          if sender in admin:
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " ","")
                            cond = query.split(" no ")
                            search = str(cond[0])
                            result = requests.get("http://api.ntcorp.us/joox/search?q={}".format(str(search)))
                            data = result.text
                            data = json.loads(data)
                            if len(cond) == 1:
                                num = 0
                                ret_ = "╭━━━━══[Daftar lagu]"
                                for music in data["result"]:
                                    num += 1
                                    ret_ += "\n┣═ {}. {}".format(str(num), str(music["single"]))
                                ret_ += "\n╰━━━━━═[ Total {} Lagu]".format(str(len(data["result"])))
                                ret_ += "\n[Info]\nGunakan Kata kunci di bawah ini coy\n{} no「number」".format(str(msg.text),str(search))
                                k1.sendMessage(to, str(ret_))
                            elif len(cond) == 2:
                                num = int(cond[1])
                                if num <= len(data["result"]):
                                    music = data["result"][num - 1]
                                    result = requests.get("http://api.ntcorp.us/joox/song_info?sid={}".format(str(music["sid"])))
                                    data = result.text
                                    data = json.loads(data)
                                    if data["result"] != []:
                                        ret_ = "╭━━━━══[Ditampilkan]"
                                        ret_ += "\n┣═ Title : {}".format(str(data["result"]["song"]))
                                        ret_ += "\n┣═ Album : {}".format(str(data["result"]["album"]))
                                     #  ret_ += "\n┣═ Size : {}".format(str(data["result"]["size"]))
                                        ret_ += "\n┣═ Link : {}".format(str(data["result"]["mp3"][0]))
                                        ret_ += "\n╰━━━━━═[Selesai]"
                                        k1.sendImageWithURL(to, str(data["result"]["img"]))
                                        k1.sendMessage(to, str(ret_))
                                        k1.sendAudioWithURL(to, str(data["result"]["mp3"][0]))
                                        k1.sendMessage(to, "Selamat Mendengarkan Kak...")
                                        k1.sendImageWithURL(to, "http://oi65.tinypic.com/3088ih2.jpg")
                        elif satria.startswith("liryc "):
                          if sender in admin:
                            sep = msg.text.split(" ")
                            query = msg.text.replace(sep[0] + " ","")
                            cond = query.split(" no ")
                            search = cond[0]
                            api = requests.get("http://api.secold.com/joox/cari/{}".format(str(search)))
                            data = api.text
                            data = json.loads(data)
                            if len(cond) == 1:
                                num = 0
                                ret_ = "╭━━━══[Ditampilkan]"
                                for lyric in data["results"]:
                                    num += 1
                                    ret_ += "\n┣═ {}. {}".format(str(num), str(lyric["single"]))
                                ret_ += "\n╰━━━━═[ Total {} Di tampilkan]".format(str(len(data["results"])))
                                ret_ += "\n[Info]\nGunakan Kata kunci di bawah ini\n{}Liricalbum {} no「number」".format(settings["keyCommand"],str(search))
                                k1.sendMessage(to, str(ret_))
                            elif len(cond) == 2:
                                num = int(cond[1])
                                if num <= len(data["results"]):
                                    lyric = data["results"][num - 1]
                                    api = requests.get("http://api.secold.com/joox/sid/{}".format(str(lyric["songid"])))
                                    data = api.text
                                    data = json.loads(data)
                                    lyrics = data["results"]["lyric"]
                                    lyric = lyrics.replace('ti:','Title - ')
                                    lyric = lyric.replace('ar:','Artist - ')
                                    lyric = lyric.replace('al:','Album - ')
                                    removeString = "[1234567890.:]"
                                    for char in removeString:
                                        lyric = lyric.replace(char,'')
                                    k1.sendMessage(to, str(lyric))
#========================#
                        elif satria.startswith("ytlink "):
                          if sender in admin:
                            k1.sendMessage(to, "Waiting...")
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            params = {"search_query": search}
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get("https://www.youtube.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╭━━━━━[ Youtube link di tampilkan ]━"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n┣[ {} ]".format(str(data["title"]))
                                    ret_ += "\n┣━ https://www.youtube.com{}".format(str(data["href"]))
                                ret_ += "\n╰━━━━━━━━[ Total {} link]━━━━━".format(len(datas))
                                k1.sendMessage(to, str(ret_))
                        elif satria.startswith("ytmp3 "):
                          if sender in admin:
                            try:
                                k1.sendMessage(to,"Waitting...\nJangan command apapun sampai muncul\nProsess ini membutuhkan waktu yang lama\nJadi haraf sabar..")
                                textToSearch = (msg.text).replace("ytmp3 ", "").strip()
                                query = urllib.parse.quote(textToSearch)
                                url = "https://www.youtube.com/results?search_query=" + query
                                response = urllib.request.urlopen(url)
                                html = response.read()
                                soup = BeautifulSoup(html, "html.parser")
                                results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                dl = 'https://www.youtube.com' + results['href']
                                vid = pafy.new(dl)
                                stream = vid.audiostreams
                                for s in stream:
                                    start = timeit.timeit()
                                    vin = s.url
                                    img = vid.bigthumbhd
                                    hasil = vid.title
                                    hasil += '\n\nPenulis : ' +str(vid.author)
                                    hasil += '\nDurasi   : ' +str(vid.duration)+ ' (' +s.quality+ ') '
                                    hasil += '\nRating   : ' +str(vid.rating)
                                    hasil += '\nDitonton    : ' +str(vid.viewcount)+ 'x '
                                    hasil += '\nDiterbitkan : ' +vid.published
                                    hasil += '\n\nTime taken : %s' % (start)
                                    hasil += '\n\n Tunggu encoding selesai...'
                                k1.sendAudioWithURL(to,vin)
                                k1.sendImageWithURL(to,img)
                                k1.sendMessage(to,hasil)
                            except:
                                k1.sendMessage(to,"Gagal Mencari...")

                        elif satria.startswith("ytmp4 "):
                          if sender in admin:
                            try:
                                k1.sendMessage(to,"Waitting...\nJangan command apapun sampai muncul\nProsess ini membutuhkan waktu yang lama\nJadi haraf sabar..")
                                textToSearch = (msg.text).replace("ytmp4 ", "").strip()
                                query = urllib.parse.quote(textToSearch)
                                url = "https://www.youtube.com/results?search_query=" + query
                                response = urllib.request.urlopen(url)
                                html = response.read()
                                soup = BeautifulSoup(html, "html.parser")
                                results = soup.find(attrs={'class':'yt-uix-tile-link'})
                                dl = 'https://www.youtube.com' + results['href']
                                vid = pafy.new(dl)
                                stream = vid.streams
                                for s in stream:
                                    vin = s.url
                                    hasil = 'Informasi\n\n'
                                    hasil += 'Judul:\n ' + vid.title
                                    hasil += '\n Tunggu encoding selesai...'
                                k1.sendVideoWithURL(to,vin)
                                k1.sendMessage(to,hasil)
                            except:
                                k1.sendMessage(to,"Gagal Mencari...")
                        elif satria.startswith("images "):
                          if sender in OWNER:
                            separate = msg.text.split(" ")
                            search = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://rahandiapi.herokuapp.com/imageapi?key=betakey&q={}".format(urllib.parse.quote(search)))
                                data = r.text
                                data = json.loads(data)
                                if data["result"] != []:
                                    items = data["result"]
                                    path = random.choice(items)
                                    a = items.index(path)
                                    b = len(items)
                                    k1.sendImageWithURL(to, str(path))
                        elif satria.startswith("imagetxt "):
                          if sender in OWNER:
                            sep = msg.text.split(" ")
                            textnya = msg.text.replace(sep[0] + " ","")
                            urlnya = "http://chart.apis.google.com/chart?chs=480x80&cht=p3&chtt=" + textnya + "&chts=FFFFFF,70&chf=bg,s,000000"
                            k1.sendImageWithURL(msg.to, urlnya)
                        elif satria.startswith("screenshoot "):
                          if sender in OWNER:
                            k1.sendMessage(to, "Waitting...")
                            sep = text.split(" ")
                            query = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                r = web.get("http://rahandiapi.herokuapp.com/sswebAPI?key=betakey&link={}".format(urllib.parse.quote(query)))
                                data = r.text
                                data = json.loads(data)
                                k1.sendImageWithURL(to, data["result"])

                        elif satria.startswith("ttl "):
                          if sender in admin:
                            try:
                                sep = msg.text.split(" ")
                                tanggal = msg.text.replace(sep[0] + " ","")
                                r = requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                                data=r.text
                                data=json.loads(data)
                                ret_ = "╭━━━━════[Tanggal,Lahir]"
                                ret_ += "\n┣═Tanggal lahir : {}".format(str(data["data"]["lahir"]))
                                ret_ += "\n┣═Umur : {}".format(str(data["data"]["usia"]))
                                ret_ += "\n┣═Tanggal ultah : {}".format(str(data["data"]["ultah"]))
                                ret_ += "\n┣═Zodiak : {}".format(str(data["data"]["zodiak"]))
                                ret_ += "\n╰━━═════[HANYA PREDIKSI]"
                                k1.sendMessage(to, str(ret_))
                            except Exception as error:
                                logError(error)
                        elif satria.startswith("info-ig "):
                          if sender in OWNER:
                            sep = text.split(" ")
                            instagram = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                html = web.get("https://www.instagram.com/" + instagram + "/")
                                soup = BeautifulSoup(html.text, 'html5lib')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://instagram.com/" + instagram
                                k1.sendImageWithURL(msg.to, text1[0])
                                k1.sendMessage(to, user + user1 + followers + following + post + link)
                                print("[Notif] Search Instagram Sucess")
                        elif satria.startswith("info-fb "):
                          if sender in OWNER:
                            sep = text.split(" ")
                            facebook = text.replace(sep[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                html = web.get("https://www.facebook.com/" + facebook + "/")
                                soup = BeautifulSoup(html.text, 'html5lib')
                                data = soup.find_all('meta', attrs={'property':'og:description'})
                                text = data[0].get('content').split()
                                data1 = soup.find_all('meta', attrs={'property':'og:image'})
                                text1 = data1[0].get('content').split()
                                user = "Name: " + text[-2] + "\n"
                                user1 = "Username: " + text[-1] + "\n"
                                followers = "Followers: " + text[0] + "\n"
                                following = "Following: " + text[2] + "\n"
                                post = "Post: " + text[4] + "\n"
                                link = "Link: " + "https://facebook.com/" + facebook
                                k1.sendImageWithURL(msg.to, text1[0])
                                k1.sendMessage(to, user + user1 + followers + following + post + link)
                        elif satria.startswith("smule "):
                          if sender in admin:
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            smule = "https://www.smule.com/"+ key
                            k1.sendMessage(to, "ini id smulenya kak\n" + smule)
                        elif satria.startswith("searchsmule "):
                          if sender in admin:
                            k1.sendMessage(to, "Waiting...")
                            sep = text.split(" ")
                            search = text.replace(sep[0] + " ","")
                            params = {"search_query": search}
                            with requests.session() as web:
                                web.headers["User-Agent"] = random.choice(settings["userAgent"])
                                r = web.get("https://www.smule.com/results", params = params)
                                soup = BeautifulSoup(r.content, "html5lib")
                                ret_ = "╭━━━━━[ list smule di tampilkan ]━"
                                datas = []
                                for data in soup.select(".yt-lockup-title > a[title]"):
                                    if "&lists" not in data["href"]:
                                        datas.append(data)
                                for data in datas:
                                    ret_ += "\n┣[ {} ]".format(str(data["title"]))
                                    ret_ += "\n┣━ https://www.smule.com{}".format(str(data["href"]))
                                ret_ += "\n╰━━━━━━━━[ Total {} id]━━━━━".format(len(datas))
                                k1.sendMessage(to, str(ret_))
                        elif satria.startswith("twitter "):
                          if sender in OWNER:
                            sep = text.split(" ")
                            key = text.replace(sep[0] + " ","")
                            twitter = "https://www.twitter.com/"+ key
                            k1.sendMessage(to, "pencarian untuk user id " + sep + "ini twitternya kak\n" + twitter)
                        elif satria.startswith("shalat "):
                          if sender in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if data[1] != "Subuh : " and data[2] != "Dzuhur : " and data[3] != "Ashar : " and data[4] != "Maghrib : " and data[5] != "Isya : ":
                                    ret_ = "╭━━══[ Jadwal Sholat Sekitar " + data[0] + " ]"
                                    ret_ += "\n┣═Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n┣═Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\n┣═" + data[1]
                                    ret_ += "\n┣═" + data[2]
                                    ret_ += "\n┣═" + data[3]
                                    ret_ += "\n┣═" + data[4]
                                    ret_ += "\n┣═" + data[5]
                                    ret_ += "\n╰━━══[ Success ]"
                                else:
                                    ret_ = "Error : lokasi tidak dintemukan" 
                                k1.sendMessage(to, str(ret_))
                        elif satria.startswith("imsak "):
                          if sender in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if data[1] != "Imsak 🌃 : ":
                                    ret_ = "╭━━══[ Jadwal Imsak di " + data[0] + " ]"
                                    ret_ += "\n┣═Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n┣═Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\n┣═" + data[1]
                                    ret_ += "\n╰━━══[ Jangan lupa doa niat puasa nya ]"
                                else:
                                    ret_ = "Error : lokasi tidak dintemukan" 
                                k1.sendMessage(to, str(ret_))
                        elif satria.startswith("maghrib "):
                          if sender in OWNER:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apisholat.php?lokasi={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if data[4] != "Maghrib 🌇: ":
                                    ret_ = "╭━━══[ Jadwal Buka puasa di " + data[0] + " ]"
                                    ret_ += "\n┣═Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                    ret_ += "\n┣═Jam : " + datetime.strftime(timeNow,'%H:%M:%S')
                                    ret_ += "\n┣═" + data[4]
                                    ret_ += "\n╰━━══[ Jangan lupa doa buka puasanya ]"
                                else:
                                    ret_ = "Error : lokasi tidak dintemukan" 
                                k1.sendMessage(to, str(ret_))
                        elif satria.startswith("cuaca "):
                          if sender in admin:
                            separate = msg.text.split(" ")
                            location = msg.text.replace(separate[0] + " ","")
                            with requests.session() as web:
                                web.headers["user-agent"] = random.choice(settings["userAgent"])
                                r = web.get("http://api.corrykalam.net/apicuaca.php?kota={}".format(urllib.parse.quote(location)))
                                data = r.text
                                data = json.loads(data)
                                tz = pytz.timezone("Asia/Jakarta")
                                timeNow = datetime.now(tz=tz)
                                if "result" not in data:
                                  ret_ = "╭━━════[ Weather Status ]"
                                  ret_ += "\n┣═Location : " + data[0].replace("Temperatur di kota ","")
                                  ret_ += "\n┣═Suhu : " + data[1].replace("Suhu : ","") + "°C"
                                  ret_ += "\n┣═Kelembaban : " + data[2].replace("Kelembaban : ","") + "%"
                                  ret_ += "\n┣═Tekanan udara : " + data[3].replace("Tekanan udara : ","") + "HPa"
                                  ret_ += "\n┣═Kecepatan angin : " + data[4].replace("Kecepatan angin : ","") + "m/s"
                                  ret_ += "\n┣═══[ Time Status ]"
                                  ret_ += "\n┣═Tanggal : " + datetime.strftime(timeNow,'%Y-%m-%d')
                                  ret_ += "\n┣═Jam : " + datetime.strftime(timeNow,'%H:%M:%S') + " WIB"
                                  ret_ += "\n╰━━═════[ Success ]"
                                else:
                                  ret_ = "[Weather Status] Error : Location not found"
                                k1.sendMessage(to, str(ret_))
                                
                        elif satria.startswith("lokasi "):
                          if sender in OWNER:
                            try:
                                separate = msg.text.split(" ")
                                location = msg.text.replace(separate[0] + " ","")
                                with requests.session() as web:
                                    web.headers["user-agent"] = random.choice(settings["userAgent"])
                                    r = web.get("http://api.corrykalam.net/apiloc.php?lokasi={}".format(urllib.parse.quote(location)))
                                    data = r.text
                                    data = json.loads(data)
                                    if data[0] != "" and data[1] != "" and data[2] != "":
                                        link = "https://www.google.co.id/maps/@{},{},15z".format(str(data[1]), str(data[2]))
                                        ret_ = "╭━━════[ Location Status ]"
                                        ret_ += "\n┣═Location : " + data[0]
                                        ret_ += "\n┣═Google Maps : " + link
                                        ret_ += "\n╰━━━═════[ Success ]"
                                    else:
                                        ret_ = "[Details Location] Error : Location not found"
                                    k1.sendMessage(to,str(ret_))
                            except Exception as error:
                                logError(error)
            #           T E X T     T O     S P E E C H             #
            
                        elif satria.startswith("sayi "):
                          if sender in admin:
                            sep = text.split(" ")
                            say = text.replace(sep[0] + " ","")
                            lang = 'en'
                            tts = gTTS(text=say, lang=lang)
                            tts.save("inggris.mp3")
                            k1.sendAudio(to,"inggris.mp3")
                            
                        elif satria.startswith("say "):
                          if sender in admin:
                            sep = text.split(" ")
                            say = text.replace(sep[0] + " ","")
                            lang = 'id'
                            tts = gTTS(text=say, lang=lang)
                            tts.save("indo.mp3")
                            k1.sendAudio(to,"indo.mp3")
#===========================
#===========================#
                        elif satria == "tag":
                          if sender in admin:
                               group = k1.getGroup(msg.to)
                               nama = [contact.mid for contact in group.members]
                               nm1, nm2, nm3, nm4,nm5,nm6,nm7, jml = [], [], [], [],[], [], [], len(nama)
                               if jml <= 20:
                                   mentionMembers(msg.to, nama)
                               if jml > 20 and jml < 40:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, len(nama)-1):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                               if jml > 40 and jml < 60:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, len(nama)-1):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                               if jml > 60 and jml < 80:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, len(nama)-1):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                               if jml > 80 and jml < 100:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, len(nama)-1):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                               if jml > 100 and jml < 120:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, len(nama)-1):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                               if jml > 120 and jml < 140:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, len(nama)-1):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                               if jml > 140 and jml < 160:
                                   for i in range (0, 19):
                                       nm1 += [nama[i]]
                                   mentionMembers(msg.to, nm1)
                                   for j in range (20, 39):
                                       nm2 += [nama[j]]
                                   mentionMembers(msg.to, nm2)
                                   for k in range (40, 59):
                                       nm3 += [nama[k]]
                                   mentionMembers(msg.to, nm3)
                                   for l in range (60, 79):
                                       nm4 += [nama[l]]
                                   mentionMembers(msg.to, nm4)
                                   for m in range (80, 99):
                                       nm5 += [nama[m]]
                                   mentionMembers(msg.to, nm5)
                                   for n in range (100, 119):
                                       nm6 += [nama[n]]
                                   mentionMembers(msg.to, nm6)
                                   for o in range (120, 139):
                                       nm7 += [nama[o]]
                                   mentionMembers(msg.to, nm7)
                                   for p in range (140, len(nama)-1):
                                       nm8 += [nama[p]]
                                   mentionMembers(msg.to, nm8)
                                   
                        elif satria == "tag2":
                          group = k1.getGroup(msg.to)
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
 #============== TEST CCTV DAN SIDER =========================
                        elif satria == "cctv2":
                            if sender in admin:
                              k1.sendMessage(to, "Mencari CCTV...")
                              try:
                               del wait2['readPoint'][to]
                               del wait2['readMember'][to]
                              except:
                                pass
                            now2 = datetime.now()
                            wait2['readPoint'][to] = msg.id
                            wait2['readMember'][to] = ""
                            wait2['setTime'][to] = datetime.strftime(now2,"%H:%M")
                            wait2['ROM'][to] = {}
                            
                        elif satria == "ciduk2":
                            if sender in admin:
                              if msg.to in wait2['readPoint']:
                                if wait2["ROM"][msg.to].items() == []:
                                  chiya = ""
                                else:
                                  chiya = ""
                                  for rom in wait2["ROM"][msg.to].items():
                                  #print rom
                                    chiya += rom[1] + "\n"
                                k1.sendMessage(msg.to, "||Dilihat Oleh||%s\n\n||By : B o t T r o x   B o t||\n\n>Pelaku CCTV<\n%sAwas Yang CCTV Bintitan\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                              else:
                               k1.sendMessage(msg.to, "Ketik Cctv Dulu Njir\nBaru Ketik Ciduk\nDasar Pikun ♪")
                               
                        elif satria == "sider on":
                          if sender in admin:
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
                            k1.sendMessage(msg.to,"Sider on\n"  + datetime.now().strftime('%H:%M:%S'))
                            
                        elif satria == "sider off":
                          if sender in admin:
                            if msg.to in cctv['point']:
                              cctv['cyduk'][msg.to]=False
                              wait["Sider"] = False
                              k1.sendMessage(msg.to, "Sider Off\n"   + datetime.now().strftime('%H:%M:%S'))
                            else:
                              k1.sendMessage(msg.to, "Woyyy\nBelom Di Set")
                    
#============== SELESAI ===================
                                    
                        elif satria == "cctv:on":
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            if receiver in read['readPoint']:
                                try:
                                    del read['readPoint'][receiver]
                                    del read['readMember'][receiver]
                                    del read['readTime'][receiver]
                                except:
                                    pass
                                read['readPoint'][receiver] = msg_id
                                read['readMember'][receiver] = ""
                                read['readTime'][receiver] = readTime
                                read['ROM'][receiver] = {}
                                k1.sendMessage(receiver,"Mencari Cicitipi ...")
                            else:
                                try:
                                    del read['readPoint'][receiver]
                                    del read['readMember'][receiver]
                                    del read['readTime'][receiver]
                                except:
                                    pass
                                read['readPoint'][receiver] = msg_id
                                read['readMember'][receiver] = ""
                                read['readTime'][receiver] = readTime
                                read['ROM'][receiver] = {}
                                k1.sendMessage(receiver,"Set reading point : \n" + readTime)
                        elif satria == "cctv:off":
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            if receiver not in read['readPoint']:
                                k1.sendMessage(receiver,"Cicitipi off")
                            else:
                                try:
                                    del read['readPoint'][receiver]
                                    del read['readMember'][receiver]
                                    del read['readTime'][receiver]
                                except:
                                    pass
                                k1.sendMessage(receiver,"Delete reading point : \n" + readTime)
    
                        elif satria == "cctv:rest":
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            if msg.to in read["readPoint"]:
                                try:
                                    del read["readPoint"][msg.to]
                                    del read["readMember"][msg.to]
                                    del read["readTime"][msg.to]
                                    del read["ROM"][msg.to]
                                except:
                                    pass
                                k1.sendMessage(to, "Reset reading point : \n" + readTime)
                            else:
                                k1.sendMessage(to, "Belum aktif. Silahkan aktifkan terlebih dahulu")
                                
                        elif satria == "ciduk":
                            tz = pytz.timezone("Asia/Jakarta")
                            timeNow = datetime.now(tz=tz)
                            day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                            hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                            bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                            hr = timeNow.strftime("%A")
                            bln = timeNow.strftime("%m")
                            for i in range(len(day)):
                                if hr == day[i]: hasil = hari[i]
                            for k in range(0, len(bulan)):
                                if bln == str(k): bln = bulan[k-1]
                            readTime = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                            if receiver in read['readPoint']:
                                if read["ROM"][receiver].items() == []:
                                    k1.sendMessage(receiver,"Tidak Ada Sider")
                                else:
                                    chiya = []
                                    for rom in read["ROM"][receiver].items():
                                        chiya.append(rom[1])
                                    cmem = k1.getContacts(chiya) 
                                    zx = ""
                                    zxc = ""
                                    zx2 = []
                                    xpesan = '╭━━╦Daftar yang terbaca╦━━╮\n'
                                for x in range(len(cmem)):
                                    xname = str(cmem[x].displayName)
                                    pesan = ''
                                    pesan2 = pesan+"@c\n"
                                    xlen = str(len(zxc)+len(xpesan))
                                    xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                    zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                    zx2.append(zx)
                                    zxc += pesan2
                                text = xpesan+ zxc + "\n" + readTime
                                try:
                                    k1.sendMessage(receiver, text, contentMetadata={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}, contentType=0)
                                except Exception as error:
                                    print (error)
                                pass
                            else:
                                k1.sendMessage(receiver,"Lurking has not been set.")
#======================================
#====================#
                        elif satria.startswith("addimage "):
                            load()
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in images:
                                settings["addImage"]["status"] = True
                                settings["addImage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open('image.json','w','utf-8')
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                k1.sendMessage(to, "Silahkan kirim gambar yang ingin anda tambahkan")
                            else:
                                k1.sendMessage(to, "Gambar sudah ada dalam list")
                        elif satria.startswith("delimage "):
                            load()
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in images:
                                k1.deleteFile(images[str(name.lower())])
                                del images[str(name.lower())]
                                f = codecs.open('image.json','w','utf-8')
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                k1.sendMessage(to, "Berhasil menghapus gambar {}".format(str(name.lower())))
                            else:
                                k1.sendMessage(to, "Gambar tidak ada dalam list")
                        elif koplaxs.startswith("setimage "):
                            load()
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in images:
                                settings["addImage"]["status"] = True
                                settings["addImage"]["name"] = str(name.lower())
                                images[str(name.lower())] = ""
                                f = codecs.open('image.json','w','utf-8')
                                json.dump(images, f, sort_keys=True, indent=4, ensure_ascii=False)
                                k1.sendMessage(to, "Silahkan kirim gambar yang ingin anda ubah")
                            else:
                                k1.sendMessage(to, "Gambar tidak ada dalam list")
                        elif koplaxs == "imagelist":
                            load()
                            ret_ = "╔══[ List Images ]"
                            for image in images:
                                ret_ += "\n╠ " + image.title()
                            ret_ += "\n╚══[ Total {} Images ]".format(str(len(images)))
                            k1.sendMessage(to, ret_)
                        elif satria.startswith("spamimage "):
                            load()
                            sep = text.split(" ")
                            text = text.replace(sep[0] + " ","")
                            cond = text.split(" ")
                            jml = int(cond[0])
                            imagename = text.replace(cond[0] + " ","").lower()
                            if imagename in images:
                                imgURL = images[imagename]
                            else:
                                k1.sendMessage(to, "Gambar tidak ditemukan")
                                return
                            for x in range(jml):
                                k1.sendImage(to, imgURL)
                        elif koplaxs.startswith("addsticker "):
                            load()
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name not in stickers:
                                settings["addSticker"]["status"] = True
                                settings["addSticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = {}
                                f = codecs.open('sticker.json','w','utf-8')
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                k1.sendMessage(to, "Silahkan kirim stiker yang ingin anda tambahkan")
                            else:
                                k1.sendMessage(to, "Nama stiker sudah ada dalam list")
                        elif koplaxs.startswith("delsticker "):
                            load()
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in stickers:
                                del stickers[str(name.lower())]
                                f = codecs.open('sticker.json','w','utf-8')
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                k1.sendMessage(to, "Berhasil menghapus stiker {}".format(str(name.lower())))
                            else:
                                k1.sendMessage(to, "Stiker tidak ada dalam list")
                        elif satria.startswith("setsticker "):
                            load()
                            sep = text.split(" ")
                            name = text.replace(sep[0] + " ","")
                            name = name.lower()
                            if name in stickers:
                                settings["addSticker"]["status"] = True
                                settings["addSticker"]["name"] = str(name.lower())
                                stickers[str(name.lower())] = ""
                                f = codecs.open('sticker.json','w','utf-8')
                                json.dump(stickers, f, sort_keys=True, indent=4, ensure_ascii=False)
                                k1.sendMessage(to, "Silahkan kirim stiker yang ingin anda ubah")
                            else:
                                k1.sendMessage(to, "Stiker tidak ada dalam list")
                        elif satria == "stickerlist":
                            load()
                            ret_ = "╔══[ List Sticker ]"
                            for sticker in stickers:
                                ret_ += "\n╠ " + sticker.title()
                            ret_ += "\n╚══[ Total {} Stickers ]".format(str(len(stickers)))
                            k1.sendMessage(to, ret_)
                        elif satria.startswith("spamsticker "):
                            load()
                            sep = text.split(" ")
                            text = text.replace(sep[0] + " ","")
                            cond = text.split(" ")
                            jml = int(cond[0])
                            stickername = text.replace(cond[0] + " ","").lower()
                            if stickername in stickers:
                                sid = stickers[stickername]["STKID"]
                                spkg = stickers[stickername]["STKPKGID"]
                                sver = stickers[stickername]["STKVER"]
                            else:
                                return
                            for x in range(jml):
                                sendSticker(to, sver, spkg, sid)
#=====================================
                        elif satria.startswith("kick "):
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        wait["blacklist"][ls] = True
                                        berak = [k1]
                                        berakin = random.choice(berak)
                                        berakin.kickoutFromGroup(to,[ls])
                                        print (to,[ls])
                                    except:
                                        try:
                                            wait["blacklist"][ls] = True
                                            berak = [k1]
                                            berakin = random.choice(berak)
                                            berakin.kickoutFromGroup(to,[ls])
                                            print (to,[ls])
                                        except:
                                            pass
#=====================================#
                        elif satria.startswith("friend "):
                          if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        k1.sendMessage(to,"Mencoba Menambakan Teman")
                                        k1.findAndAddContactsByMid(ls)
                                        k1.findAndAddContactsByMid(ls)
                                        k1.findAndAddContactsByMid(ls)
                                        k1.findAndAddContactsByMid(ls)
                                        k1.findAndAddContactsByMid(ls)
                                        k1.findAndAddContactsByMid(ls)
                                        k1.findAndAddContactsByMid(ls)
                                        k1.findAndAddContactsByMid(ls)
                                        k1.findAndAddContactsByMid(ls)
                                        k1.findAndAddContactsByMid(ls)
                                        k1.sendMessage(to,"Sukses")
                                    except:
                                        line.sendMessage(to,"ERROR")
                                
                        elif satria.startswith("unban "):
                          if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        del wait["blacklist"][ls]
                                        k1.sendMessage(to,"Blacklist berhasil dihapus")
                                        print("[Notif] Delete blacklist Success")
                                    except:
                                        k1.sendMessage(to,"Tidak ada dalam daftar blacklist")
                        elif satria.startswith("ban "):
                          if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        wait["blacklist"][ls] = True
                                        k1.sendMessage(to,"Succes.!!")
                                        print("[Notif] menambahkan blacklist Success")
                                    except:
                                        k1.sendMessage(to,"Sudah ada dalam daftar blacklist")
                        elif sattia.startswith("unblock "):
                          if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        del settings["bancet"][ls]
                                        k1.sendMessage(to,"Block berhasil dihapus")
                                        k1.findAndAddContactsByMid(ls)
                                        print("[Notif] Delete blockchat Success")
                                    except:
                                        k1.sendMessage(to,"Tidak ada dalam daftar block")
                        elif satria.startswith("block "):
                          if sender in OWNER:
                            if 'MENTION' in msg.contentMetadata.keys()!= None:
                                names = re.findall(r'@(\w+)', text)
                                mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                                mentionees = mention['MENTIONEES']
                                lists = []
                                for mention in mentionees:
                                    if mention["M"] not in lists:
                                        lists.append(mention["M"])
                                for ls in lists:
                                    try:
                                        settings["bancet"][ls] = True
                                        k1.sendMessage(to,"Succes.!!")
                                        k1.findBlockedContactsByMid(ls)
                                        print("[Notif] menambahkan block Success")
                                    except:
                                        k1.sendMessage(to,"Sudah ada dalam daftar block")
                        elif satria == "banall":
                          if sender in OWNER:
                            if msg.toType == 2:
                                gs = k1.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    k1.sendMessage(to,"Noting member")
                                else:
                                    for target in targets:
                                         if target not in wait["blacklist"] or target not in Bots:
                                            try:
                                                waiy["blacklist"][target] = True
                                                k1.sendMessage(to,"Succes.!!")
                                            except:
                                                pass
                        elif satria == "adminall":
                          if sender in OWNER:
                            if msg.toType == 2:
                                gs = k1.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    k1.sendMessage(to,"Noting member")
                                else:
                                    for target in targets:
                                         if target not in admin or target not in Bots:
                                            try:
                                                admin[target] = True
                                                k1.sendMessage(to,"Succes.!!")
                                            except:
                                                pass
                        elif satria == "unbanall":
                            if msg.toType == 2:
                                gs = k1.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    k1.sendMessage(to,"Tidak ada member terblacklist di grup ini")
                                else:
                                    for target in targets:
                                            try:
                                                del wait["blacklist"][target]
                                                k1.sendMessage(to,"Succes.!!")
                                            except:
                                                pass
                        elif satria == "blockall":
                            if msg.toType == 2:
                                gs = k1.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    k1.sendMessage(to,"Noting member")
                                else:
                                    for target in targets:
                                         if target not in settings["bancet"] or target not in Bots:
                                            try:
                                                settings["bancet"][target] = True
                                                k1.sendMessage(to,"Succes.!!Blocked")
                                            except:
                                                pass
                        elif satria == "unblockall":
                            if msg.toType == 2:
                                gs = k1.getGroup(msg.to)
                                targets = []
                                for g in gs.members:
                                    targets.append(g.mid)
                                targets.remove(mid)
                                if targets == []:
                                    k1.sendMessage(to,"Tidak ada member block di grup ini")
                                else:
                                    for target in targets:
                                            try:
                                                del settings["bancet"][target]
                                                k1.sendMessage(to,"Succes.!!Unblocked")
                                            except:
                                                pass
                        elif satria == "blacklist":
                            wait["blacklist"] = True
                            k1.sendMessage(to, "Silahkan kirim kontak")
                        elif koplaxs == "unblacklist":
                            wait["banDel"] = True
                            k1.sendMessage(to, "Silahkan kirim kontak")
                        elif koplaxs == "banlist":
                                if wait["blacklist"] == {}:
                                    k1.sendMessage(to,"Tidak Ada kontak blacklist")
                                else:
                                    k1.sendMessage(to,"═══════List blacklist═══════")
                                    h = ""
                                    for i in wait["blacklist"]:
                                        h = k1.getContact(i)
                                        k1.sendContact(to,i)
                                        
                        elif msg.text in ["Ownerlist","ownerlist"]:
                          if OWNER == []:
                            k1.sendMessage(msg.to,"The Ownerlist is empty")
                          else:
                            k1.sendMessage(msg.to,"Tunggu...")
                            mc = "╔═══════════════════\n║👑 Owner BotTrox Bot 👑\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                            for mi_d in OWNER:
                              mc += "║[★]" + k1.getContact(mi_d).displayName + "\n"
                            k1.sendMessage(msg.to,mc)
                                        
                        elif msg.text in ["Adminlist","adminlist"]:
                          if admin == []:
                            k1.sendMessage(msg.to,"The Adminlist is empty")
                          else:
                            k1.sendMessage(msg.to,"Tunggu...")
                            mc = "╔═══════════════════\n║👑 Admin BotTrox Bot 👑\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                            for mi_d in admin:
                              mc += "║[★]" + k1.getContact(mi_d).displayName + "\n"
                            k1.sendMessage(msg.to,mc)
                            
                        elif msg.text in ["Stafflist","stafflist"]:
                          if staff == []:
                            k1.sendMessage(msg.to,"The Stafflist is empty")
                          else:
                            k1.sendMessage(msg.to,"Tunggu...")
                            mc = "╔═══════════════════\n║👑 Staff BotTrox Bot 👑\n║𖤓≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛≛𖤓\n"
                            for mi_d in staff:
                              mc += "║[★]" + k1.getContact(mi_d).displayName + "\n"
                            k1.sendMessage(msg.to,mc)
                                        
                        elif satria == "adminlist2":
                          if sender in admin:
                                if admin == {}:
                                    k1.sendMessage(to,"NOTING ADMIN..")
                                else:
                                    k1.sendMessage(to,"═══════List Admin═══════")
                                    h = ""
                                    for i in admin:
                                        h = k1.getContact(i)
                                        k1.sendContact(to,i)
                        elif satria == "blocklist":
                                if settings["bancet"] == {}:
                                    k1.sendMessage(to,"Tidak Ada kontak blocklist")
                                else:
                                    k1.sendMessage(to,"═══════List blockchat═══════")
                                    h = ""
                                    for i in settings["bancet"]:
                                        h = k1.getContact(i)
                                        k1.sendContact(to,i)
                        elif satria == "clearban":
                          if sender in OWNER:
                            wait["blacklist"] = {}
                            k1.sendMessage(to,"done all deleted blacklist")
                            k1.sendMessage(to,"succes.!!")
                            
                        elif satria == "clearadmin":
                          if sender in OWNER:
                            settings["admin"] = {}
                            k1.sendMessage(to,"done all deleted admin")
                        elif koplaxs == "clearblock":
                          if sender in OWNER:
                            settings["bancet"] = {}
                            k1.sendMessage(to,"done all deleted blocked")
                        elif satria == "clearchat":
                          if sender in OWNER:
                            k1.removeAllMessages(op.param2)
                            k1.removeAllMessages(op.param2)
                            k1.sendMessage(to, "Berhasil hapus semua chat")
                        elif satria.startswith("sendgrup "):
                          if sender in OWNER:
                            sep = text.split(" ")
                            txt = text.replace(sep[0] + " ","")
                            groups = k1.groups
                            for group in groups:
                                sendMessageWithFooter(group, "╭━━━━━╦BroadCast by ONE PIECE TEAM╦━━━━━╮\n{}".format(str(txt)))
                            k1.sendMessage(to, "Berhasil broadcast ke {} group".format(str(len(groups))))
                                

                        elif satria.startswith("gname "):
                          if sender in OWNER:
                            if msg.toType == 2:
                                X = k1.getGroup(to)
                                sep = msg.text.split(" ")
                                X.name = msg.text.replace(sep[0] + " ","")
                                k1.updateGroup(X)
                                
                        elif satria == "gruplist":
                            groups = k1.groups
                            ret_ = "╭━━━━━══[ Group List ]══━━━━━╮"
                            no = 0 + 1
                            for gid in groups:
                                group = k1.getGroup(gid)
                                ret_ += "\n┣═ {}. {} ┣═Member: {}".format(str(no), str(group.name), str(len(group.members)))
                                no += 1
                            ret_ += "\n╰━━━━━══[ Total {} Groups ]════━━━━━".format(str(len(groups)))
                            k1.sendMessage(to, str(ret_))
                        elif satria == "friendlist":
                            contactlist = k1.getAllContactIds()
                            kontak = k1.getContacts(contactlist)
                            num=1
                            msgs="╭━━━━━══[ Friend List ]══━━━━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n━━━━━══[ Friend Result ]══━━━━━\nTotal : %i" % len(kontak)
                            k1.sendMessage(to, msgs)
                                
                        elif satria == "friendblocklist":
                            blockedlist = k1.getBlockedContactIds()
                            kontak = k1.getContacts(blockedlist)
                            num=1
                            msgs="╭━━━━━══[ Friend Block ]══━━━━━╮"
                            for ids in kontak:
                                msgs+="\n[%i] %s" % (num, ids.displayName)
                                num=(num+1)
                            msgs+="\n━━━━━══[ Block Result ]══━━━━━\nBlock Total : %i" % len(kontak)
                            k1.sendMessage(to, msgs)
                        elif satria == "gcreator":
                            k1.sendMessage(to, "━━━━══[Pembuat Grup]══━━━━")
                            group = k1.getGroup(to)
                            GS = group.creator.mid
                            k1.sendContact(to, GS)
                            k1.sendMessage(to, "━━━━══━━╩━━══━━━━")
                        elif koplaxs == "memberlist":
                          if sender in admin:
                            if msg.toType == 2:
                                    group = k1.getGroup(to)
                                    ret_ = "╭━━━══[ Member List ]"
                                    no = 0 + 1
                                    for mem in group.members:
                                        ret_ += "\n┣═ {}. {}".format(str(no), str(mem.displayName))
                                        no += 1
                                    ret_ += "\n╰━━━══[ Total {} member]".format(str(len(group.members)))
                                    k1.sendMessage(to, str(ret_))
                                
                        elif satria == "pendinglist":
                            if sender in OWNER:
                                if msg.toType == 2:
                                    group = k1.getGroup(to)
                                    ret_ = "╭━━━══[ Pending List ]"
                                    no = 0 + 1
                                    if group.invitee is None or group.invitee == []:
                                        k1.sendMessage(to, "Tidak ada pendingan")
                                        return
                                    else:
                                        for pen in group.invitee:
                                            ret_ += "\n┣═ {}. {}".format(str(no), str(pen.displayName))
                                            no += 1
                                        ret_ += "\n╰━━━══[ Total {} tertunda]".format(str(len(group.invitee)))
                                        k1.sendMessage(to, str(ret_))
                        
                        elif satria == "ginfo":
                            if sender in admin:
                                group = k1.getGroup(to)
                                try:
                                    gCreator = group.creator.displayName
                                except:
                                    gCreator = "Tidak ditemukan"
                                if group.invitee is None:
                                    gPending = "0"
                                else:
                                    gPending = str(len(group.invitee))
                                if group.preventedJoinByTicket == True:
                                    gQr = "Closed"
                                    gTicket = "Qr tidak tersedia karna di tutup"
                                else:
                                    gQr = "Open"
                                    gTicket = "https://line.me/R/ti/g/{}".format(str(k1.reissueGroupTicket(group.id)))
                                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                                ret_ = "╭━━━━══[ Group Info ]"
                                ret_ += "\n┣═Nama Group : {}".format(str(group.name))
                                ret_ += "\n┣═ID Group : {}".format(group.id)
                                ret_ += "\n┣═Pembuat : {}".format(str(gCreator))
                                ret_ += "\n┣═Jumlah Member : {}".format(str(len(group.members)))
                                ret_ += "\n┣═Jumlah Pending : {}".format(gPending)
                                ret_ += "\n┣═━━━Kode Qr/Link━━━═"
                                ret_ += "\n┣═Group Ticket : {}".format(gTicket)
                                ret_ += "\n┣═Group Qr : {}".format(gQr)
                                ret_ += "\n╰━━━━══[ CREATOR   B O T T R O X.  B O T]"
                                k1.sendMessage(to, str(ret_))
                            
                        elif satria == "gpict":
                          if sender in admin:
                            group = k1.getGroup(to)
                            path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            k1.sendImageWithURL(to, path)
                        elif satria == "gname":
                          if sender in admin:
                            gid = k1.getGroup(to)
                            k1.sendMessage(to, "[Nama Group : ]\n" + gid.name)
                        elif koplaxs == "gid":
                          if sender in admin:
                            gid = k1.getGroup(to)
                            k1.sendMessage(to,gid.id)
                        elif satria == "gurl":
                          if sender in admin:
                            if msg.toType == 2:
                                group = k1.getGroup(to)
                                if group.preventedJoinByTicket == False:
                                    ticket = k1.reissueGroupTicket(to)
                                    k1.sendMessage(to, "https://line.me/R/ti/g/{}".format(str(ticket)))
                                else:
                                    group.preventedJoinByTicket = False
                                    k1.updateGroup(group)
                                    k1.sendMessage(to, "https://line.me/R/ti/g/{}".format(str(ticket)))
                        elif msg.text in ["Buka qr","buka qr"]:
                         if msg._from in admin:
                            if msg.toType == 2:
                                group = k1.getGroup(to)
                                if group.preventedJoinByTicket == False:
                                    k1.sendMessage(to, "Sudah terbuka")
                                else:
                                    group.preventedJoinByTicket = False
                                    k1.updateGroup(group)
                                    k1.sendMessage(to, "Berhasil membuka Qr")
                        elif msg.text in ["Tutup qr","tutup qr"]:
                         if msg._from in admin:
                            if msg.toType == 2:
                                group = k1.getGroup(to)
                                if group.preventedJoinByTicket == True:
                                    k1.sendMessage(to, "Sudah tertutup")
                                else:
                                    group.preventedJoinByTicket = True
                                    k1.updateGroup(group)
                                    k1.sendMessage(to, "Berhasil menutup Qr")
#==============================================================================#
                        elif satria == "set":
                          if sender in admin:
                            try:
                                ret_ = "╭━━╦̰̰̈́𖤓B o t T r o x   B o t𖤓╦━━╮\n┣━━━━Status Proteksi━━━━"
                                if wait["Protectkick"] == True: ret_ += "\n┣━╣ Protect Kick Enable✔"
                                else: ret_ += "\n┣━╣ Protect Kick Disable❌"
                                if wait["ProtectInvite"] == True: ret_ += "\n┣━╣ Protect Invite Enable✔"
                                else: ret_ += "\n┣━╣ Protect Invite Disable❌"
                                if wait["ProtectQR"] == True: ret_ += "\n┣━╣ Protect QR Enable✔"
                                else: ret_ += "\n┣━╣ Protect QR Disable❌"
                                if wait["Protectcancel"] == True: ret_ += "\n┣━╣ Protect Cancel Enable✔"
                                else: ret_ += "\n┣━╣ Protect Cancel Disable❌"
                                if wait["autoAdd"] == True: ret_ += "\n┣━╣ AutoAdd Enable✔"
                                else: ret_ += "\n┣━╣ AutoAdd Disable❌"
                                if wait["contact"] == True: ret_ += "\n┣━╣ Contact  Enable✔"
                                else: ret_ += "\n┣━╣ Contact  Disable❌"
                                if wait["AddFriend"] == True: ret_ += "\n┣━╣ Add Friend  Enable✔"
                                else: ret_ += "\n┣━╣ Add Friend  Disable❌"
                                ret_ += "\n┣━━━━━━━━━━━━━━━━━\n╰━╩𖤓B o t T r o x   B o t𖤓╩━╯"
                                k1.sendMessage(to, str(ret_))
                                k1.sendContact(to, k1MID)
                            except Exception as e:
                                k1.sendMessage(to, str(e))
                                k1.sendContact(to, k1MID)
                                
                        elif satria == "friend:on":
                          if sender in OWNER:
                            wait["AddFriend"] = True
                            k1.sendMessage(to, "Kirim Kontaknya Boss")
                            
                        elif satria == "friend:on":
                          if sender in OWNER:
                            wait["AddFriend"] = False
                            k1.sendMessage(to, "Kirim Kontaknya Boss")
                                
                        elif satria == "autoadd:on":
                          if sender in OWNER:
                            settings["autoAdd"] = True
                            k1.sendMessage(to, "Already on")
                        elif satria == "autoadd:off":
                            settings["autoAdd"] = False
                            k1.sendMessage(to, "Already off")
                        elif satria == "autojoin:on":
                            wait["autoJoin"] = True
                            k1.sendMessage(to, "Already on")
                        elif satria == "autojoin:off":
                            wait["autoJoin"] = False
                            k1.sendMessage(to, "Already off")
                        elif satria == "sambutan:on":
                            if msg.to in settings["SAMBUT"]:
                                k1.sendMessage(to, "Already on")
                            else:
                                k1.sendMessage(to, "Sudah on")
                                settings["SAMBUT"][msg.to] = True
                        elif satria == "sambutan:off":
                            if msg.to in settings["SAMBUT"]:
                                k1.sendMessage(to, "Already off")
                                del settings["SAMBUT"][msg.to]
                            else:
                                k1.sendMessage(to, "Sudah off")
                        elif satria == "respon:on":
                            settings["detectMention"] = True
                            k1.sendMessage(to, "Already on")
                        elif satria == "respon:off":
                            settings["detectMention"] = False
                            k1.sendMessage(to, "Already off")
                        elif satria == "jointicket:on":
                            settings["autoJoinTicket"] = True
                            k1.sendMessage(to, "Already on")
                        elif satria == "jointicket:off":
                            settings["autoJoinTicket"] = False
                            k1.sendMessage(to, "Already off")
                            
                        elif msg.text in ["Contact On","Contact on","contact on"]:
                         if msg._from in OWNER:
                          if wait["contact"] == True:
                           if wait["lang"] == "JP":
                            k1.sendMessage(msg.to,"Cek Mid Lewat Share Kontak On")
                           else:
                            k1.sendMessage(msg.to,"done")
                          else:
                           wait["contact"] = True
                           if wait["lang"] == "JP":
                            k1.sendMessage(msg.to,"Cek Mid Lewat Share Kontak On")
                           else:
                            k1.sendMessage(msg.to,"done")
                            
                        elif msg.text in ["Contact Off","Contact off","contact off"]:
                         if msg._from in OWNER:
                          if wait["contact"] == False:
                           if wait["lang"] == "JP":
                            k1.sendMessage(msg.to,"Cek Mid Lewat Share Kontak Off")
                           else:
                            k1.sendMessage(msg.to,"done")
                          else:
                           wait["contact"] = False
                           if wait["lang"] == "JP":
                            k1.sendMessage(msg.to,"Cek Mid Lewat Share Kontak Off")
                           else:
                            k1.sendMessage(msg.to,"done")
                            
                        elif satria == "contact:on":
                            settings["checkContact"] = True
                            k1.sendMessage(to, "Already on")
                        elif satria == "contact:off":
                            settings["checkContact"] = False
                            k1.sendMessage(to, "Already off")
                        elif satria == "share:on":
                            settings["checkPost"] = True
                            k1.sendMessage(to, "Already on")
                        elif satria == "share:off":
                            settings["checkPost"] = False
                            k1.sendMessage(to, "Already off")
                        elif satria == "autoread:on":
                            settings["autoRead"] = True
                            k1.sendMessage(to, "Already on")
                        elif satria == "autoread:off":
                            settings["autoRead"] = False
                            k1.sendMessage(to, "Already off")
                        elif satria == "unsend:on":
                            settings["unsendMessage"] = True
                            k1.sendMessage(to, "Already on")
                        elif satria == "unsend:off":
                            settings["unsendMessage"] = False
                            k1.sendMessage(to, "Already off")
#===============================================================
                        elif satria == "list protect":
                                pli = ""
                                pme = ""
                                pna = ""
                                pin = ""
                                a = 0
                                b = 0
                                c = 0
                                d = 0
                                gid = Prolink
                                for group in gid:
                                    a = a + 1
                                    end = '\n'
                                    pli += str(a) + ". " +k1.getGroup(group).name + "\n"
                                gid = PROTECT
                                for group in gid:
                                    b = b + 1
                                    end = '\n'
                                    pme += str(b) + ". " +k1.getGroup(group).name + "\n"
                                gid = Proname
                                for group in gid:
                                    d = d + 1
                                    end = '\n'
                                    pna += str(d) + ". " +k1.getGroup(group).name + "\n"
                                gid = Proinvite
                                for group in gid:
                                    c = c + 1
                                    end = '\n'
                                    pin += str(c) + ". " +k1.getGroup(group).name + "\n"
                                k1.sendMessage(msg.to,"╭━━╦̰̰̈́𖤓B O T T R O X   B O T𖤓╦━━╮\n┣━╣PROTECT LINK:: "+pli+"\n┣━╣PROTECTION:: "+pme+"\n┣━╣PROTECT NAME:: "+pna+"\n┣━╣PROTECT INVITE:: "+pin+"\n╰━╩TOTAL %s PRO GROUPS╩━╯" %(str(len(Prolink)+len(PROTECT)+len(Proname)+len(Proinvite))))
                        elif satria == "Namelock:on":
                          if sender in admin:
                            if msg.to in wait['pname']:
                              k1.sendMessage(msg.to,"ƬƲƦƝЄƊ ƠƝ.")
                            else:
                              k1.sendMessage(msg.to,"ƛԼƦЄƛƊƳ ƠƝ")
                              wait['pname'][msg.to] = True
                              wait['pro_name'][msg.to] = k1.getGroup(msg.to).name
                          else:
                            k1.sendMessage(msg.to,"Just For Admin")
                        elif satria == "Namelock:off":
                          if sender in admin:
                            if msg.to in wait['pname']:
                              k1.sendMessage(msg.to,"ƬƲƦƝ ƠƑƑ.")
                              del wait['pname'][msg.to]
                            else:
                              k1.sendMessage(msg.to,"ƛԼƦЄƛƊƳ ƠƑƑ")
                          else:
                            k1.sendMessage(msg.to,"Just For Admin")
                            
                        elif "Getline " in msg.text:
                          if sender in admin:
                            msgg = msg.text.replace("Getline ",'')
                            conn = k1.findContactsByUserid(msgg)
                            if True:
                              k1.sendContact(to, conn.mid)
                              k1.sendMessage(to,"http://k1.me/ti/p/~" + msgg)
                        elif "Cekmid " in msg.text:
                          if sender in admin:
                            mmid = msg.text.replace("Cekmid ","")
                            h = k1.getContact(mmid)
                            k1.sendMessage(to, h.displayName)
                            k1.sendImageWithURL(to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                            k1.sendContact(to, mmid)
                            
                        elif "Getcontact " in msg.text:
                          if msg._from in OWNER:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]                
                            mmid = k1.getContact(key1)
                            k1.sendContact(msg.to,key1)
                        elif "Getname " in msg.text:
                          if msg._from in OWNER:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            contact = k1.getContact(key1)
                            try:
                              k1.sendMessage(msg.to, "══════❴CONTACT NAME❵══════\n" + contact.displayName)
                            except:
                              k1.sendMessage(msg.to, "══════❴CONTACT NAME❵══════\n" + contact.displayName)
                        elif msg.text in ["Myname"]:
                          h = k1.getContact(msg._from)
                          k1.sendMessage(msg.to, "══════❴YOUR.NAME❵══════\n" + h.displayName)
                        elif msg.text in ["Mybio"]:
                          if msg._from in admin:
                            h = k1.getContact(msg._from)
                            k1.sendMessage(msg.to, "══════❴YOUR.STATUS❵══════\n" + h.statusMessage)
                        elif msg.text in ["Mypict"]:
                          if msg._from in admin:
                            h = k1.getContact(msg._from)
                            k1.sendMessage(msg.to, "══════❴YOUR.PICTURES❵══════")
                            k1.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                        elif msg.text in ["Myvid"]:
                          if msg._from in admin:
                            h = k1.getContact(msg._from)
                            k1.sendMessage(msg.to, "══════❴YOUR.VIDEO PICTURES❵══════")
                            k1.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                        elif msg.text in ["Urlpict"]:
                          if msg._from in admin:
                            h = k1.getContact(msg._from)
                            k1.sendMessage(msg.to, "══════❴YOUR.URL.PICTURES❵══════")
                            k1.sendMessage(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
                        elif "Getmid @" in msg.text:
                          if msg._from in admin:
                            _name = msg.text.replace("Getmid @","")
                            _nametarget = _name.rstrip(' ')
                            gs = k1.getGroup(msg.to)
                            for g in gs.members:
                              if _nametarget == g.displayName:
                                k1.sendMessage(msg.to, g.mid)
                          else:
                            pass
                        elif "Getinfo" in msg.text:
                          if msg._from in admin:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            contact = k1.getContact(key1)
                            try:
                              k1.sendMessage(msg.to,"🎀═displayName═🎀\n✤[" + contact.displayName + "]✤\n🎀═MIDs═🎀\n✤[" + contact.mid + "]✤\n🎀═StatusContact═🎀\n✤" + contact.statusMessage + "✤")
                            except:
                              k1.sendMessage(msg.to,"🎀═displayName═🎀\n✤[" + contact.displayName + "]✤\n🎀═MIDs═🎀\n✤[" + contact.mid + "]✤\n🎀═StatusContact═🎀\n✤" + contact.statusMessage + "✤")
                              
                        elif "Getbio" in msg.text:
                          if msg._from in admin:
                            key = eval(msg.contentMetadata["MENTION"])
                            key1 = key["MENTIONEES"][0]["M"]
                            contact = k1.getContact(key1)
                            cu = k1.channel.getCover(key1)
                            try:
                              k1.sendMessage(msg.to,contact.statusMessage)
                            except:
                              k1.sendMessage(msg.to,contact.statusMessage)
                        elif "Gimage" in msg.text:
                          if msg._from in admin:
                            group = k1.getGroup(msg.to)
                            path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                            k1.sendImageWithURL(msg.to,path)
                        elif "Getpict @" in msg.text:
                          if msg._from in admin:
                            _name = msg.text.replace("Getpict @","")
                            _nametarget = _name.rstrip('  ')
                            gs = k1.getGroup(msg.to)
                            targets = []
                            for g in gs.members:
                              if _nametarget == g.displayName:
                                targets.append(g.mid)
                            if targets == []:
                              k1.sendMessage(msg.to,"Contact not found")
                            else:
                              for target in targets:
                                try:
                                  contact = k1.getContact(target)
                                  path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                  k1.sendImageWithURL(msg.to, path)
                                except:
                                  pass
                                  
                        elif "Me" == msg.text:
                          tz = pytz.timezone("Asia/Jakarta")
                          timeNow = datetime.now(tz=tz)
                          day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                          hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                          bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                          hr = timeNow.strftime("%A")
                          bln = timeNow.strftime("%m")
                          for i in range(len(day)):
                            if hr == day[i]: hasil = hari[i]
                          for k in range(0, len(bulan)):
                             if bln == str(k): bln = bulan[k-1]
                          rst = hasil + ", " + timeNow.strftime('%d') + " - " + bln + " - " + timeNow.strftime('%Y') + "\nJam : [ " + timeNow.strftime('%H:%M:%S') + " ]"
                          k1.sendContact(msg.to,msg._from)
                          k1.sendMessage(msg.to,rst)
                          
                        elif msg.text in ["Clearban"]:
                          if msg._from in OWNER:
                            wait["blacklist"] = {}
                            k1.sendMessage(to,"done all deleted blacklist")
                            
                        elif "Bangsat" in msg.text:
                          if msg._from in OWNER:
                            if msg.toType == 2:
                              #print "Ratain"
                              _name = msg.text.replace("Bangsat","")
                              gs = k1.getGroup(msg.to)
                              targets = []
                              for g in gs.members:
                                if _name in g.displayName:
                                  targets.append(g.mid)
                              if targets == []:
                                k1.sendMessage(msg.to,"Not found")
                              else:
                                for target in targets:
                                  if target in admin:
                                    pass
                                  elif target in Bots:
                                    pass
                                  elif target in staff:
                                    pass
                                  else:
                                    try:
                                      klist=[k1]
                                      kicker=random.choice(klist)
                                      kicker.kickoutFromGroup(msg.to,[target])
                                      #print (msg.to,[g.mid])
                                    except:
                                      try:
                                        k1.kickoutFromGroup(msg.to,[target])
                                      except:
                                        random.choice(KAC).kickoutFromGroup(msg.to,[target])
#====================#
        if op.type == 55:
          try:
            group_id = op.param1
            user_id=op.param2
            subprocess.Popen('echo "'+ user_id+'|'+str(op.createdTime)+'" >> dataSeen/%s.txt' % group_id, shell=True, stdout=subprocess.PIPE, )
          except Exception as e:
              print (e)
              
        if op.type == 55:
                try:
                    if cctv['cyduk'][op.param1]==True:
                        if op.param1 in cctv['point']:
                          if op.param2 in OWNER:
                            pass
                          else:
                            Name = k1.getContact(op.param2).displayName
                            Np = k1.getContact(op.param2).pictureStatus
                            #Kontol = k1.getContact(op.param2).mid
                            if Name in cctv['sidermem'][op.param1]:
                                pass
                            else:
                                cctv['sidermem'][op.param1] += "\n• " + Name
                                if " " in Name:
                                    nick = Name.split(' ')
                                    if len(nick) == 2:
                                        #k1.sendMessage(op.param1, "Woy " + "☞ " + nick["@x"]+ " ☜" + "\nDasar Cicitipi")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                        k1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                        k1.mention(op.param1, [op.param2])
                                        #mentionMembers(to, [Kontol])
                                    else:
                                       # k1.sendMessage(op.param1, "Woy " + "☞ " + nick["@x"] + " ☜" + "\nBetah Banget Jadi Cicitipi. . .\nChat Woy (-__-)   ")
                                        time.sleep(0.2)
                                        summon(op.param1,[op.param2])
                                        k1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                        k1.mention(op.param1, [op.param2])
                                        #mentionMembers(to, [Kontol])
                                else:
                                    #k1.sendMessage(op.param1, "Jiahahaha " + "☞ " + nick["@x"] + " ☜" + "\nNgapain Cicitipi Doang???\nGa Gaul Lu ga Mau Chat\nPasti Temennya Dikit ")
                                    time.sleep(0.2)
                                    summon(op.param1,[op.param2])
                                    k1.sendImageWithURL(op.param1, "http://dl.profile.line-cdn.net/" + Np)
                                    k1.mention(op.param1, [op.param2])
                                    #mentionMembers(to, [Kontol])
                        else:
                            pass
                    else:
                        pass
                except:
                    pass
        else:
            pass
                                
        if op.type == 65:
            print ("[ 65 ] NOTIFIED DESTROY MESSAGE")
            if settings["unsendMessage"] == True:
                try:
                    at = op.param1
                    msg_id = op.param2
                    if msg_id in msg_dict:
                        if msg_dict[msg_id]["from"]:
                            contact = k1.getContact(msg_dict[msg_id]["from"])
                            if contact.displayNameOverridden != None:
                                name_ = contact.displayNameOverridden
                                name_ = contact.displayName
                                mention = str(nama_)
                            else:
                                ret_ = "Send Message cancelled."
                           #     ret_ += "\nSend At : {}".format(str(dt_to_str(cTime_to_datetime(msg_dict[msg_id]["createdTime"]))))
                                ret_ += "\nType : {}".format(str(Type._VALUES_TO_NAMES[msg_dict[msg_id]["contentType"]]))
                                ret_ += "\nText : {}".format(str(msg_dict[msg_id]["text"]))
                                ret_ += "\n_____________UNSEND DONE______________"
                          #      sendMention(at, mention)
                                k1.sendMessage(at, str(ret_))
                            del msg_dict[msg_id]
                        else:
                            k1.sendMessage(at,"SentMessage cancelled,But I didn't have log data.\nSorry > <")
                            print("unsend aktiv")
                except Exception as error:
                    logError(error)
                    traceback.print_tb(error.__traceback__)
                    
        #if op.type == 17:
          #ginfo = k1.getGroup(op.param1)
          #cp = k1.getContact(op.param2)
         # k1.sendImageWithURL(op.param1,"http://dl.profile.line-cdn.net/" + cp.pictureStatus)
          #k1.sendMessage(op.param1, "Ｓｅｌａｍａｔ Ｄａｔａｎｇ ❲" + str(cp.displayName) + "❳\nＤｉ Ｇｒｏｕｐ ❲ " + str(ginfo.name) +"❳\nBudayakan Baca Note\nSemoga Betah^o^\nKalo Ga Betah Ya Di Betah²in Aja Lah Njiir :v")
                    
        if op.type == 26:
          msg = op.message
          if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True: 
                    msg.text.replace("@"+k1.getProfile().displayName,"")
                    contact = k1.getContact(msg._from)
                    cName = contact.displayName
                    #balas = [cName + "\nDᴏɴᴛ Tᴀɢ Mᴇ!! Cɪᴘᴏᴋ Lᴏʜ Nᴀɴᴛɪ"]
                    #balas = ["Kenapa Tag Si "+k1.getProfile().displayName+"Kangen yah..!!!\nPC aja langsung ownernya biar anu hihi..!!\n[autoRespon]","Nah ngetag lagi si "+k1.getProfile().displayName+" mending ajak mojok aja ownernya dari pada ngetag mulu.. wkwk...!!!\n[autoRespon]"]
                    balas = [cName + "\n[Auto Respon]\nAda Apa? \nKoplaxs Lagi Sibuk!! ",cName + "\n[Auto Respon]\nKoplaxs nya Lagi Kojum",cName + "\n[Auto Respon]\nJones Ngetag²!",cName + "\n[Auto Respon]\nSorry \nIm Busy",cName + "\n[Auto Respon]\nNah Tag Gw Ngajak Desah Ya...!!",cName + "\n[Auto Respon]\nNgajak Desah Ya???"]
                    path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus                
                    ret_ = random.choice(balas)
                    name = re.findall(r'@(\w+)', msg.text)
                    mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                    mentionees = mention['MENTIONEES']
                    for mention in mentionees:
                      if mention['M'] in Bots:
                        k1.sendMessage(msg.to,ret_)
                        #cl.mention(op.param1, [contact.mid])
                        k1.sendImageWithURL(msg.to,path)
                        #msg.contentType = 7    
                        #msg.text = None
                        #msg.contentMetadata = {'STKID': '23643092',
                        #  'STKPKGID': '1738223',
                        #  'STKVER': '1'}                                  
                        k1.sendMessage(msg)
                        break
                
#====================================
    except Exception as error:
        logError(error)
        
        if op.type == 59:
            print (op)
#==============================================================================#
while True:
    try:
      ops=oepoll.singleTrace(count=50)
      if ops != None:
        for op in ops: 
          bot(op)
          oepoll.setRevision(op.revision)
        
    except Exception as e:
        k1.log("[SINGLE_TRACE] ERROR : " + str(e))
