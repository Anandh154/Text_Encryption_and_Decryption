class Transposition_Cipher:
    def __init__(self, key):
        self.key = key
    # text encryption process done here
    def encryption(self, plaintext):
        # Implementing encryption logic here
        en_text=""
        for text in plaintext:
            en_text+=chr(ord(text)+self.key)           
        return en_text
    # text decryption process done here
    def decryption(self, en_text):
        # Implementing decryption logic here
        de_text=""
        for text in en_text:
            de_text+=chr(ord(text)-self.key)          
        return de_text
    

# Example usage:
CO = Transposition_Cipher(3)
plaintext = "welcome to my python world"
en_text = CO.encryption(plaintext)
de_text = CO.decryption(en_text)
print('plained data :', plaintext)
print('encrypted data :', en_text)
print('decrypted data :', de_text)
















