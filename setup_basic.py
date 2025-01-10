import os,sys,time,socket,subprocess


# Versoin: 1.0
# Author: evilfeonix
# Name: EvilFeonix Basic
# Date: 13 - NOVEMBER - 2024
# Website: www.evilfeonix.com 
# Email: evilfeonix@gmail.com 


########    EvilFeonix Basic, a basic Python script that aimed at beginners starting with gray hat hacking in Termux. 
########    This tool install essential Python libraries and Termux packages, 
########    giving you a foundational toolkit for exploring network security and gray hat hacking.
########    EvilFeonix Basic provides a setup for installing essential tools and Python packages for gray hat hacking and security analysis on Termux. 
########    This is ideal for beginners, as it covers network and security fundamentals in a user-friendly manner.


stop="\033[0m"
red="\033[31;1m"
blue="\033[34;1m"
green="\033[32;1m"
darkred="\033[91m"
yellow="\033[33;1m"
purple="\033[35;1m"


error=f"{blue}[{stop}-{blue}]{red} "
info2=f"{red}[{stop}•{red}]{yellow} "
notice=f"{blue}[{stop}!{blue}]{red} "
info=f"{green}[{stop}+{green}]{purple} "
first= f"{green}[{stop}01{green}]{purple} "
second= f"{green}[{stop}02{green}]{purple} "
version="1.0.0"


def slow(y):
    for x in y+'\n':sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./300)
def load(y):
    for x in y:sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./300)
    for a in '...'+'\n':sys.stdout.write(a),sys.stdout.flush(),time.sleep(1)


def internet():
    try:
        s = socket.socket(socket.AF_NET, socket.SOCK_STREAM)
        s.connect_ex(("www.google.com",80))
        return True
    except Exception:return False
    

def start_banner():
    logo=f"""{stop}███████╗██╗       ██╗██╗██╗      ███████╗███████╗ ██████╗ ███╗   ██╗██╗██╗  ██╗ 
{green}██╔════╝ ██║     ██║ ██║██║      ██╔════╝██╔════╝██╔═══██╗████╗  ██║██║╚██╗██╔╝{stop}
{green}█████╗    ██║   ██║  ██║██║ ███╗ █████╗  █████╗  ██║   ██║██╔██╗ ██║██║ ╚███╔╝{stop}
{green}██╔══╝     ██║ ██║   ██║██║ ╚══╝ ██╔══╝  ██╔══╝  ██║   ██║██║╚██╗██║██║ ██╔██╗{stop}
███████╗   ╚███╔╝    ██║███████╗ ██║     ███████╗╚██████╔╝██║ ╚████║██║██╔╝ ██╗
╚══════╝    ╚══╝     ╚═╝╚══════╝ ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝ 
                        
\t\t\t\t██████╗  █████╗ ███████╗██╗ ██████╗
{blue}:>> {green}Coded by EVIL {darkred}FEONIX{blue} <<:\t{green}██╔══██╗██╔══██╗██╔════╝██║██╔════╝
{blue}:>> {green}www.evilfeonix.com{blue} <<:\t{green}██████╔╝███████║███████╗██║██║{stop}   
{blue}:>> {green}EvilFeonix Basic{blue} <<:\t{green}██╔══██╗██╔══██║╚════██║██║██║{stop}   
\t      v[{green}{version[:-2]}{stop}]\t\t██████╔╝██║  ██║███████║██║╚██████╗ 
\t\t\t\t╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝ ╚═════╝\n{red}"""
    print(logo)
    slow(f"===========================================================")



def end_banner():
    slow(f"{red}")
    slow("===========================================================")
    slow(f"{green}EvilFeonix Basic setup complete. Happy hacking ({stop}ethically{green})!{red}")
    slow("===========================================================")
    slow(f"{stop}")
        
def update_termux():
    load(f"\n{info}Updating Termux packages{stop}")
    os.system("pkg update -y && pkg upgrade -y")
    slow(f"{info}Termux packages updated.\n{stop}")

def install_core_tools():
    load(f"\n{info}Installing core Termux hacking tools{stop}")
    core_tools = ["nmap", "hydra", "curl", "wget", "git", "openssl", "python"]
    for tool in core_tools:
        os.system(f"pkg install {tool} -y")
    slow(f"{info}Core Termux tools installed.\n{stop}")

def install_extra_tools():
    load(f"\n{info}Installing extra hacking tools (sqlmap, john, netcat){stop}")
    extra_tools = ["sqlmap", "john", "netcat"]
    for tool in extra_tools:
        os.system(f"pkg install {tool} -y")
    slow(f"{info}Extra tools installed.\n{stop}")

def install_python_requirements():
    load(f"\n{info}Installing Python packages{stop}")
    os.system("pip install -r requirements.txt")
    slow(f"{info}Python packages installed.\n{stop}")

def configure_ssh():
    load(f"\n{info}Configuring SSH (for remote access testing){stop}")
    os.system("pkg install openssh -y")
    os.system("sshd")
    slow(f"{info}SSH configured. Use 'ssh <username>@<ip>' to connect.\n{stop}")

def additional_tools_recommendation():
    slow(f"\n{notice}Additional Recommendations:")
    slow(f"{info2}To install Metasploit, run:{stop}")
    slow("    pkg install unstable-repo && pkg install metasploit")
    slow(f"{yellow}Metasploit is an advanced tool that requires responsibility and legal compliance.")
    slow(f"{info2}To install Nikto (a web server scanner), run:{stop}")
    slow("    pkg install nikto")
    slow(f"{yellow}These tools should be used responsibly and only on systems you have permission to test.\n")

def install_net_utils():
    load(f"\n{info}Installing network utilities{stop}")
    network_utils = ["tsu", "termux-api", "net-tools"]
    for util in network_utils:
        os.system(f"pkg install {util} -y")
    slow(f"{info}Network utilities installed.\n{stop}")
    
def all_in_0ne():
    os.system("clea" + "r || cls"),start_banner()
    load("Starting EvilFeonix Basic setup for Termux")
    update_termux()
    install_core_tools()
    install_extra_tools()
    install_python_requirements()
    configure_ssh()
    install_net_utils()
    additional_tools_recommendation()
    end_banner()

def main():
    os.system("clea" + "r || cls")
    start_banner()
    net=internet()
    
    if not net:
        time.sleep(1)
        slow(f"\n{error}Please check your internet connection{stop}")
        os.sys.exit()
    try:
        slow(""f"\n\t{first}Run EvilFeonix Basic\n\t{second}Exit\n""")
        opt=input(""f"{green}[{stop}SELECT OPTION..{green}] {blue}:>>{purple} """)
        if opt in["1","01","a","A"]:all_in_0ne()
        elif opt in["2","02","b","B"]:slow(f"\n{error}Thanks for using our tool.{stop}"),os.sys.exit()
        else:load(f"\n{error}Invalid Option!{stop}"),main()
    except KeyboardInterrupt:
        slow(f"\n\n{error}User Requested an Interrupt!{stop}")
        load(f"{error}Program Running Down!{stop}")
        os.sys.exit()


if __name__ == "__main__":
    main()
