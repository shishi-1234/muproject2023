print('Добро пожаловать!', '\n', 'Тебе нужно выбраться из дома!')

choice = input('Выбери куда отправишься дальше? (кухня, спальня, кладовая, подвал): ')

health = 100
print('health=', health)

def window():
    print('Упс! Под окном находилась ловушка!', 'health=', health - 20)
    print('Но вы смогли успешно выбраться')
def error():
    print('я не понимаю что здесь написанно')
def basem():
    print('Вы проиграли! В подвале вас убили')
def kitchen():
    print('Отличный выбор! Вы нашли еду и оружие: нож')
    choice2 = input('Дальше выбор из таинственной двери и окна: ')

    if choice2 == 'таинственная дверь':
        print('Это был выход! Отлично')
    elif choice2 == 'окно':
        window()
    else:
        error()

if choice == 'кухня':
    kitchen()

elif choice == 'спальня':
    print('В спальне ничего не оказалось')
    ch = input('куда дальше? (окно, дверь в другую комнату) ')
    if ch == 'окно':
        window()
    elif ch == 'дверь':
        print('Это был подвал')
        basem()
    else:
        error()

elif choice == 'подвал':
    basem()
elif choice == 'кладовая':
    print('Отличный выбор! Тут вы нашли огромное количество оружие')
    ch2 = input('Что будете делать? Спрататься здесь/ отправиться на кухню ')
    if ch2 == 'кухня':
        kitchen()
    elif ch2 == 'спрятаться':
        print('Вы спрятались среди вещей, но спустя некоторе время Вы услышали приближающиеся шаги')
        cho = input('Что будете делать? Сидеть тихо/ взять оружие и напасть')
        if cho == 'сидеть':
            print('Он зашел в кладовую и заметил вас. Вы проиграли')
        elif cho == "напасть":
            print('Он неожидал этого, поэтому Вы смогли победить его хоть и с травмами','health=', health - 50)
            print('Вы решили отпраиться на кухню')
            kitchen()
        else:
            error()
    else:
        error()
else:
    error()