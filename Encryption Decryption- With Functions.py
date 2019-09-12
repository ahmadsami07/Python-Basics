#Encryption/Decryption With Functions
#Description: Use the encryption and decryption functions to encrypt a string into odd and even separations,and then decrypt to normal form.

text=input("Please enter the text you wish to encrypt:")
print("Your text initially:{}".format(text))
def encrypt(text):
    length=len(text)
    str_of_odd_chars=""
    str_of_even_chars=""
    charposition=0
    for charposition in range(length):
        text[charposition]
        if (charposition % 2==0):
            str_of_even_chars+=text[charposition]
        else:
            str_of_odd_chars+=text[charposition]
    
    ciphertext=str_of_even_chars+str_of_odd_chars
    return ciphertext
ciphertext=encrypt(text)

print("Your encrypted message is : {}.".format(ciphertext))

print("Now to decrypt the message: i.e. get it back to initial form:")

def decrypt(ciphertext):
        