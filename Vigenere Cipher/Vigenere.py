# vigenerer

aphalbel = "abcdefghijklmnopqrstuvwxyz"
# alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def ciphere_text(plaintext, key):
	answer = ''
	key_index = 0
	for char in plaintext:
		if char in aphalbel:
			length = len(key)
			index_char_key = key[key_index % length]
			char_index = (aphalbel.index(char) + aphalbel.index(index_char_key))%26
			answer += aphalbel[char_index]
			key_index+=1
		else:
			answer += char
	return answer


def run():
    print(ciphere_text("ngaymaigapnhau","hoahue"))
run()