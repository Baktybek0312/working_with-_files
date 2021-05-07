# Создайте программу, которая считает из файла текст, и если в тексте содержится буква “w”, то выведет на экран “Да, в тексте есть w”, иначе - “Нет, в тексте нет w”.
# Подсказка: используйте ключевое слово in.

a = open('/home/baha/PycharmProjects/test1/w.txt', 'w')
a.write("""Python is a widely used high-level programming language for general-purpose

programming, created by Guido van Rossum and first released in 1991. An interpreted

language, Python has a design philosophy that emphasizes code readability (notably

using whitespace indentation to delimit code blocks rather than curly brackets or

keywords), and a syntax that allows programmers to express concepts in fewer lines of

code than might be used in languages such as C++ or Java.""")

a.close()

a = open('/home/baha/PycharmProjects/test1/w.txt','r')
count = 0
if "w" in a.read():
    print("Да, в тексте есть w”")
    count += 1
    print(count)
else:
    print("“Нет, в тексте нет w”")
