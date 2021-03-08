password = 'a123456'
i = 3
while True:
	pw = input('请输入密码：')
	if pw == password:
		print('登录成功！')
		break
	else:
		i = i - 1
		print ('密码错误！还有', i, '次机会。')
		if i == 0:
			break