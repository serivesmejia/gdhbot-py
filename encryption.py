from cryptography.fernet import Fernet
import os

def encrypt(filename):
  fStr = open(filename,"r").read()
  f = Fernet(os.getenv("decrypt_key"))
  
  st = f.encrypt(fStr.encode("utf-8")).decode("utf-8")

  return st

def decrypt(filename):
  fStr = open(filename,"r").read()
  f = Fernet(os.getenv("decrypt_key"))

  st = f.decrypt(fStr.encode("utf-8")).decode("utf-8")

  return st