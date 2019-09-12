#Encryption/Decryption

#Description:Encrypt plaintext and decrypt ciphertext using my own algorithm.
#Author:Ahmad As Sami
#Date:5th  June2019


#At first we create a function for encrypting our message.

def encrypt(plain):
# Our algorithm will basically encrypt the message, by swapping the first and last chars of the input, and so on.
#First, we take length of the string.
    length=len(plain)
#We will create 2 empty strings- one with the 1st digits, and one with the last digits.
    str_of_1st_digits=""
    str_of_last_digits=""
#After that,we can start a for loop, which then basically puts the first digits in one string, starting from the left, and the last digits in another string, starting from the right.
#if the length of the input is even, we divide the range by 2, as we can actually do integer division and a float isnt produced.
    if length%2==0:
        for i in range(length//2):
        #if the indexes end up to be equal, i.e. the most middle character, that is just placed iin the 1st digits string.
            if i==length-1-i:
                str_of_1st_digits+=plain[i]
                break
            else:
                str_of_1st_digits+=plain[i]
                str_of_last_digits+=plain[length-1-i]
            
    else:
        for i in range(length):
        #if the indexes end up to be equal, i.e. the most middle character, that is just placed iin the 1st digits string.
            if i==length-1-i:
                str_of_1st_digits+=plain[i]
                break
            else:
                str_of_1st_digits+=plain[i]
                str_of_last_digits+=plain[length-1-i]
    #We then add the strings together to form a ciphertext.
    ciphertext=str_of_last_digits+str_of_1st_digits
        
    return ciphertext


def decrypt(ciphertext):
    str_of_1st_digits=""
    str_of_last_digits=""
    length=len(ciphertext)
    #Again, if the length of the input is even, we divide it by 2 to get the range, as an integer value is produced.
    if length%2==0:
        for i in range(length//2):
        #if the indexes end up to be equal, i.e. the most middle character, that is just placed iin the 1st digits string.
            if i==length-1-i:
                str_of_1st_digits+=ciphertext[i]
                break
            else:
                str_of_last_digits+=ciphertext[i]
                str_of_1st_digits+=ciphertext[length-1-i]
    else:
          for i in range(length):
        #if the indexes end up to be equal, i.e. the most middle character, that is just placed iin the 1st digits string.
            if i==length-1-i:
                str_of_1st_digits+=ciphertext[i]
                break
            else:
                str_of_last_digits+=ciphertext[i]
                str_of_1st_digits+=ciphertext[length-1-i]
                
    #We then go on to reverse the
    plaintext=str_of_1st_digits[::-1]+str_of_last_digits[::-1]           
    return plaintext    


# Main part of program
notFinished=True;
while notFinished:
    plaintext=input("Please enter your message to encrypt or s to stop:")
    if plaintext!= 'S' and plaintext!= 's' :
        print("\tLet's encrypt your message ... ")
        ciphertext= encrypt(plaintext)
        print("\t'{}' becomes '{}'.".format(plaintext, ciphertext))
        # Call the decrypt function with ciphertext
        # The decrypt function returnsplaintext
        print("\tLet's decrypt your encrypted message ... ")
        plaintext= decrypt(ciphertext)
        # Print the ciphertextand plainText
        print("\t'{}' becomes '{}'.".format(ciphertext, plaintext))
    else:
        notFinished= False;
        
print("Bye!")