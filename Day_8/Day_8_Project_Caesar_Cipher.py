def shift_alphabet(shift):
	shifted_alphabet = []
	for n in range(26):
		i = n + shift
		if i >= 26:
			shifted_alphabet.append(alphabet[i-26])
		else:
			shifted_alphabet.append(alphabet[i])
	return shifted_alphabet
	

def encrypt(text, shift):
	encrypted = ""
	alphabet_positions = []
	shifted_alphabet = shift_alphabet(shift)
	for char in text:
		alphabet_positions.append(alphabet.index(char))
	for pos in alphabet_positions:
		encrypted += shifted_alphabet[pos]
	print(f"The encrypted text is {encrypted}")
	
def decrypt(text, shift):
	decrypted = ""
	alphabet_positions = []
	shifted_alphabet = shift_alphabet(shift)
	for char in text:
		alphabet_positions.append(shifted_alphabet.index(char))
	for pos in alphabet_positions:
		decrypted += alphabet[pos]
	print(f"The decrypted text is {decrypted}")
			
		

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

direction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction == "encode":
	encrypt(text=text, shift=shift)
else:
	decrypt(text=text, shift=shift)