from Crypto.Cipher import AES
import random

# Deve ter 16, 24 ou 32 bytes de comprimento

list_palavras = 'ABCDEFGHIJKLMNOPQRSTUVXYZabcdefghijklmnopqrstuvxyz1234567890!@#$%&*?><+='


def criptografar(msg, comp=16):
    chars = random.choices(list_palavras, k=comp)
    key = ''.join(chars).encode()
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    texto, tag = cipher.encrypt_and_digest(msg.encode('ascii'))
    key = key.decode('UTF-8')
    return texto, key, nonce, tag


'''
def descriptografar(noc, texto):
    cipher = AES.new(key, AES.MODE_EAX, nonce=noc)
    texto2 = cipher.decrypt(texto)
    return texto2.decode('ascii')'''
