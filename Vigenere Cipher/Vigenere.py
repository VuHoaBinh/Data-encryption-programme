import tkinter as tk
	
root = tk.Tk()
root.title("Ma hoa Vigenere")

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

label_key = tk.Label(root,text ="nhap key:")
entry_key = tk.Entry(root, width = 20)

label_plaintext = tk.Label(root,text ="nhap plaintext:")
entry_plaintext = tk.Entry(root, width = 20)

label_result_cipher = tk.Label(root,text = "")

label_result_decipher = tk.Label(root,text = "")

# def ciphere_text(plaintext, key):
# 	answer = ''
# 	key_index = 0
# 	for char in plaintext:
# 		if char in aphalbel:
# 			length = len(key)
# 			index_char_key = key[key_index % length]
# 			char_index = (aphalbel.index(char) + aphalbel.index(index_char_key))%26
# 			answer += aphalbel[char_index]
# 			key_index+=1
# 		else:
# 			answer += char
# 	return answer



# def deciphere_text(plaintext, key):
# 	answer = ''
# 	key_index = 0
# 	for char in plaintext:
# 		if char in aphalbel:
# 			length = len(key)
# 			index_char_key = key[key_index % length]
# 			char_index = (aphalbel.index(char) - aphalbel.index(index_char_key))%26
# 			answer += aphalbel[char_index]
# 			key_index+=1
# 		else:
# 			answer += char
# 	return answer


def Vigenere():
	key = entry_key.get().upper()
	plaintext = entry_plaintext.get().upper()
	
	#cipher
	answer = ''
	key_index = 0
	for char in plaintext:
		length = len(key)
		if char in alphabet:
			index_char_cipher = key[key_index % length]
			char_index_cipher = (alphabet.index(char) + alphabet.index(index_char_cipher))%len(alphabet) # 26
			answer += alphabet[char_index_cipher]
			key_index+=1
		else:
			answer += char
	label_result_cipher.config(text ="Result cipher: " +  answer)

	#decipher
	result = ''
	index = 0
	for char in plaintext:
		length = len(key)
		if char in alphabet:
			index_char_decipher = key[index % length]
			char_index_decipher = (alphabet.index(char) - alphabet.index(index_char_decipher))%len(alphabet)
			result += alphabet[char_index_decipher]
			index+=1
		else:
			result += char
	label_result_decipher.config(text ="Result decipher: " +  result)


button = tk.Button(root, text="Chuyển đổi", command=Vigenere)

label_plaintext.grid(row=0, column=0)
entry_plaintext.grid(row=0, column=1)
label_key.grid(row=1, column=0)
entry_key.grid(row=1, column=1)
label_result_cipher.grid(row=2, column=0)
label_result_decipher.grid(row=3, column=0)


button.grid(row=4, column=0, columnspan=2)

root.mainloop()