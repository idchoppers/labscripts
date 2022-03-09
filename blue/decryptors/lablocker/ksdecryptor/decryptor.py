#
# decryptor.py - idchoppers
#
# A hastily made decryption software, one file at a time.
# Requires the key used during encryption.
# Usage: decryptor.py <<File>> <<Key>>
#
# USE AH'S DECRYPTION SOFTWARE, IT IS BETTER!
#

import sys
import os
from cryptography.fernet import Fernet

targetfile = sys.argv[1]
keyfile = sys.argv[2]

def Decryptfile(targetfile, keyfile):
    with open(keyfile, "rb") as key:
        for data in key:
            keydata = Fernet(data)
    
    with open(targetfile, "rb") as file:
        encrypted = file.read()

    decrypted = keydata.decrypt(encrypted)

    with open(targetfile, "wb") as origfile:
        origfile.write(decrypted)

Decryptfile(targetfile, keyfile)
