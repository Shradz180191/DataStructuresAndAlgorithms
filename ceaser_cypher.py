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
