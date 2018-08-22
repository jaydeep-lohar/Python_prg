def check_uppercase(psw):
	uppercase_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	uppercase = 0
	for ch in psw:
		if ch in uppercase_list:
			uppercase += 1
	if uppercase >= 1:
		return True
	else : 
		return False

def check_lowercase(psw):
	lowercase_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
	lowercase = 0
	for ch in psw:
		if ch in lowercase_list:
			lowercase += 1
	if lowercase >= 1:
		return True
	else : 
		return False

def check_number(psw):
	number_list = ['0','1','2','3','4','5','6','7','8','9']
	number = 0
	for ch in psw:
		if ch in number_list:
			number += 1
	if number >= 1:
		return True
	else : 
		return False

def check_special(psw):
	special_list = ['$','#','@']
	notspecial_list = ['(',')','%','^','&']
	special,notspecial = 0,0
	for ch in psw:
		if ch in special_list:
			special += 1
		if ch in notspecial_list:
			notspecial += 1
	if special >= 1 and notspecial == 0:
		return True
	else : 
		return False

def check_length(psw):
	if len(psw) >=6 and len(psw) <=12:
		return True
	else : 
		return False

def __main__():
	str = raw_input("Enter the passwords separated by , ")
	psw_list=str.split(',')
	print('From the list of given password following are valid:-')
	for psw in psw_list:
  		if check_uppercase(psw) & check_lowercase(psw) & check_length(psw) & check_special(psw) & check_number(psw):
  			print(psw)

if __name__ == '__main__':
	__main__()
