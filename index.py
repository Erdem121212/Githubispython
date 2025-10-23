import os
import time

def loop():
    write = input("python-user/home --> ")

print("fake pc ")
print("...")
time.sleep(3)
print("System check clear.")
os.system('clear')

print("Booting from SSD")
time.sleep(2)
os.system('clear')
print("Loading initramfs")
time.sleep(2.5)
print("Loading linux6.16-py")
time.sleep(1)
os.system('clear')
print("welcome to pylinux!!")
print("make sure you installed this from github and correct repo!")
while True:
 write = input("python-user/home --> ")
 
 if write == 'help':
    print("Help ------")
    print("help -- shows this page")
    print("ls -- list directory contents")
    print("echo - display a line of text")
    print("pytfetch -- shows the system information")
    print("apt , package manager.")
    print("shutdown , shuts the system down")
 if write == 'echo':
    writedthing = ""
    echo = input("write the text --> ")
    print(writedthing)
 if write == 'ls':
    print("python1folder python2folder python2.txt python3.txt Downloads Documents Musics Videos .local .mozilla")
 if write == 'pytfetch':
    asciiart = """
         .+++++++*****.             
        .++..++++*******            
        +++..+**********            
        +++++***********            
 ...:+++++++++++********.......     
.-++++++++**************.::::::.    
.++++++++***************.:::::::    
++++++*****************-.:::::::..  
+++++******-:::::::::..::::::::::.  
+++*****:..:::::::::::::::::::::..  
=+*****+.:::::::::::::::::::::::..  
.******.::::::::::::::::::::::::    
 .+****.::::::::::::::::::::::.     
   .....::::::::......::......      
        ::::::::::::::::            
        .::::::::::. .::            
         .:::::::::::::             
            ...::...                         
"""
    print(asciiart)
    print("OS : PyLinux v1.0")
    print("Monitor : Default Monitor Device")
    print("CPU : Intel Core i7 2th Gen")
    print("GPU: NVIDIA 1060ti (so old yeah :d)")
    print("Kernel : linux-6.16")
 elif write:
    print("bash: command not found")
 if write == 'info':
       print("pylinux 1.0")
       print("'an fake linux completely made with python'")
 elif write == 'apt':
       print("E: Could not open lock life /var/lib/dpkg/lock-frontend - open (13: Permission denied)")
       print("E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), are you root?")
 elif write == 'sudo apt':
       print("1- web-server")
       print("2- python3")
       print("3- shimejiy")
       install_packages = input("--> ")
       INSTALLED_PACKAGES = []
       if install_packages == 'web-server':
          INSTALLED_PACKAGES.append("web-server")
 elif "web-server" in INSTALLED_PACKAGES and write == 'web-server':
        print("web-server daemon is not running")
        print("start web-server with systemctl enable now web-server.service")
 elif write == 'shutdown':
    print("The system will shutdown now!")
    print("pylinux 6.16")
    time.sleep(2.5)
    os.system('clear')
    break
 else:
    pass
