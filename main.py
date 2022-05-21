import time
import os

from progress.bar import *

os.system('cls' if os.name == 'nt' else 'clear')

bar  =  IncrementalBar ( "Загрузка:" ,  max = 100 ) 
for  i  in  range ( 100 ): 
    time.sleep(0.01)
    bar.next()
os.system('cls' if os.name == 'nt' else 'clear')

txt = 'Добро пожаловать!'
for i in txt:
    time.sleep(0.1)
    print(i, end='', flush=True)
time.sleep(1)

print('\n')

time.sleep(1)

txt = 'Я помогу вам освоить Termux и узнать, как его использовать.\nЭто просто!\n'
for i in txt:
    time.sleep(0.08)
    print(i, end='', flush=True)
time.sleep(3)

txt = 'Termux - это эмулятор терминала среды Linux. По сути, это всё тот же Linux, но без графического интерфейса и взаимодействие с этой оболочкой осуществляется только через текстовые команды. Конечно, через терминал многого не сделаешь, но этого всё равно достаточно для запуска, например, Bash и Python-скриптов. Важно, чтобы у Python-скрипта не было графической оболочки.\nСкоро сами поймёте.'
for i in txt:
    time.sleep(0.05)
    print(i, end='', flush=True)
time.sleep(3)

txt = '\nПервое, что нужно делать сразу после открытия Termux, так это обновлять пакеты. Для этого используются две команды:'
for i in txt:
    time.sleep(0.08)
    print(i, end='', flush=True)
time.sleep(1)

os.system('cls' if os.name == 'nt' else 'clear')

print('''
Задание 1 | Обновите пакеты

===========================
''')

print('В случае, если Termux спрашивает разрешение, то отвечайте "Y", чтобы разрешить или "N", чтобы не разрешить.')

time.sleep(2)

txt = 'apt update\n \n'
for i in txt:
    time.sleep(0.1)
    print(i, end='', flush=True)

time.sleep(2)

bar  =  IncrementalBar ( "Обновление списка пакетов:" ,  max = 100 ) 
for  i  in  range ( 100 ): 
    time.sleep(0.01)
    bar.next()

print('\nУспешно! Мы обнаружили, что у вас устарели 4 библиотеки. Давайте обновим их с помощью "apt upgrade"\n')
time.sleep(3)

txt = 'apt upgrade\n \n'
for i in txt:
    time.sleep(0.1)
    print(i, end='', flush=True)

time.sleep(2)

bar  =  IncrementalBar ( "Обновление пакетов:" ,  max = 100 ) 
for  i  in  range ( 100 ): 
    time.sleep(0.01)
    bar.next()

print('\nУспешно! Все пакеты были обновлены до последней версии.\n \n')

time.sleep(3)

txt = 'Совет: Чтобы писать команды в одну строку пишите после каждой команды два амперсанда "&&". \n'
for i in txt:
    time.sleep(0.1)
    print(i, end='', flush=True)

time.sleep(2)

txt = '\n apt update && apt upgrade'
for i in txt:
    time.sleep(0.1)
    print(i, end='', flush=True)

time.sleep(2)

txt = '\n \nПопробуйте после завершения обучения!'
for i in txt:
    time.sleep(0.05)
    print(i, end='', flush=True)

time.sleep(1)

txt = '\n \nТеперь давайте попробуем переместиться по директориям. Запомните: \n'
for i in txt:
    time.sleep(0.09)
    print(i, end='', flush=True)

txt = '\n▏ cd FolderName - перейти в другую папку.\n'
for i in txt:
    time.sleep(0.03)
    print(i, end='', flush=True)

txt = '\n▏ cd .. - вернуться в предыдущую директорию.\n'
for i in txt:
    time.sleep(0.03)
    print(i, end='', flush=True)

txt = '\n▏ ls - посмотреть, какие файлы и папки есть в директории.\n'
for i in txt:
    time.sleep(0.03)
    print(i, end='', flush=True)

time.sleep(5)

os.system('cls' if os.name == 'nt' else 'clear')
time.sleep(3)
print('Файловая система:')

print('''
╦ home 
╚ Folder1
    ╠ Folder2
    ╚ File.txt
╚ Archive.7z
''')

print('\n')

txt = '\nls'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)

time.sleep(1)

print('\nFolder1      Archive.7z')

time.sleep(3)

txt = '\ncd Folder1'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)

time.sleep(2)

txt = '\nls'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)

time.sleep(1)

print('\nFolder2      File.txt')

time.sleep(2)

txt = '\ncd ..'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)

time.sleep(3)

txt = '\nls'
for i in txt:
    time.sleep(0.5)
    print(i, end='', flush=True)

time.sleep(1)
print('\nFolder1      Archive.7z')

time.sleep(3)

txt = '\nОтлично! Но что, если вам надо удалить или переместить файл?'
for i in txt:
    time.sleep(0.03)
    print(i, end='', flush=True)

time.sleep(1)

txt = ' Для этого есть следующие команды:'
for i in txt:
    time.sleep(0.03)
    print(i, end='', flush=True)

time.sleep(3)

txt = '\n▏ rm - удалить  один файл\n'
for i in txt:
    time.sleep(0.03)
    print(i, end='', flush=True)

txt = '\n▏ rm -r удалить папку со всеми файлами внутри неё\n'
for i in txt:
    time.sleep(0.03)
    print(i, end='', flush=True)

txt = '\n▏ rm -i - удаление с выводом в консоли запрос на подтверждение удаления каждого файла.\n'
for i in txt:
    time.sleep(0.03)
    print(i, end='', flush=True)

