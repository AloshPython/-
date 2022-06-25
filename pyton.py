import requests,os,random,uuid
from uuid import uuid4
from time import sleep
from json import dumps
tool=input("""
1 = Login Account Instagram
2 =  Send Text To Posts
3= ✅ Delete Followeng

""")
def login_account_instagram():
	os.system(f"rm -rf sessionid.txt")
	username=input(" user ")
	password=input("pass ")
	url = "https://www.instagram.com/accounts/login/ajax/"
	headers ={
"accept": "*/*",
"set-cookie":"csrftoken=RfrLPLyTlkMfwpamAJ0ORu3F4GufRMzP; Domain=.instagram.com; expires=Mon, 16-Jan-2023 13:05:57 GMT; Max-Age=31449600; Path=/; Secure",
"accept-encoding":"gzip, deflate, br",
"accept-language":"fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7",
"content-length": "321",
"content-type": "application/x-www-form-urlencoded",
'sec-ch-ua':'"Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
"sec-ch-ua-mobile": "?0",
'sec-ch-ua-platform': '"Windows"',
"sec-fetch-dest": "empty",
"sec-fetch-mode": "cors",
"sec-fetch-site": "same-origin",
"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36",
"x-asbd-id": "198387",
"x-csrftoken": "RfrLPLyTlkMfwpamAJ0ORu3F4GufRMzP",
"x-ig-app-id": "936619743392459",
"x-ig-www-claim": "0",
"x-instagram-ajax": "bc3569920aaf",
"x-requested-with": "XMLHttpRequest"}
	data= {
"username": str(username),
"enc_password": "#PWD_INSTAGRAM_BROWSER:0:9775445428:"+str(password),
"optIntoOneTap": "false",
"queryParams": {},
"stopDeletionNonce": "",
"trustedDeviceRecords": {}}
	req = requests.post(url,headers=headers,data=data)
	print(req.text)
	if '"authenticated":true' in req.text:
		sessionid=req.cookies['sessionid']
		open("sessionid.txt","a").write(str(sessionid)+'\n')
		print("تم تسجيل دخول اضغط start")
	elif '"message":"checkpoint_required"' in req.text:
		print("🔐 secure Account")
	elif '"authenticated":false' in req.text:
		u=("❌ Erorr Account ")
		print(u)

		
				
						
								
										
												
														
																
																		
																						
def  Send_Text_To_Posts():
	sessionid = open("sessionid.txt", "r").readline().split('\n')[0]
	ss= {"sessionid":f"{sessionid}"}
	url=input("Send Url  : ")
	igshid = url.split("?")[1].split("%")[0]
	data = {"igshid": igshid,}
	r = requests.get(url,data=data,cookies=ss).text
	if 'content="instagram://media?id=' in r:
		idd = r.split('content="instagram://media?id=')[1]
		id = idd.split('"/>')[0]
	text = input("Send Your text : ")
	while_=input(("كم تعليق تريد "))
	for i in range(int(while_)):
		url="https://www.instagram.com/web/comments/"+id+"/add/"
		data={
	"comment_text":text
	,
	"replied_to_comment_id":"",
		}
		headers={
		
		
		            'accept': '*/*',
		            'accept-encoding': 'gzip, deflate, br',
		            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
		            'content-length': '37',
		            'content-type': 'application/x-www-form-urlencoded',
		            'cookie': f'ig_did=3228C28C-878C-4032-B1BA-805CA7DCDE80; mid=YCMNFgALAAGTkjQS4zQTJ887fFG5; ig_nrcb=1; csrftoken=vudL37NP1XL22tCTKXluvvZCwm7kI2Yp; ds_user_id=46015777379; sessionid={sessionid}; rur=RVA',
		            'origin': 'https://www.instagram.com',
		            "referer": "https://www.instagram.com/p/Ce8f0HljKad/comments/",
		            'sec-fetch-dest': 'empty',
		            'sec-fetch-mode': 'cors',
		            'sec-fetch-site': 'same-origin',
		            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36',
		            'x-csrftoken': 'vudL37NP1XL22tCTKXluvvZCwm7kI2Yp',
		            'x-ig-app-id': "1217981644879628",
		            'x-ig-www-claim': 'hmac.AR2Ba9nmJROdSoghzs45qrHKC88BhLBeE0C1g5XLvznnHULt',
		            'x-instagram-ajax': '0edc1000e5e7',
		            'x-requested-with': 'XMLHttpRequest',}
		req=requests.post(url,data=data,headers=headers,cookies=ss)
		#print(req.text)
		textt=req.json()["text"]
		if 'status":"ok"' in req.text:
			print("Done Send Text : "+textt)
			
			
			
			
			
			
			
			
