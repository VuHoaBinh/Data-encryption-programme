import tkinter as tk

root = tk.Tk()
root.title("Ma hoa Substitution")

label_plaintext = tk.Label(root,text ="nhap plaintext:")
entry_plaintext = tk.Entry(root, width = 20)


label_result_cipher = tk.Label(root,text = "")

label_result_decipher = tk.Label(root,text = "")

substitution_table_cipher = {
    'A': 'X',
    'B': 'N',
    'C': 'Y',
    'D': 'A',
    'E': 'H',
    'F': 'P',
    'G': 'O',
    'H': 'G',
    'I': 'Z',
    'J': 'Q',
    'K': 'W',
    'L': 'B',
    'M': 'T',
    'N': 'S',
    'O': 'F',
    'P': 'L',
    'Q': 'R',
    'R': 'C',
    'S': 'V',
    'T': 'M',
    'U': 'U',
    'V': 'E',
    'W': 'K',
    'X': 'J',
    'Y': 'D',
    'Z': 'I'
}

substitution_table_decipher = {
    'A': 'D',
    'B': 'L',
    'C': 'R',
    'D': 'Y',
    'E': 'V',
    'F': 'O',
    'G': 'H',
    'H': 'E',
    'I': 'Z',
    'J': 'X',
    'K': 'W',
    'L': 'P',
    'M': 'T',
    'N': 'B',
    'O': 'G',
    'P': 'F',
    'Q': 'J',
    'R': 'Q',
    'S': 'N',
    'T': 'M',
    'U': 'U',
    'V': 'S',
    'W': 'K',
    'X': 'A',
    'Y': 'C',
    'Z': 'I'
}

# def substitution_cipher(message):
#     cipher_text = ''
#     for char in message:
#         if char in substitution_table_cipher:
#             cipher_text += substitution_table_cipher[char]
#         else:
#             cipher_text += char
#     return cipher_textx

# def substitution_decipher(message):
#     decipher_text = ''
#     for char in message:
#         if char in substitution_table_decipher:
#             decipher_text += substitution_table_decipher[char]
#         else:
#             decipher_text += char
#     return decipher_text


def substitution():
    message = entry_plaintext.get().upper()
    
    #cipher
    cipher_text = ''
    for char in message:
        if char in substitution_table_cipher:
            cipher_text += substitution_table_cipher[char]
        else:
            cipher_text += char
    label_result_cipher.config(text ="Result cipher: " +  cipher_text)
        
    #decipher
    decipher_text = ''
    for char in message:
        if char in substitution_table_decipher:
            decipher_text += substitution_table_decipher[char]
        else:
            decipher_text += char
    label_result_decipher.config(text ="Result decipher: " +  decipher_text)

button = tk.Button(root, text="Chuyển đổi", command=substitution)

#GUI
label_plaintext.grid(row=0, column=0)
entry_plaintext.grid(row=0, column=1)

label_result_cipher.grid(row=2, column=0)
label_result_decipher.grid(row=3, column=0)


button.grid(row=4, column=0, columnspan=2)

root.mainloop()