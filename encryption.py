from cryptography.fernet import Fernet
import os

def encrypt_file(filename, decrypt_key):
  fStr = open(filename,"r").read()
  f = Fernet(decrypt_key)
  
  st = f.encrypt(fStr.encode("utf-8")).decode("utf-8")

  return st

def decrypt_file(filename, decrypt_key):
  fStr = open(filename,"r").read()
  f = Fernet(decrypt_key)

  st = f.decrypt(fStr.encode("utf-8")).decode("utf-8")

  return st

def encrypt_str(text, decrypt_key):
  f = Fernet(decrypt_key)
  
  st = f.encrypt(text.encode("utf-8")).decode("utf-8")

  return st

def decrypt_str(text, decrypt_key):
  f = Fernet(decrypt_key)

  st = f.decrypt(text.encode("utf-8")).decode("utf-8")

  return st