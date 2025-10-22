import os
import time

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
print("Welcome to pythonlinux!!")
print("To learn more things about the terminal write 'help' to the terminal")
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
    print("OS : PythonOS v1.0")
    print("Monitor : Default Monitor Device")
    print("CPU : Intel Core i7 2th Gen")
    print("GPU: NVIDIA 1060ti (so old yeah :d)")
    print("Kernel : linux-6.16")
