import tkinter as tk

root = tk.Tk()
root.title("Ma hoa Caesar")

# aphalbel
alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

label_K = tk.Label(root,text ="nhap K:")
entry_K = tk.Entry(root, width = 20)

label_plaintext = tk.Label(root,text ="nhap plaintext:")
entry_plaintext = tk.Entry(root, width = 20)

label_result_cipher = tk.Label(root,text = "")

label_result_decipher = tk.Label(root,text = "")


# def ciphertext(n,plaintext):
#     answer = ''
#     for k in plaintext:
#         try:
#             index_char = ((alphabet.index(k)+n) % len(alphabet)) # len(aphabel) = 26
#             answer += alphabet[index_char]
#         except ValueError: # back
#             answer +=k
#     return answer

# def decrypt(n, plaintext):
#     result = ''
#     n = int(entry_K.get())
#     plaintext = entry_plaintext.get()
#     for l in plaintext:
#         try:
#             i = (alphabet.index(l) - n) % len(alphabet))
#             result += alphabet[i]
#         except ValueError:
#             result += l
#     return result

def Ceaser():
    n = int(entry_K.get())
    plaintext = entry_plaintext.get().upper()


    #cipher
    answer = ''
    for k in plaintext:
        try:
            index_char = ((alphabet.index(k)+n) % len(alphabet)) # len(aphabel) = 26
            answer += alphabet[index_char]
        except ValueError: # back
            answer +=k
    label_result_cipher.config(text ="Result cipher: " +  answer)

    #decipher
    result = ''
    for l in plaintext:
        try:
            i = (alphabet.index(l) - n) % len(alphabet)
            result += alphabet[i]
        except ValueError:
            result += l
    label_result_decipher.config(text ="Result decipher: " +  result)


#GUI
button = tk.Button(root, text="Chuyển đổi", command=Ceaser)

label_plaintext.grid(row=0, column=0)
entry_plaintext.grid(row=0, column=1)
label_K.grid(row=1, column=0)
entry_K.grid(row=1, column=1)
label_result_cipher.grid(row=2, column=0)
label_result_decipher.grid(row=3, column=0)


button.grid(row=4, column=0, columnspan=2)

root.mainloop()