txt = '\n▏ mkdir - создаёт папку в той директории, где вы находитесь. Если указать после "mkdir" путь, то там папка будет создана там.\n'
for i in txt:
    time.sleep(0.03)
    print(i, end='', flush=True)

txt = '\n▏ touch - создаёт файл в той директории, где вы находитесь. Если указать после "touch" путь, то там файл будет создан там.\n'
for i in txt:
    time.sleep(0.03)
    print(i, end='', flush=True)

txt = 'Итак...'
for i in txt:
    time.sleep(0.2)
    print(i, end='', flush=True)

time.sleep(8)

os.system('cls' if os.name == 'nt' else 'clear')

print('''
Задание 2 | Поработайте с файлами

=================================

Кстати, консоль вы можете очистить
используя команду "clear"
''')

print('\n')

time.sleep(2)

time.sleep(3)
print('Файловая система:')

print('''
╦ home 
╚ Folder1
    ╠ Folder2
    ╚ File.txt
╚ Archive.7z
''')

txt = 'ls'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)

time.sleep(2)

print('\nFolder1      Archive.7z')

time.sleep(3)

txt = 'mkdir MkdirFolder'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)

time.sleep(2)

print('\n')

txt = '\nls'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)

time.sleep(2)

print('\nFolder1        MkdirFolder        Archive.7z')

time.sleep(2)

txt = '\ncd MkdirFolder'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)
time.sleep(2)
print('')

txt = '\ntouch file.txt'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)
time.sleep(2)
print('')

txt = '\nls'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)
time.sleep(2)
print('\nfile.txt')
time.sleep(2)
txt = '\ncd ..'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)

print ('')
time.sleep(2)

txt = '\nls'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)

time.sleep(2)

print('\nFolder1        MkdirFolder        Archive.7z')

txt = '\nrm MkdirFolder'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)

time.sleep(1)

print('\nОшибка | В данной папке есть файлы')

time.sleep(2)
txt = '\nrm -r MkdirFolder'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)
print('')
time.sleep(3)
txt = '\nls'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)
print('\nFolder1      Archive.7z')
time.sleep(2)
txt = '\nclear'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)

time.sleep(2)
os.system('cls' if os.name == 'nt' else 'clear')
txt = '\nТолько что мы научились работать с файлами. А что, если вам надо перекинуть файлы из памяти своего телефона в Termux?'
for i in txt:
    time.sleep(0.04)
    print(i, end='', flush=True)
time.sleep(3)
txt = '\nИтак, команды:'
for i in txt:
    time.sleep(0.04)
    print(i, end='', flush=True)

time.sleep(2)
txt = '\n \ntermux-setup-storage - разрешить Termux работать с файлами на телефоне. Необходимо прописать!'
for i in txt:
    time.sleep(0.04)
    print(i, end='', flush=True)
time.sleep(2)

txt = '\npwd- узнать полный путь к директории, где вы находитесь'
for i in txt:
    time.sleep(0.04)
    print(i, end='', flush=True)
time.sleep(2)

txt = '\ncp -rf Начальный путь Конечный путь - скопировать файл/папку по указанному пути'
for i in txt:
    time.sleep(0.03)
    print(i, end='', flush=True)

time.sleep(2)

txt = '\nmv -rf Начальный_путь Конечный_путь - переместить файл/папку по указанному пути'
for i in txt:
    time.sleep(0.04)
    print(i, end='', flush=True)

time.sleep(10)
os.system('cls' if os.name == 'nt' else 'clear')

print('''
Задание 3 | Перемещение и копирование файлов

=========================

''')

time.sleep(3)
print('Файловая система:')

print('''
╦ home 
╚ Folder1
    ╠ Folder2
    ╚ File.txt
╚ Archive.7z
''')

txt = '\npwd'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)
time.sleep(2)

print('\n/data/data/com.termux/files/home')

time.sleep(3)

txt = '\ncp -rf /data/data/com.termux/files/home/storage/downloads/myfile.txt /data/data/com.termux/files/home/Folder1'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)
time.sleep(2)

time.sleep(4)
print('\n')
time.sleep(2)
txt = '\ncd Folder1'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)
time.sleep(2)
print('\n')
time.sleep(2)
txt = '\nls'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)
time.sleep(2)
print('\nmyfile.txt     Folder2     File.txt')
txt = 'clear'
for i in txt:
    time.sleep(0.3)
    print(i, end='', flush=True)
time.sleep(1)
os.system('cls' if os.name == 'nt' else 'clear')

txt ='Итак, мы научились работать с файлами! Теперь немного о том, что стоит установить дополнительно на ваш телефон. Я вам очень советую их установить, но опять же, устанавливайте по мере необходимости.\n1. Python - нужен для запуска .py файлов. Его вы уже установили, так как он нужен для работы TermuxTeacherRu.\npkg install python\npkg install python2\npkg install python3\n2. Git - нужен для копирования репозиториев с GitHub. Must have.\npkg install git\n3. Wget - скачивайте какие-либо файлы по прямой ссылке.\npkg install git\n4.Nano - редактируйте текстовые файлы прямо в терминале!\npkg install nano\n5. Unzip - архиватор для сжатия или распаковки архивов в терминале.\npkg install unzip\n6. Proot-distro - удобный инструментарий для запуска терминалов из разных дистрибутивов Linux.\npkg install proot-distro\n7. OpenSSH - поможет вам в создании SSH-соединения.\npkg install openssh\n8. Ngrok - с его помощью можно сделать локальную ссылку на сайт общедоступной, причём бесплатно.\npkg install ngrok-termux\n9. Python-pip - нужен для установки библиотек для Python.\npkg install python-pip'
for i in txt:
    time.sleep(0.03)
    print(i, end='', flush=True)
time.sleep(15)