from utils.logo import *
from utils.general import *
import modules.cms_scanner.main as cms_scanner
import keyboard

VERSION = 0.1

class Xen:
        
    def __init__(self) -> None:
        self.flag = 0
        self.usr_choice = ""
        pass


    def Tools_Menu(self):
        clear_screen()
        xen_print("Xen1um Hacking Tools Menu:", WHITE, True)
        xen_print(f"\t{BOLD}1{RED} {CYAN}-{RESET}{RED} [{RESET} CMS Scanner {RED}]{RESET}", WHITE, False)
        xen_print(f"\t{BOLD}2{RED} {CYAN}-{RESET}{RED} [{RESET} ICERIK {RED}]{RESET}", WHITE, False)
        xen_print(f"\t{BOLD}3{RED} {CYAN}-{RESET}{RED} [{RESET} ICERIK {RED}]{RESET}", WHITE, False)
        xen_print(f"\t{BOLD}4{RED} {CYAN}-{RESET}{RED} [{RESET} ICERIK {RED}]{RESET}", WHITE, False)
        xen_print(f"\t{BOLD}5{RED} {CYAN}-{RESET}{RED} [{RESET} ICERIK {RED}]{RESET}", WHITE, False)
        while self.flag == False:
            self.usr_choice = str(input("make a choice >> "))
            if self.usr_choice == "1":
                self.flag = True
                cms_scanner.Run()
            elif self.usr_choice == "2":
                print("currently under development.")
                self.flag = True
            elif self.usr_choice == "3":
                print("currently under development.")
                self.flag = True
            elif self.usr_choice == "4":
                print("currently under development.")
                self.flag = True
            elif self.usr_choice == "5":
                print("currently under development.")
                self.flag = True
            elif self.usr_choice == "menu":
                self.Tools_Menu()
                break
            elif self.usr_choice == "q" or "quit" in self.usr_choice:
                break


    def Boot_Menu(self):
        clear_screen()
        print(f"{LOGO}\n[*] Happy, Hacking ! [*]")
        delay(2)
        if os.geteuid() != 0:
            print("[ERROR] You need to be root to use the tool.")
            return
        os.system("/bin/bash -c 'read -s -n 1 -p \"Press any key to continue...\"'")
        self.Tools_Menu()


run = Xen()

run.Boot_Menu()