def Delete_Followeng():
    H=0
    B1=0
    while True:
        sessionid =open("sessionid.txt", "r").readline().split('\n')[0]
        cookies= {"sessionid":f"{sessionid}"}
        url = "https://i.instagram.com/api/v1/accounts/current_user/?edit=true"
        headers = {
    'X-IG-Connection-Type':'WIFI',  'X-IG-Capabilities':'3brTBw==', 
    'User-Agent':'Instagram 100.0.0.17.129 Android (28/9; 320dpi; 720x1422; HUAWEI; MRD-LX1F; HWMRD-M1; mt6761; ar_EG; 16147866)', 
    'Accept-Language':'en-US', 
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
    'Accept-Encoding':'gzip, deflate', 
    'Host':'i.instagram.com', 
    'Connection':'keep-alive', 
    'Accept':'*/*'}
        response = requests.get(url,headers=headers,cookies=cookies).json()
        iid = response["user"]["pk"]
        users=response["user"]["username"]
        #print(iid)
        #cook = coo['sessionid']        
        tok = 'd04b0a864b4b54837c0d870b0e77e076'
        cookies = {"sessionid": sessionid,}
        variables = {"id": iid,"first": 50}
        
        params = {"query_hash": tok,"variables": dumps(variables)}
        req1 = requests.get("https://www.instagram.com/graphql/query/", params = params, cookies = cookies)
        #print(req1.json())
        foId = str(req1.json()['data']['user']['edge_follow']['edges'][0]['node']['id'])
        foou = str(req1.json()['data']['user']['edge_follow']['edges'][0]['node']['username'])
        url1 = 'https://www.instagram.com/web/friendships/{}/unfollow/'.format(foId)
        hed1 = {
                    'accept': '*/*',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-length': '0',
                    'content-type': 'application/x-www-form-urlencoded',
                    'cookie': 'ig_did=77A45489-9A4C-43AD-9CA7-FA3FAB22FE24; ig_nrcb=1; mid=YGwlfgALAAEryeSgDseYghX2LAC-; csrftoken=EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA; ds_user_id=47432466264; sessionid='+sessionid,
                    'origin': 'https://www.instagram.com',
                    'referer': f'https://www.instagram.com/{users}/following/',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36 Edg/91.0.864.71',
                    'x-csrftoken': 'EMbT4gJqC4q9NTF2JVgBrAnTNC2MGPQA',
                    'x-ig-app-id': '936619743392459',
                    'x-ig-www-claim': 'hmac.AR0EWvjix_XsqAIjAt7fjL3qLwQKCRTB8UMXTGL5j7pkgYkq',
                    'x-instagram-ajax': '753ce878cd6d',
                    'x-requested-with': 'XMLHttpRequest'}
        done = requests.post(url1,headers=hed1)
       # print(done.text)  
        if '"status":"ok"' in done.text:
            sleep(3)
            H+=1
            print("Done Delete user: "+users)
        elif 'Please' in done.text:
            sleep(3)
            B1+=1			
            print("Not Delete user: "+users)
			
		
			
			
def Send_Text_To_Account():
		pass

		
				
								
if tool=="1":
	login_account_instagram()	
	
if tool=="2":
	Send_Text_To_Posts()
	
if tool=="3":
	Delete_Followeng()
	
	