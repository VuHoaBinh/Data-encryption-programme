# class Caesar:
    
# aphalbel
alphabet = "abcdefghijklmnopqrstuvwxyz"

def ciphertext(n ,plaintext):
    answer = ''
    for k in plaintext:
        try:
            index_char = (alphabet.index(k)+n) % len(alphabet) # len(aphabel) = 26
            answer += alphabet[index_char]
        except ValueError: # back
            answer +=k
    return answer

# def decrypt(self, n, ciphertext):
#     """Decrypt the string and return the plaintext"""
#     result = ''

#     for l in ciphertext:
#         try:
#             i = (self.key.index(l) - n) % len(self.key)
#             result += self.key[i]
#         except ValueError:
#             result += l

#     return result

def run():
    print(ciphertext(13,"guidelines"))
run()