import os
import time

def loop():
    write = input("python-user/home --> ")

print("Screen : PyScreen")
print("Hardware checking..")
time.sleep(1)
print("Checked. Healthy.")
os.system('clear')

print("Booting from Adata SU650 - 500 GB")
time.sleep(2)
os.system('clear')
print("Loading linux6.16-py")
time.sleep(2.5)
print("Loading initramfs")
time.sleep(1)
os.system('clear')
print("welcome to pylinux!!")
print("")
while True:
 write = input("python-user/home --> ")
 
 if write == 'help':
    print("Help ------")
    print("help -- shows this page")
    print("ls -- shows the files and directorys on the directory.")
    print("echo -- shows the text you writed")
    print("pytfetch -- shows the system information")
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
    print("keske os kullanabilseydim ama okul bilgisayarları bilgisayar donanımı bilgisi alma şifreli oluyor eğer şifreyi girmezsek büyük ihtimal gösteremiyor")
 elif write:
    print("bash: command not found")
 if write == 'info':
       print("pylinux 1.0")
       print("'an fake linux completely made with python'")
 elif write == 'apt':
       print("apt cant be runned without sudo. Are you sudo??")
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
