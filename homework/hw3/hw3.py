'''
1. Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
2. В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из документации к языку.
3. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
'''
import string

a = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

text1 = '«City of Blinding Lights» (с англ. — «Город ослепительных огней»[3]) — песня ирландской рок-группы U2, четвёртый сингл из альбома How to Dismantle an Atomic Bomb (2004). Композиция была спродюсирована Марком «Фладом» Эллисом при поддержке Криса Томаса и Джекнайфа Ли. «City of Blinding Lights» стала хитом в Канаде и ряде европейских стран, добравшись до верхней строчки чарта Испании, а также отметившись в Top-10 Ирландии и Великобритании. Она была хорошо принята критиками и выиграла премию «Грэмми» в номинации «Лучшая рок-песня» на церемонии 2006 года. Первоначальная версия песни была написана гораздо раньше её релиза — в период сессий для альбома Pop (1997). Отчасти её текст был вдохновлён воспоминаниями фронтмена группы — Боно — о его первой поездке в Лондон (будучи подростком) и участников квартета во время выступления в Нью-Йорке в период после терактов 11 сентября, отчасти — затрагивала отношения фронтмена с его женой Элисон  (англ.)рус.. Основная идея песни посвящена утраченной невинности, эта тема была вдохновлена ретроспективным взглядом Боно на самого себя начала 1980-х. Высказываясь о звучании композиции, критики часто проводили параллели с творчеством группы времён пластинки The Unforgettable Fire (1984) и, в частности, c синглом «Where the Streets Have No Name» (1987). Публичный дебют песни состоялся во время гастрольного тура Vertigo Tour  (англ.)рус., зачастую её выбирали открывающей шоу, и с тех пор группа исполняет эту композицию практически на каждом своём концерте. «City of Blinding Lights» звучала в эпизодах сериалов «Симпсоны» и «Красавцы», а также в фильме «Дьявол носит Prada». Барак Обама использовал эту песню в ходе своих предвыборных кампаний 2008 и 2012 годов[4][5], и называл её одним из своих любимых музыкальных произведений[6]. В 2009 году U2 исполнили её во время концерта, посвящённого инаугурации президента  (англ.)рус.[7].'

''' Словарь с количеством повторений каждого слова, оттуда берутся те, где количество больше 1 - возможно использовать и для задачи 2'''

def repeatables (list1):
    uniques = list(set(list1))
    repetitions_dict = {}
    for unique in uniques:
        count = 0
        for item in list1:
            if unique == item:
                count += 1
        repetitions_dict.update({unique : count})
    repetitions = list(k for k, v in repetitions_dict.items() if v !=1)
    return repetitions

def replace_punctuation(text):
    for char in text:
        if char in string.punctuation:
            text = text.replace(char, " ")
    return text

def top_num_words (text, num):
    text = text.lower()
    list1 = replace_punctuation(text).split(" ")
    uniques = list(set(list1))
    uniques = list(filter(None, uniques))
    repetitions_dict = {}
    for unique in uniques:
        count = 0
        for item in list1:
            if unique == item:
                count += 1
        repetitions_dict.update({unique: count})
    sorted_repetitions = sorted(repetitions_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_repetitions[0:num]

def pack_backpack(items, max_weight):
    possible_items = []
    for item, weight in items.items():
        if weight <= max_weight:
            possible_items.append(item)
            max_weight -= weight
    return possible_items

print(repeatables(a))
      
print (top_num_words(text1, 10))

items = {'laptop': 3, 'water': 3, 'food': 2, 'clothes': 2, 'tent': 8, 'first aid kit': 1}
max_weight = 10
print(pack_backpack(items, max_weight))