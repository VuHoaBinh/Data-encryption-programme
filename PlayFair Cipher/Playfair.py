import tkinter as tk

root = tk.Tk()
root.title("Ma hoa Playfair")


label_Key = tk.Label(root,text ="nhap Key:")
entry_Key = tk.Entry(root, width = 20)

label_plaintext = tk.Label(root,text ="nhap plaintext:")
entry_plaintext = tk.Entry(root, width = 20)

label_result_cipher = tk.Label(root,text = "")

label_result_decipher = tk.Label(root,text = "")



def matrix(key):
	alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
	matrix=[]
	for e in key:
		if e not in matrix:
			matrix.append(e)

	for e in alphabet:
		if e not in matrix:
			matrix.append(e)    
	
	matrix_group=[]
	for e in range(5):
		matrix_group.append('')

	# group 5*5
	matrix_group[0]=matrix[0:5]
	matrix_group[1]=matrix[5:10]
	matrix_group[2]=matrix[10:15]
	matrix_group[3]=matrix[15:20]
	matrix_group[4]=matrix[20:25]

	return matrix_group

def cipher_to_message(message):
	i=0
	new=[]
	for x in range(int(len(message)/2)):
		new.append(message[i:i+2])
		i+=2
	return new

def message_to_digraphs(message_original):
	message=[]
	for e in message_original:
		message.append(e)

	# delete space 
	for unused in range(len(message)):
		if " " in message:
			message.remove(" ")

	# add "X"
	k = 0
	for e in range(int(len(message)/2)):
		if message[k]==message[k+1]:
			message.insert(k+1,'X')
		k+=2

	if len(message)%2==1:
		message.append("X")

	#Grouping
	i=0
	new=[]
	for x in range(1,int(len(message)/2+1)):
		new.append(message[i:i+2])
		i+=2
	return new

def find_position(key_matrix,letter):
	x=y=0
	for i in range(5):
		for j in range(5):
			if key_matrix[i][j] == letter:
				x=i
				y=j
	return x,y



# def ciphertext(message):
# 	message=message_to_digraphs(message)
# 	key_matrix=matrix(key)
# 	cipher=[]
# 	for e in message:
# 		x_new1,y_new1=find_position(key_matrix,e[0])
# 		x_new2,y_new2=find_position(key_matrix,e[1])
# 		# cung hang ngang
# 		if x_new1==x_new2:
# 			if y_new1==4:
# 				y_new1=-1
# 			if y_new2==4:
# 				y_new2=-1
# 			cipher.append(key_matrix[x_new1][y_new1+1])
# 			cipher.append(key_matrix[x_new2][y_new2+1])     
# 		elif y_new1==y_new2:
# 			if x_new1==4:
# 				x_new1=-1;
# 			if x_new2==4:
# 				x_new2=-1;
# 			cipher.append(key_matrix[x_new1+1][y_new1])
# 			cipher.append(key_matrix[x_new2+1][y_new2])
# 		else:
# 			cipher.append(key_matrix[x_new1][y_new2])
# 			cipher.append(key_matrix[x_new2][y_new1])
# 	answer=""
# 	for e in cipher:
# 		answer+=e
# 	return answer


# def decipher(message):
# 	message=digraphs_to_message(message)
# 	key_matrix=matrix(kdeey)
# 	decipher=[]
# 	for e in message:
# 		x_new1,y_new1=find_position(key_matrix,e[0])
# 		x_new2,y_new2=find_position(key_matrix,e[1])
# 		# cung hang ngang
# 		if x_new1==x_new2:
# 			if y_new1==4:
# 				y_new1=-1
# 			if y_new2==4:
# 				y_new2=-1
# 			decipher.append(key_matrix[x_new1][y_new1-1])
# 			decipher.append(key_matrix[x_new2][y_new2-1])     
# 		elif y_new1==y_new2:
# 			if x_new1==4:
# 				x_new1=-1;
# 			if x_new2==4:
# 				x_new2=-1;
# 			decipher.append(key_matrix[x_new1-1][y_new1])
# 			decipher.append(key_matrix[x_new2-1][y_new2])
# 		else:
# 			decipher.append(key_matrix[x_new1][y_new2])
# 			decipher.append(key_matrix[x_new2][y_new1])
# 	for unused in range(len(decipher)):
# 		if "X" in decipher:
# 			decipher.remove("X")
# 	result=""
# 	for e in decipher:
# 		result+=e
# 	return result

def PlayFair():
	key = entry_Key.get().upper()
	message = entry_plaintext.get().upper()
	
	#cipher
	message=message_to_digraphs(message)
	key_matrix=matrix(key)
	cipher=[]
	for e in message:
		x_new1,y_new1=find_position(key_matrix,e[0])
		x_new2,y_new2=find_position(key_matrix,e[1])
		# cung hang ngang
		if x_new1==x_new2:
			if y_new1==4:
				y_new1=-1
			if y_new2==4:
				y_new2=-1
			cipher.append(key_matrix[x_new1][y_new1+1])
			cipher.append(key_matrix[x_new2][y_new2+1])     
		elif y_new1==y_new2:
			if x_new1==4:
				x_new1=-1;
			if x_new2==4:
				x_new2=-1;
			cipher.append(key_matrix[x_new1+1][y_new1])
			cipher.append(key_matrix[x_new2+1][y_new2])
		else:
			cipher.append(key_matrix[x_new1][y_new2])
			cipher.append(key_matrix[x_new2][y_new1])
	
	answer=""
	for e in cipher:
		answer+=e
	label_result_cipher.config(text ="Result cipher: " +  answer)




	#decipher
	key = entry_Key.get().upper()
	message = entry_plaintext.get().upper()
	message=cipher_to_message(message)
	key_matrix=matrix(key)
	decipher=[]
	for e in message:
		x_new1,y_new1=find_position(key_matrix,e[0])
		x_new2,y_new2=find_position(key_matrix,e[1])
		# cung hang ngang
		if x_new1==x_new2:
			if y_new1==4:
				y_new1=-1
			if y_new2==4:
				y_new2=-1
			decipher.append(key_matrix[x_new1][y_new1-1])
			decipher.append(key_matrix[x_new2][y_new2-1])     
		elif y_new1==y_new2:
			if x_new1==4:
				x_new1=-1;
			if x_new2==4:
				x_new2=-1;
			decipher.append(key_matrix[x_new1-1][y_new1])
			decipher.append(key_matrix[x_new2-1][y_new2])
		else:
			decipher.append(key_matrix[x_new1][y_new2])
			decipher.append(key_matrix[x_new2][y_new1])

	#delete "X"
	for unused in range(len(decipher)):
		if "X" in decipher:
			decipher.remove("X")

	result=""
	for e in decipher:
		result+=e
	label_result_decipher.config(text ="Result decipher: " +  result)


button = tk.Button(root, text="Chuyển đổi", command=PlayFair)

label_plaintext.grid(row=0, column=0)
entry_plaintext.grid(row=0, column=1)
label_Key.grid(row=1, column=0)
entry_Key.grid(row=1, column=1)
label_result_cipher.grid(row=2, column=0)
label_result_decipher.grid(row=3, column=0)


button.grid(row=4, column=0, columnspan=2)

root.mainloop()

