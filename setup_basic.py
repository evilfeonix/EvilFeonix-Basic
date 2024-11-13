import os
import subprocess
# 10 - AUGUST - 2024
# Tool-Name: emailCracker
# Versoin: 2.0.1
# Author: FEONIX
# Website: www.evilfeonix.com 


################ This is a dictionary attack tool based on cracking email password
###############  Named, (emailCracker) and was build with the help of python programming language
######           This tool generates a list of password (also known as wordlist) based on the victim's info2rmatiom provided
############     Those password this tool generate are 4 in minimum and 18 in maximum (length)
################ And also trys to crack the victim's email password with the generated password.


stop="\033[0m"
red="\033[31;1m"
d_red="\033[91m"
blue="\033[34;1m"
green="\033[32;1m"
yellow="\033[33;1m"
purple="\033[35;1m"
skyblue="\033[36;1m"


error="%s[%s-%s]%s "%(blue,stop,blue,red)
info2="%s[%s•%s]%s "%(green,stop,green,purple)
add="%s[%s+%s]%s "%(red,stop,red,yellow)
notice="%s[%s!%s]%s "%(blue,stop,blue,red)
success="%s[%s√%s]%s "%(purple,stop,purple,green)
first= "%s[%s01%s]%s "%(green,stop,green,purple)
second= "%s[%s02%s]%s "%(green,stop,green,purple)
third= "%s[%s03%s]%s "%(green,stop,green,purple)
version="2.0.1.6"


def slow2(y):
    for x in y+'    '+'    '+'\r':sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./300)
def slow(y):
    for x in y:sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./300)
def show(y):
    for x in y+'\n':sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./1000)
def slowbr(y):
    for x in y+'\n':sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./300)
def loadbr(y):
    for x in y:sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./300)
    for a in '...'+'\n':sys.stdout.write(a),sys.stdout.flush(),time.sleep(1)
def load(y):
    for x in y:sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./300)
    for a in '...'+'      '+'\r':
        sys.stdout.write(a),sys.stdout.flush()
        if a==' ':time.sleep(1./300)
        else:time.sleep(1)


def internet():
    try:
        s = socket(AF_NET, SOCK_STREAM)
        s.connect_ex(("www.google.com",80))
        return True
    except Exception:return False
    

def aboutus():
    os.system("clea" + "r || cls")
    granted()
    slowbr('\t%sTool Name      %s:>>%s  EVILFEONIX BASIC'%(info2,blue,purple))
    slowbr('\t%sVersion        %s:>>%s  v[%s]'%(info2,blue,purple,version[:-2]))
    slowbr('\t%sAuthor         %s:>>%s  FEONIX'%(info2,blue,d_red))
    slowbr('\t%sGithub         %s:>>%s  Evil %sFeoniX'%(info2,blue,purple,d_red))
    slowbr('\t%sYoutube        %s:>>%s  Evil %sFeoniX'%(info2,blue,purple,d_red))
    slowbr('\t%sLatest Update  %s:>>%s  13-11-2024'%(info2,blue,purple))
    slowbr('\t%sWebsite        %s:>>%s  www.evilfeonix.com'%(info2,blue,purple))
    slow("%s"%(red))
    slowbr("="*60)
    slowbr("")
    act=input('%sPress %s[%sENTER%s]%s To Continue'%(add,purple,stop,purple,yellow))
    return main()

