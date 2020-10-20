import random


def decrypt(ciphertext): #defines method to decrypt input string
    plaintext = ""
    for i in range(len(ciphertext)):
        if i % 2 == 0: #if even
            cipher_ascii = ord(ciphertext[i]) #convert chr to ascii int
            plain_ascii = cipher_ascii - 1 #carry out given decrypt logic
            plaintext += chr(plain_ascii) #convert ascii int to chr and add to string plaintext
        elif i % 2 == 1: #if odd
            cipher_ascii = ord(ciphertext[i]) #convert chr to ascii int
            plain_ascii = cipher_ascii + 1 #carry out given decrypt logic
            plaintext += chr(plain_ascii) #convert ascii int to chr and add to string plaintext
    return plaintext #return decrypted string


words = ["WHDSPQZ", "XHO", "TTDBFRT", "QQJYF", "ENQD", "DNPK", "CNTR", "EHWHOD", "TSVMOHOF",
         "XNOCFQGTM"]  # words to be picked from
word = words[random.randint(0, 9)]  # select word at random
lives = 10 #establish 10 lives
print("You have 10 lives left and you have used these letters: ")
userInput = input("Guess a letter:").capitalize() #get first input from user and capitalize it to match given array format
currentWord = "" #current form that user sees, blanks or correct guesses
guessedSoFar = "" #letters guessed by user
for x in range(len(word)): #set values of current word to periods as blanks
    currentWord += "."
for b in range(10): #increment for 10 lives
    if not userInput in word: #if userinput is wrong
        print("Your letter, " + userInput + " is not in the word.")
        guessedSoFar += userInput + " "
        lives -= 1
    elif userInput in word: #if userinput is right
        for y in range(len(currentWord)): #increment through the output word state (blanks and correct values)
            if word[y] == userInput: #if userinput exists at this index
                currentWord = currentWord[:y] + userInput + currentWord[y + 1:] #slice currentWord and insert userInput where a blank was before at correct position
    if currentWord == word: #if user has guessed the word entirely
        print("YAY! You guessed the word " + word + "!!\nThis was the encrypted message!")
        print("The decoded message says: " + decrypt(word)) #run decrypt method to decrypt mystery word
        break #end for loop (no need to finish lives)
    if lives == 0: #if out of guesses
        print("You died, sorry. The word was " + word + "\nYou'll have to guess the word correctly to decode the message")
        break #end for loop (no need to finish lives)
    print("You have " + str(lives) + " lives left and you have used these letters: " + guessedSoFar) #print number of lives left and list of guesses
    print(currentWord) #print current output (blanks and correct guesses)
    userInput = input("Guess a letter:").capitalize() #take next userinput and capitalize it to match given array format




