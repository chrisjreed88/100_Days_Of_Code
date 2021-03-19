def caesar(text, shift, direction):
	result = ""
	if direction == "decode":
		shift *= -1
	for char in text:
		if char in alphabet:
			current_position = alphabet.index(char)
			new_position = current_position + shift
			result += alphabet[new_position]
		else:
			result += char
	if direction == "encode":
		print(f"The encoded text is {result}")
	elif direction == "decode":
		print(f"The decoded text is {result}")	
	

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
alphabet.extend(alphabet)

print("""

   ___                          ___ _      _            
  / __|__ _ ___ ___ __ _ _ _   / __(_)_ __| |_  ___ _ _ 
 | (__/ _` / -_|_-</ _` | '_| | (__| | '_ \ ' \/ -_) '_|
  \___\__,_\___/__/\__,_|_|    \___|_| .__/_||_\___|_|  
                                     |_|                
""")

cont = True
while cont:
	direction = input("Type 'encode' to encrypt, or 'decode' to decrypt:\n").lower()
	text = input("Type your message:\n").lower()
	try:
		shift = int(input("Type the shift number:\n"))
		shift = shift % 26
	except ValueError:
		print("Shift value needs to be a number!!")
		continue
	if direction not in ["encode", "decode"]:
		print(f"{direction} is not valid!!")
		continue
	caesar(text=text, shift=shift, direction=direction)
	run_again = input("Do you want to do some more? y or n: ").lower()
	if run_again == "n":
		cont = False
print("Goodbye")