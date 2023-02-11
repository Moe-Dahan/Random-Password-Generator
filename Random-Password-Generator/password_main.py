import tkinter as tk
from tkinter import filedialog
import string
import random
import pyautogui
import os
from cryptography.fernet import Fernet


pyautogui.alert('Select Encryption Key Location')
choose_loction_key = filedialog.askdirectory(initialdir='/')
chosen_location = f'{choose_loction_key}\\keyfile.key'

class password:
    def __init__(self, key):
        self.key = key
    def encrypt(): # encrypting the key
        # Gen the key to decrypt and encrypt file
        key = Fernet.generate_key()
        with open(chosen_location, 'wb') as keyfile: # writes the key to usb
            keyfile.write(key)
        with open(chosen_location, 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        # opening the original file to encrypt
        with open('Pass_it.text', 'rb') as file:
            original = file.read()
        # encrypting the file
        encrypted = fernet.encrypt(original)
        with open('pass_it.text', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    def decrypt():# Decrypting the key
        # opening the key
        with open(chosen_location, 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)
        # opening the encrypted file
        with open('pass_it.text', 'rb') as enc_file:
            encrypted = enc_file.read()
        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
                # writing the decrypted data
        with open('pass_it.text', 'wb') as dec_file:
            dec_file.write(decrypted)

    # function to generate the password
    def GenPassword(): # generate the password
        userPasswordLength = int(passwordLengthEntry.get())
        password = []
        letters = string.ascii_letters
        digi = string.digits
        chara = string.punctuation
        for i in range(userPasswordLength):
            randomchar = random.choice(digi + chara + letters) 
            password.append(randomchar)
        the_password.set(password)
        the_website.set(siteNameEntry.get())

    def savePasswords(): # save the password
        with open('Pass_it.text', 'a') as the_list:
            the_list.write(f'{siteNameEntry.get()} : {results.get()}\n')
            pyautogui.alert(f'Password Saved in {os.getcwd()}\\pass_it.text')

main_window = tk.Tk()
main_window.iconbitmap('icon\\systemlockscreen_94256.ico')
main_window.title('Password Generator')
main_window.geometry('410x310')

the_password = tk.StringVar() # password string var
the_website = tk.StringVar() # website string var

configPasswordFrame = tk.Frame(main_window) # config settings for password Generator

siteName = tk.Label(configPasswordFrame, text='Site Name', font=("Comic Sans MS", 9, 'bold')).grid(row=0, column=0, sticky='w') # Label for site name
siteNameEntry = tk.Entry(configPasswordFrame, font=("Comic Sans MS", 9, 'bold'), width=45)
siteNameEntry.grid(row=1, column=0, sticky='w') # site entry here

passwordLength = tk.Label(configPasswordFrame, text='password length', font=("Comic Sans MS", 9, 'bold')).grid(row=2, column=0, sticky='w')
passwordLengthEntry = tk.Entry(configPasswordFrame, font=("Comic Sans MS", 9, 'bold'), width=10)
passwordLengthEntry.grid(row=3, column=0, sticky='w') # length entry box here

configPasswordFrame.place(x=5, y=0) # end of password frame

the_password = tk.StringVar() # password string var
the_website = tk.StringVar() # website string var

resultsWebsiteFrame = tk.Frame(main_window) # frame for results starts

resultsWebsite = tk.Label(resultsWebsiteFrame, text='Results Website', font=("Comic Sans MS", 9, 'bold')).grid(row=0, column=0, sticky='w') # label for website
resultsWebsiteLabel = tk.Entry(resultsWebsiteFrame, textvariable=the_website, font=("Comic Sans MS", 9, 'bold'), width=45)
resultsWebsiteLabel.grid(row=1, column=0, sticky='w')

resultsLabel = tk.Label(resultsWebsiteFrame, text='Results Password', font=("Comic Sans MS", 9, 'bold')).grid(row=2, column=0, sticky='w') # label for password
results = tk.Entry(resultsWebsiteFrame, textvariable=the_password, font=("Comic Sans MS", 9, 'bold'), width=45)
results.grid(row=3, column=0, sticky='w')

resultsWebsiteFrame.place(x=5, y=100) # end of results of the frame

button_frame = tk.Frame(main_window)

genButton = tk.Button(button_frame, text='Generate Password', command=password.GenPassword, font=("Comic Sans MS", 9, 'bold'), width=21).grid(row=4, column=0, sticky='w') # button to generate the password
saveResults = tk.Button(button_frame, text='Save Passwords', command=password.savePasswords, font=("Comic Sans MS", 9, 'bold'), width=21).grid(row=4, column=1, sticky='w') # saving the passwords

encrypt_Results = tk.Button(button_frame, text='Encrypt Passwords', command=password.encrypt, font=("Comic Sans MS", 9, 'bold'), width=21).grid(row=5, column=0, sticky='w')
decrypt_results = tk.Button(button_frame, text='Decrypt Passwords', command=password.decrypt, font=("Comic Sans MS", 9, 'bold'), width=21).grid(row=5, column=1, sticky='w')

button_frame.place(x=5, y=215)
main_window.mainloop()

