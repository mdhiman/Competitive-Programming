"""
1. Create a cipher with the following algorithm:
Divide the sentence in a block of key = x
Reverse the content of each block
Rotate each character with certain characters = y (OPTIONAL)
Return the cipher text
Create both encryption and decryption algorithms
Example: 
X = 5
Y = 0
Plain Text: WE HAVE RECEIVED THE LOCATION
Cipher Text:AH EWER EVEVIECEHT DTACOL NOIT
			AH EWER EVEVIECEHT DACOL NOIT
Explanation
WE HA - VE RE - CEIVE - D THE - " "LOCA - TION
AH EW - ER EV - EVIEC - EHT D - ACOL" " - NOIT 
"""
def str_reverse(str):
	if not str:
		return ""
	return str_reverse(str[1:len(str)])+str[0]

def create_cipher(plain_text,x,y):

	token_list=[]
	current_token=""
	for i in range(len(plain_text)):
		current_token=plain_text[i]+current_token
		if len(current_token)==x:
			token_list.append(str_reverse(current_token))
			current_token=""
	token_list.append(str_reverse(current_token))

	print(token_list)
	cipher_text="".join(token_list)
	return cipher_text

plain_text="WE HAVE RECEIVED THE LOCATION"
print(create_cipher(plain_text,5,0))
