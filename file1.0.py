# С помощью Linux запишите в Файл все названия директорий из "/" - корневого каталога.
# Если у вас Windows, сделайте тоже самое))) Только с помощью команды dir. В итоге у вас на рабочем столе должен появиться файл directories.txt.
# Откройте этот файл с помощью Python и выведите на экран все директории из directories.txt.

f = open('directories.txt', 'w')
f.write('''PycharmProjects   snap    Документы   Изображения   Общедоступные   Шаблоны
 repaTest          Видео   Загрузки    Музыка       'Рабочий стол'
''')
f.close()

with open('directories.txt','r') as f:
    print(f.read())
