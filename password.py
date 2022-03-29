
i = 0
while i < 3:
	password = input('please enter your password: ')

	if password == 'a123456' :
		print('you login succussfully')
		break
	else : 
		i = i + 1
		print('password is wrong, you still have',3-i,'oppportunites')
		
		