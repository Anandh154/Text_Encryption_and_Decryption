'''
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
'''
class TranspositionCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        # Remove spaces from the plaintext
        plaintext = plaintext.replace(" ", "")

        # Calculate the number of columns based on the length of the key
        num_columns = len(self.key)

        # Calculate the number of rows required
        num_rows = (len(plaintext) + num_columns - 1) // num_columns

        # Add padding to the plaintext if necessary
        padding_size = num_rows * num_columns - len(plaintext)
        plaintext += ' ' * padding_size

        # Create a list of empty strings to represent the columns
        columns = [''] * num_columns

        # Populate the columns with characters from the plaintext
        for i, char in enumerate(plaintext):
            column_index = i % num_columns
            columns[column_index] += char

        # Rearrange the columns based on the key
        rearranged_columns = [None] * num_columns
        for i, col_index in enumerate(self.key):
            rearranged_columns[i] = columns[col_index - 1]

        # Concatenate the rearranged columns to form the ciphertext
        ciphertext = ''.join(rearranged_columns)
        return ciphertext

    def decrypt(self, ciphertext):
        # Calculate the number of columns based on the length of the key
        num_columns = len(self.key)

        # Calculate the number of rows required
        num_rows = len(ciphertext) // num_columns

        # Create a list of empty strings to represent the columns
        columns = [''] * num_columns

        # Calculate the number of characters in the last row
        last_row_chars = len(ciphertext) % num_columns

        # Fill the columns with characters from the ciphertext
        col_index = 0
        for i, char in enumerate(ciphertext):
            if i % num_rows == 0 and last_row_chars > 0:
                num_rows += 1
                last_row_chars -= 1
            columns[col_index] += char
            col_index = (col_index + 1) % num_columns

        # Rearrange the columns based on the key
        rearranged_columns = [None] * num_columns
        for i, col_index in enumerate(self.key):
            rearranged_columns[col_index - 1] = columns[i]

        # Concatenate the rearranged columns to form the plaintext
        plaintext = ''.join(rearranged_columns).strip()
        return plaintext

# Example usage:
key = [3, 1, 4, 2]
cipher = TranspositionCipher(key)
plaintext = "Hello World"
encrypted_text = cipher.encrypt(plaintext)
print("Plaintext:", plaintext)
print("Encrypted text:", encrypted_text)

decrypted_text = cipher.decrypt(encrypted_text)
print("Decrypted text:", decrypted_text)


























