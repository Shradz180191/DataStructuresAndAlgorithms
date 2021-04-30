'''

Using the Caesar’s Cypher as a reference, write a function encrypt_message(<key>, <’message’> ), that takes in an offset number as an input from main and a string message, and returns and prints an encrypted message based on your offset (using lowercase only).

As an example, encrypt_message(-1,’Hello’) would return gdkkn

Where H ==> g

Where e ==> d

Where l ==> k

Where o ==> n

For the program take an input of 3 and encrypt the message “Hello, how are you?” and print the result.

 

Using the Caesar’s Cypher as a reference, write a function decrypt_message(<key>, <’message’> ), that takes in an offset number as an input from main and a string message, and returns and prints an decrypted message based on your offset (using lowercase only).

Use this function to decode " dzntlw otdelynp" given that the letters had been shifted by 11 and print the result.

Hint: Use for to loop through each letter in the message.  Use the in method to check for the letter.   Create an index position for the letter, using find, and add the key to the to the position to cause it to shift.

Remember to call the functions from the main function

'''


def encrypt_message(key,mess):
    encoded = ""
    for i in range(0,len(mess)):
        val = ord(mess[i])
        if(val + key > 126):
            encoded += chr(val + key - 127 + 32)
        else:
            encoded += chr(val + key)
    return encoded

def decrypt)message(key,mess):
    orgi = ""
    for i in range(0,len(mess)):
        val = ord(mess[i])
        if (val - key < 32):
            orgi += chr(((val - key )+ 127) - 32)
        else:
            orgi += chr(val - key)
    return orgi

def main():
    choice = 'y'
    while(choice == 'y'):
        n = int(input("Enter 1 to encrypt, 2 to decode: "))
        if(n==1):
            mess = input("Enter the message to be encrypt: ")
            key = int(input("Enter a key for encoding: "))
            print("Message Encoded: \n\t"+encrypt_message(key,mess))
            choice = input("\n\tContinue (y/n):\t")
        elif(n==2):
            mess = input("Enter an encrypted message to decode: ")
            key = int(input("Enter a key for decoding: "))
            print("Message Decoded: \n\t"+decrypt_message(key,mess))
            choice = input("\n\tContinue (y/n):\t")
        elif(n==0):
            break

if __name__ == "__main__":
    main()
  
  
