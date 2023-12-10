import modules.cms_scanner.useragents as user_agent
import modules.cms_scanner.wordpress as wp
import modules.cms_scanner.xenforo as xen
import requests
import random
import validators


def set_target():
    global target
    target = str(input("Enter URL with (http/https) : "))
    validate_data()


def validate_data():
    flag = check_domain(target)
    if flag != True:
        print("[FAIL] Make sure you enter a valid URL.")
        return
    send_req()


def check_domain(str_domain):
    str_domain = str(str_domain)
    return bool(validators.url(str_domain))


def check_WordPress(html):
    for word in wp.WORDPRESS_LIST:
        if word in html:
            return True
        return False
    

def check_XenForo(html):
    for word in xen.XENFORO_LIST:
        if word in html:
            return True
        return False


def detect_CMS(html_data):
    html_data = str(html_data).lower()
    if check_WordPress(html_data) == True:
        print(f"[+] {target} is WordPress [+]")
    elif check_XenForo(html_data) == True:
        print(f"[+] {target} is XenForo [+]")
    else:
        print(f"[-] {target} is unknown CMS [-]")


def send_req():
    random_uagent = random.choice(user_agent.USER_AGENTS_LIST)
    response = requests.get(url=target , headers={"User-Agent" : random_uagent},timeout=10)
    if response.status_code in range(200,400):
        print(f"[STATUS:{response.status_code}] {response.url} scanning CMS...")
        detect_CMS(response.text)
    elif response.status_code in range(400,500):
        print(f"[STATUS:{response.status_code}] {response.url} is not found.")
    elif response.status_code in range(500,600):
        print(f"[STATUS:{response.status_code}] {response.url} SERVER ERROR.")
    else:
        print(response.status_code)

def Run():
    set_target()