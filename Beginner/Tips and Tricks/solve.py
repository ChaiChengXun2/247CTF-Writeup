from pwn import * 

with remote("f56f6f56444d8618.247ctf.com", 50006) as connection: 
	connection.readline()
	connection.readline()

	for i in range(500):
		question = connection.readline().decode().replace("\r", "")[22:-2]
		question_answer = eval(question)

		print(f"{question} = {question_answer}")

		payload = (str(question_answer) + "\r\n").encode()

		connection.sendline(payload)
		connection.readline()

	print(connection.readline().decode().replace("\r", ""))