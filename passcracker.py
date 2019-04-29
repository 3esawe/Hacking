import crypt 

def encrypt(word):
	return crypt.crypt(word,"AI")





def passcracker(cryptedpass):
	words = open("words2")
	salt = cryptedpass[0:2]

	for word in words.readlines():
		word = word.strip('\n')
		cryptword = crypt.crypt(word,salt)
		if cryptword == cryptedpass:
			return word 
	return 'not found'



if __name__ == '__main__':
	c = encrypt("hello")
	v = passcracker(c)
	print(v)