def granted():
    logo="""
███████╗██╗       ██╗██╗██╗          ███████╗███████╗ ██████╗ ███╗   ██╗██╗██╗  ██╗ 
██╔════╝ ██║     ██║ ██║██║          ██╔════╝██╔════╝██╔═══██╗████╗  ██║██║╚██╗██╔╝
█████╗    ██║   ██║  ██║██║          █████╗  █████╗  ██║   ██║██╔██╗ ██║██║ ╚███╔╝
██╔══╝     ██║ ██║   ██║██║          ██╔══╝  ██╔══╝  ██║   ██║██║╚██╗██║██║ ██╔██╗
███████╗   ╚███╔╝    ██║███████╗     ██║     ███████╗╚██████╔╝██║ ╚████║██║██╔╝ ██╗
╚══════╝    ╚══╝      ╚═╝╚══════╝    ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝ 

                  ██████╗  █████╗ ███████╗██╗ ██████╗
                  ██╔══██╗██╔══██╗██╔════╝██║██╔════╝
                  ██████╔╝███████║███████╗██║██║   
                  ██╔══██╗██╔══██║╚════██║██║██║   
                  ██████╔╝██║  ██║███████║██║╚██████╗ 
                  ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝"""
    print(logo)
    slow("%s"%(red))
    slowbr("="*60)
    slowbr("%s:>> %sCoded by EVIL %sFEONIX %s<<:".center(66," ")%(blue,green,d_red,blue))
    slowbr("%s:>> %swww.evilfeonix.com %s<<:".center(63," ")%(blue,green,blue))
    slowbr("%s:>> %sEvilFeonix Basic %s<<:%s".center(66," ")%(blue,green,blue,red))
    slowbr("="*60)


def end_banner():
  print("==========================================================")
  print("EvilFeonix Basic setup complete. Ready for ethical hacking!")
  print("==========================================================")
        
def update_termux():
    print("\n[+] Updating Termux packages...")
    os.system("pkg update -y && pkg upgrade -y")
    print("[+] Termux packages updated.\n")

def install_core_tools():
    print("\n[+] Installing core Termux hacking tools...")
    core_tools = ["nmap", "hydra", "curl", "wget", "git", "openssl", "python"]
    for tool in core_tools:
        os.system(f"pkg install {tool} -y")
    print("[+] Core Termux tools installed.\n")

def install_extra_tools():
    print("\n[+] Installing extra hacking tools (sqlmap, john, netcat)...")
    extra_tools = ["sqlmap", "john", "netcat"]
    for tool in extra_tools:
        os.system(f"pkg install {tool} -y")
    print("[+] Extra tools installed.\n")

def install_python_requirements():
    print("\n[+] Installing Python packages...")
    os.system("pip install -r requirements.txt")
    print("[+] Python packages installed.\n")

def configure_ssh():
    print("\n[+] Configuring SSH (for remote access testing)...")
    os.system("pkg install openssh -y")
    os.system("sshd")
    print("[+] SSH configured. Use 'ssh <username>@<ip>' to connect.\n")

def additional_tools_recommendation():
    print("\n[!] Additional Recommendations:")
    print("To install Metasploit, run:")
    print("    pkg install unstable-repo && pkg install metasploit")
    print("Metasploit is an advanced tool that requires responsibility and legal compliance.")
    print("To install Nikto (a web server scanner), run:")
    print("    pkg install nikto")
    print("These tools should be used responsibly and only on systems you have permission to test.\n")

def install_network_utils():
    print("\n[+] Installing network utilities...")
    network_utils = ["tsu", "termux-api", "net-tools"]
    for util in network_utils:
        os.system(f"pkg install {util} -y")
    print("[+] Network utilities installed.\n")

def main():
    os.system("clea" + "r || cls"),granted()
    net=internet()
    if not net:
        slow("\033[31m; Please check your internet connection \033[0m")
        os.sys.exit()
    try:
        slowbr("""\n\t%sStart Program\n\t%sAbout\n\t%sExit\n"""%(first,second,third))
        opt=input("""%s[%sSELECT OPTION..%s] %s:>>%s """%(green,stop,green,blue,purple))
        if opt in["1","01","a","A"]:cracker(argument)
        elif opt in["2","02","b","B"]:aboutus()
        elif opt in["3","03","c","C"]:slowbr("\n%sThanks for using our tool.%s"%(error,stop)),os.sys.exit()
        else:loadbr("\n%sInvali Option!%s"%(error,stop)),main()
    except KeyboardInterrupt:slowbr("\n\n%sUser Requested an Interrupt!%s"%(error,stop)),slow("%sProgram Running Down!%s"%(error,stop)),load(''),os.sys.exit()


if __name__ == "__main__":
    print("Starting EvilFeonix Basic setup for Termux...\n")
    update_termux()
    install_core_tools()
    install_extra_tools()
    install_python_requirements()
    configure_ssh()
    install_network_utils()
    additional_tools_recommendation()
    print("\n")
