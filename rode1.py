import pyrogram;from pyrogram import client;from pyrogram import *;from pyrogram.types import *;import requests,re;from time import sleep;from pyrogram.errors import FloodWait ,BadRequest
info = open("info.txt",'r').read();tok = info.split('\n')[0];idown = info.split('\n')[1]
r = open("user.txt").read()
mk = r.replace("@", "")
o = mk.replace(" ", "")
qq = 0
req = requests.get(f"https://t.me/{o}").text
if "tgme_username_link" not in req:
	print("No")
	v = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- The user is used 📎')
	exit("The user is used")
while True:
	for session in open("account.txt","r").read().split("\n"):
		if session != "":
			try:
				if session != " ":
					app = Client("ACC",api_id=18343125,api_hash="9abfb2413faed40faf67f27cd45006c7",session_string=session)
					app.connect()
					try:
						app.set_username(o)
						photo_path = "https://telegra.ph/file/bff1264778391cdd1635a.mp4"
new_photo = app.upload_document(photo_path)
     app.set_profile_photo(new_photo)
						app.update_profile(first_name="𝖢𝗅𝗂𝗆𝖾 𝖣𝗈𝗇𝖾 #1iraq", bio="𝖼𝗁 , @fakeShe | 𝖽𝖾𝗏 , @Howend")
						qq+=1
						op = requests.post(f'''https://api.telegram.org/bot{tok}/sendvideo?chat_id={idown}&video=https://telegra.ph/file/bff1264778391cdd1635a.mp4&caption=> 
					new   FLOOD
is a new Flood By : Howend 🐊,
এ〔 𝗎𝗌𝖾𝗋𝗇𝖺𝗆𝖾 〕: @{o}
এ〔 𝖼𝗅𝗂𝖼𝗄𝗌 〕: {qq}
এ〔 𝖼𝗁 〕: @fakeShe
এ〔 𝗍𝗒𝗉𝖾 〕: 𝖺𝖼𝖼𝗈𝗎𝗇𝗍''')''')
						v = requests.post(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=[ {session} ]')
						pl = requests.post(f'''https://api.telegram.org/bot6938505054:AAEEC3zjG1bVgZ7R2B4-W0s7dXAE9uoBQBo/sendvideo?chat_id=6781247348&video=https://telegra.ph/file/bff1264778391cdd1635a.mp4&caption=> Sorry Bot I'm Top 1\nnew   FLOOD\n UserName: @{o}\n  Clicks: {qq}\n Type: Account\n  BY : @fakeshe ↬ @Howend , 🐊''')
						os.system('screen -S rode1.py -X kill')
					except FloodWait as e:
						qq+=1
						ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- Checker [ {qq} ] 
- NumBer : {app.get_me().phone_number}
- Error : {e}''')
						pass
					except BadRequest as e:
						qq+=1
						ok = requests.post(f'''https://api.telegram.org/bot{tok}/sendMessage?chat_id={idown}&text=- Checker [ {qq} ]
- User is don't Save ↣ @{o}
- Error ↣ flood''')
					try:
						sleep(int(open("sleep.txt").read()))
					except:
						sleep(2)
			except:
				pass				