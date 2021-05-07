# Создайте файл users.txt.
# Напишите программу которая спрашивает у пользователя его Логин и Пароль и записывает в файл users.txt.

f = open('/home/baha/PycharmProjects/test1/users.txt', 'w')
email = input("Введите логин: ")
password = input("Введите логин: ")

f.write(f"login {email}\n password{password}")
f.close()
with open('/home/baha/PycharmProjects/test1/users.txt','r') as f:
    print(f.read())


