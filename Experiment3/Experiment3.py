"""
* coding=utf-8
* python=3.11
* File: Experiment3.py
* Author: donghy23@mails.tsinghua.edu.cn
* Created: 2024-7-12
* Repo: https://github.com/FHYQ-Dong/Tsinghua-Program-Design-Assignment-3/blob/main/Experiment3/Experiment3.py
"""

import argparse


class CaesarCrypto():
    def __init__(
        self, 
        plaintext: str|None = None, 
        key: int|None = None, 
        ciphertext: str|None = None
    ):
        self._plaintext = None
        self._key = None
        self._ciphertext = None
        
        if not key:
            raise ValueError("Key must be provided")
        else:
            self._key = key
            if plaintext and not ciphertext:
                self._plaintext = plaintext
                self._ciphertext = ciphertext
                self.encrypt()
            elif not plaintext and ciphertext:
                self._plaintext = plaintext
                self._ciphertext = ciphertext
                self.decrypt()
            elif plaintext and ciphertext:
                if not self.valid():
                    raise ValueError("Plain text, key and cipher text not match")
                else:
                    self._plaintext = plaintext
                    self._ciphertext = ciphertext
            
    def encrypt(self):
        self._ciphertext = ''
        k = self._key % 26
        for c in self._plaintext:
            if 'a' <= c <= 'z':
                self._ciphertext += chr(
                    ord(c) + k if ord(c) + k <= ord('z') \
                    else ord(c) + k - ord('z') + ord('a') - 1
                )
            elif 'A' <= c <= 'Z':
                self._ciphertext += chr(
                    ord(c) + k if ord(c) + k <= ord('Z') \
                    else ord(c) + k - ord('Z') + ord('A') - 1
                )
            else:
                self._ciphertext += c
    
    def decrypt(self):
        self._plaintext = ''
        k = self._key % 26
        for c in self._ciphertext:
            if 'a' <= c <= 'z':
                self._plaintext += chr(
                    ord(c) - k if ord(c) - k >= ord('a') \
                    else ord('z') - ord('a') + ord(c) - k + 1
                )
            elif 'A' <= c <= 'Z':
                self._plaintext += chr(
                    ord(c) - k if ord(c) - k >= ord('A') \
                    else ord('Z') - ord('A') + ord(c) - k + 1
                )
            else:
                self._plaintext += c

    def valid(self) -> bool:
        temp = ''
        k = self._key % 26
        for c in self._plaintext:
            if 'a' < c < 'z':
                temp += chr(
                    tmp := ord(c) + k if tmp <= ord('z') \
                    else ord(c) + k - ord('z') + ord('a') - 1
                )
            elif 'A' < c < 'Z':
                temp += chr(
                    tmp := ord(c) + k if tmp <= ord('Z') \
                    else ord(c) + k - ord('Z') + ord('A') - 1
                )
            else:
                temp += c
        return temp == self._ciphertext
    
    @property
    def plaintext(self):
        return self._plaintext
    @property
    def key(self):
        return self._key
    @property
    def ciphertext(self):
        return self._ciphertext

    @plaintext.setter
    def plaintext(self, plaintext):
        self._plaintext = plaintext
        self.encrypt()
    @ciphertext.setter
    def ciphertext(self, ciphertext):
        self._ciphertext = ciphertext
        self.decrypt()
        

