from time import sleep as delay
LOGO = """
            ___           _,.---,---.,_
            |         ,;~'             '~;,
            |       ,;                     ;,
   Reverse  |      ;                         ; ,--- HACKERMAN
    Shell   |     ,'                         /'
            |    ,;                        /' ;,
 SUID <-----|    ; ;      .           . <-'  ; |
            |__  | ;   ______       ______   ;<----- /dev/brain
           ___   |  '/~"     ~" . "~     "~\'  |
           |     |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
Happy,     |      |   |        }:{        | <------ Vulnerability
  Hacking! |      |   l       / | \       !   |
Linux OS > |      .~  (__,.--" .^. "--.,__)  ~.
           |      |    ----;' / | \ `;-<--------- CVE-2023-00000
           |__     \__.       \/^\/       .__/
              ___   V| \                 / |V <--- Exploits
              |      | |T~\___!___!___/~T| |
              |      | |`IIII_I_I_I_IIII'| |
              |      |  \,III I I I III,/  |
 pwned.py <---|       \   `~~~~~~~~~~'    /
              |         \   .       .    /----[ 0day ]
              |          \.    ^       ./
              |___         ^~~~^~~~~~~^            
"""

def print_logo(sec=0.03):
  for line in LOGO.split('\n'):
    print(line)
    delay(sec)