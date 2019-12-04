password = 'a123456'
x = 3
while x > 0:
	password1 = input('请输入密码：')
	if password1 == password:
		print('登陆成功！')
		break
	else:
		x = x - 1
		print('密码错误！还有',x,'次机会')