class VigenereCrypto():
    def __init__(
        self, 
        plaintext: str|None = None, 
        key: str|None = None, 
        ciphertext: str|None = None
    ):
        self._plaintext = None
        self._key = None
        self._ciphertext = None
        
        if not key:
            raise ValueError("Key must be provided")
        else:
            self._key = key
            if plaintext and not ciphertext:
                self._plaintext = plaintext
                self._ciphertext = ciphertext
                self.encrypt()
            elif not plaintext and ciphertext:
                self._plaintext = plaintext
                self._ciphertext = ciphertext
                self.decrypt()
            elif plaintext and ciphertext:
                if not self.valid():
                    raise ValueError("Plain text, key and cipher text not match")
                else:
                    self._plaintext = plaintext
                    self._ciphertext = ciphertext
            
    def encrypt(self):
        self._ciphertext = ''
        k = self._key
        for i, c in enumerate(self._plaintext):
            if 'a' <= c <= 'z':
                self._ciphertext += chr(
                    ord(c) + ord(k[i % len(k)]) - ord('a') if ord(c) + ord(k[i % len(k)]) - ord('a') <= ord('z') \
                    else ord(c) + ord(k[i % len(k)]) - ord('a') - ord('z') + ord('a') - 1
                )
            elif 'A' <= c <= 'Z':
                self._ciphertext += chr(
                    ord(c) + ord(k[i % len(k)]) - ord('A') if ord(c) + ord(k[i % len(k)]) - ord('A') <= ord('Z') \
                    else ord(c) + ord(k[i % len(k)]) - ord('A') - ord('Z') + ord('A') - 1
                )
            else:
                self._ciphertext += c
    
    def decrypt(self):
        self._plaintext = ''
        k = self._key
        for i, c in enumerate(self._ciphertext):
            if 'a' <= c <= 'z':
                self._plaintext += chr(
                    ord(c) - ord(k[i % len(k)]) + ord('a') if ord(c) - ord(k[i % len(k)]) + ord('a') >= ord('a') \
                    else ord('z') - ord('a') + ord(c) - ord(k[i % len(k)]) + 1
                )
            elif 'A' <= c <= 'Z':
                self._plaintext += chr(
                    ord(c) - ord(k[i % len(k)]) + ord('A') if ord(c) - ord(k[i % len(k)]) + ord('A') >= ord('A') \
                    else ord('Z') - ord('A') + ord(c) - ord(k[i % len(k)]) + 1
                )
            else:
                self._plaintext += c
                
    def valid(self) -> bool:
        temp = ''
        k = self._key
        for i, c in enumerate(self._plaintext):
            if 'a' < c < 'z':
                temp += chr(
                    tmp := ord(c) + ord(k[i % len(k)]) - ord('a') if tmp <= ord('z') \
                    else ord(c) + ord(k[i % len(k)]) - ord('a') - ord('z') + ord('a') - 1
                )
            elif 'A' < c < 'Z':
                temp += chr(
                    tmp := ord(c) + ord(k[i % len(k)]) - ord('A') if tmp <= ord('Z') \
                    else ord(c) + ord(k[i % len(k)]) - ord('A') - ord('Z') + ord('A') - 1
                )
            else:
                temp += c
        return temp == self._ciphertext
    
    @property
    def plaintext(self):
        return self._plaintext
    @property
    def key(self):
        return self._key
    @property
    def ciphertext(self):
        return self._ciphertext
    @plaintext.setter
    def plaintext(self, plaintext):
        self._plaintext = plaintext
        self.encrypt()
    @ciphertext.setter
    def ciphertext(self, ciphertext):
        self._ciphertext = ciphertext
        self.decrypt()
    @key.setter
    def key(self, key):
        self._key = key
        self.encrypt()
        self.decrypt()
        

def Caesar_test():
    pt = "XYZABxyzab"
    ky = 28
    cc = CaesarCrypto(pt, ky, None)
    ct = cc.plaintext
    print(f"------- Encrypt Test -------\nPlain text: {pt}\nKey: {ky}\nCipher text: {ct}")
    
    cc = CaesarCrypto(None, ky, ct)
    pt = cc.plaintext
    print(f"------- Decrypt Test -------\nCipher text: {ct}\nKey: {ky}\nPlain text: {pt}")
    
    
def Vigenere_test():
    pt = "XYZABxyzab"
    ky = "KEY"
    cc = VigenereCrypto(pt, ky, None)
    ct = cc.ciphertext
    print(f"------- Encrypt Test -------\nPlain text: {pt}\nKey: {ky}\nCipher text: {ct}")
    
    cc = VigenereCrypto(None, ky, ct)
    pt = cc.plaintext
    print(f"------- Decrypt Test -------\nCipher text: {ct}\nKey: {ky}\nPlain text: {pt}")
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser("Crypto")
    parser.add_argument("method", type=str, help="[caesar|vigenere]", required=True)
    parser.add_argument("mode", type=str, help="[encrypt|decrypt]", required=True)
    parser.add_argument("-k", "--key", type=int, help="Key for encrypt/decrypt")
    parser.add_argument("-p", "--plaintext", type=str, help="Plain text")
    parser.add_argument("-c", "--ciphertext", type=str, help="Cipher text")
    args = parser.parse_args()
    
    if args.mode == "encrypt" and args.method == "caesar":
        try:
            cc = CaesarCrypto(args.plaintext, args.key, None)
            print(f"Encrypt...\nPlain text: {args.plaintext}\nKey: {args.key}\nCipher text: {cc.ciphertext}")
        except ValueError as e:
            print(e)
            parser.print_help()
    elif args.mode == "decrypt" and args.method == "caesar":
        try:
            cc = CaesarCrypto(None, args.key, args.ciphertext)
            print(f"Decrypt...\nPlain text: {cc.plaintext}\nKey: {args.key}\nCipher text: {args.ciphertext}")
        except ValueError as e:
            print(e)
            parser.print_help()
    elif args.mode == "encrypt" and args.method == "vigenere":
        try:
            cc = VigenereCrypto(args.plaintext, args.key, None)
            print(f"Encrypt...\nPlain text: {args.plaintext}\nKey: {args.key}\nCipher text: {cc.ciphertext}")
        except ValueError as e:
            print(e)
            parser.print_help()
    elif args.mode == "decrypt" and args.method == "vigenere":
        try:
            cc = VigenereCrypto(None, args.key, args.ciphertext)
            print(f"Decrypt...\nPlain text: {cc.plaintext}\nKey: {args.key}\nCipher text: {args.ciphertext}")
        except ValueError as e:
            print(e)
            parser.print_help() 
    else:
        parser.print_help()