import sqlite3

# conn = sqlite3.connect('questions.db')
# cur = conn.cursor()
# cur.execute("""CREATE TABLE IF NOT EXISTS questions(
#    id INT ,
#    quest TEXT,
#    ans TEXT);
# """)
# conn.commit()
# cur.execute("""INSERT INTO questions(id, quest, ans)
#    VALUES('1', 'Есть ли вычеты за пропуски?', 'Есть, если пропуск по уважительной причине. Т. е. есть справка по болезни, например.');""")
# cur.execute("""INSERT INTO questions(id, quest, ans)
#    VALUES('2', 'Можно ли купить одну неделю в лагере?', 'Только при наличии мест. Если на начало программы остаются свободные места, то такая возможность есть.');""")
# cur.execute("""INSERT INTO questions(id, quest, ans)
#    VALUES('3', 'Где обедают дети?', 'Дети обедают в городских точках питания, рассчитанных на такое количество людей. Это или Квант, или Пикник.');""")
# cur.execute("""INSERT INTO questions(id, quest, ans)
#    VALUES('4', 'Можно ли обедать дома?', 'Можно, если написать заявление и обеспечить ребёнку передвижение. Отводить домой возможности нет.\n
#    Приносить с собой обед можно только в отдельных случаях. Если есть проблемы со здоровьем.');""")
# cur.execute("""INSERT INTO questions(id, quest, ans)
#    VALUES('5', 'Может ли ребёнок приходить/уходить домой самостоятельно?', 'Может. Пишем заявление при оформлении в лагерь.');""")
# cur.execute("""INSERT INTO questions(id, quest, ans)
#    VALUES('6', 'Можно ли приводить детей утром раньше?', 'Не желательно. Ответственность за жизнь и здоровья ребёнка берут на себя родители в таких случаях.\n
# Программа с 9:30. В 9:00 приходят дежурные вожатые. НО в 8:00 приводить точно нельзя.');""")
# cur.execute("""INSERT INTO questions(id, quest, ans)
#    VALUES('7', 'Где дети гуляют?', 'Основное место прогулки - стадион гимназии (школа 5), площадка "Башенки" перед Байтиком и др.');""")
# cur.execute("""INSERT INTO questions(id, quest, ans)
#    VALUES('8', 'Может ли ребёнок с особенностями принимать участие в программе?', 'Нет. Данная программа не адаптирована на таких детей.');""")
# cur.execute("""INSERT INTO questions(id, quest, ans)
#    VALUES('9', 'Есть ли скидки?', 'Есть.\n\nСкидка 10% даётся:\n
# 1) По соц. категориям: потеря кормильца, семья с детьми инвалидами (но не сам участник), многодетным семьях с 4 детьми\n
# 2) если в лагерь идут два ребёнка из одной семьи, скидка действует на второго ребёнка\n
# 3) если ребёнок идёт сразу на две смены, скидка на вторую смену');""")
# cur.execute("""INSERT INTO questions(id, quest, ans)
#    VALUES('10', 'Нужна ли справка о здоровье?', 'Нет. Но сообщить об особенностях ребёнка обязательно! (аллергии и т. д.)');""")
# cur.execute("""INSERT INTO questions(id, quest, ans)
#    VALUES('11', 'Какой распорядок дня?', 'Кратко:\n
# Начало в 9:30. Зарядка. Далее в первую половину дня идут занятия по разным направлениям согласно заданной тематики. Есть ланч.\n
# Обед ок. 13:30\n
# После обеда прогулки, творческие вечера, спортивные игры. Чай. Домой в 17:30.');""")
# cur.execute("""INSERT INTO questions(id, quest, ans)
#    VALUES('12', 'Что дают на ланч и чаепитие?', 'Печенье, фрукты (яблоки, бананы), кексы, вафли');""")
# cur.execute("""INSERT INTO questions(id, quest, ans)
#    VALUES('13', 'Какие педагоги?', '1. смена: Булатова Татьяна, Борисова Юлия, Кроливец Татьяна (комп), Новикова Елена (комп)\n
# 2. смена: Булатова Татьяна, Борисова Юлия, Денисова Елена (комп), Новикова Елена (комп)
# Куратор: Ионкина Наталья \n\n+ вожатые\n
#
# Дети разделены на отряды. У каждого отряда свой педагог и вожатые.');""")
# cur.execute("""INSERT INTO questions(id, quest, ans)
#    VALUES('14', 'Какие условия оплаты?', 'Лучше оплатить всё сразу. Если нет возможности, то:\n
# - 5000 руб. - предоплата при заключении договора. Срок невозврата предоплаты 14 календарных дней до начала программы\n
# - полная оплата за 7 календарных дней до начала программы\n
# - обеды оплачиваются отдельно (информация уточняется)');""")
# cur.execute("""INSERT INTO questions(id, quest, ans)
#    VALUES('15', 'Какие документы нужны для оформления?', '- Договор (у администратора)\n
# - Согласие на обработку персональных данных (у администратора)\n
# - Разрешение на фото- и видео-съёмку (у администратора)\n
# - Сопровождение на обеды (у администратора)\n
# - Разрешение ходить самостоятельно (у администратора)\n
# - Свидетельство о рождении (родитель)\n
# - Медицинский полис (родитель)');""")
# conn.commit()


conn = sqlite3.connect('db_data/questions_and_courses.db')
cur = conn.cursor()
cur.execute("""CREATE TABLE IF NOT EXISTS courses0(
   id INT ,
   name TEXT,
   description TEXT,
   link TEXT);
""")
cur.execute("""CREATE TABLE IF NOT EXISTS courses1(
   id INT ,
   name TEXT,
   description TEXT,
   link TEXT);
""")
cur.execute("""CREATE TABLE IF NOT EXISTS courses5(
   id INT ,
   name TEXT,
   description TEXT,
   link TEXT);
""")
conn.commit()


with open('mama_and_malish.txt', 'r', encoding='utf-8') as f:
    text_mama_and_malish = f.read()

lst0 = [['МАМА И МАЛЫШ', f'{text_mama_and_malish}', 'https://bytic.ru/courses/leto-2023/mama-i-malyish-leto.html'],
        ['СОЗДАЙ СВОЙ МУЛЬТФИЛЬМ НА КОМПЬЮТЕРЕ',
         'На занятиях ваш ребенок узнает, что такое алгоритм, спрайт, цикл, научится создавать программы, рисовать в графическом редакторе, записывать звук - все это поможет ему сделать первые шаги в мультипликации.',
         'https://bytic.ru/courses/leto-2023/sozdaj-svoj-multfilm-na-kompyutere.html'],
        ['РОБОТОТЕХНИКА LEGО ДЛЯ ДОШКОЛЬНИКОВ',
         'На занятиях вместе с педагогом дети создадут своих роботов, познакомятся с работой моторов и датчиков. Освоят базовые принципы программирования и научатся создавать алгоритмы в графической среде WEDO.',
         'https://bytic.ru/courses/leto-2023/robototexnika-lego-dlya-doshkolnikov.html'],
        ['КЕРАМИКА И РОСПИСЬ',
         'На каждом занятии будем работать с глиной и создавать неповторимые изделия (игрушки, посуду, статуэтки и многое другое), изучим различные техники лепки и росписи керамических изделий.\nВсе работы будут обожжены в профессиональной муфельной печи.\nЛепка из глины — это увлекательный процесс, который развивает моторику рук, успокаивает нервную систему и помогает развитию воображения.',
         'https://bytic.ru/courses/leto-2023/keramika-i-rospis.html'],
        ['КАЛЛИГРАФИЯ',
         'Письмо – это навык, который требует умения сосредоточиться, координировать свои движения, точную работу мышц кисти руки.',
         'https://bytic.ru/courses/leto-2023/kalligrafiya-leto.html'],
        ['ЭКСПРЕСС-ПОДГОТОВКА К ШКОЛЕ', 'Наша цель: максимально эффективно подготовить ребенка к школе. Занимаясь с педагогом в малой группе (до 6 человек), ребенок учится правильно развивать ход своих мыслей.', 'https://bytic.ru/courses/leto-2023/ekspress-podgotovka-k-shkole.html'],
        ['РАЗГОВАРИВАЮ ПРАВИЛЬНО', 'На занятиях мы будем отрабатывать навыки осмысленного чтения, а с помощью составления рассказов по сюжетным картинкам развивать логику и наблюдательность.', 'https://bytic.ru/courses/leto-2023/razgovarivayu-pravilno.html'],
        ['РИСОВАНИЕ ПЕСКОМ', 'Песочное рисование – это рисование картин движениями рук на специальном стеклянном столе при помощи света и тени. Это не только современный вид творчества, но и эффективный метод, помогающий развить внутренний мир ребенка', 'https://bytic.ru/courses/doshkolnoe-otdelenie/risovanie-peskom.html'],
        ]

with open('KODY_GAME_LAB.txt', 'r', encoding='utf-8') as f:
    kody = f.read()

lst1 = [['ГЕЙМ ДИЗАЙН В ROBLOX STUDIO', 'На летних каникулах приглашаем ребят погрузиться в увлекательный мир разработки игр и сделать первый шаг к освоению востребованной профессии!\nОсвоим базовые инструменты для разработки игр в ROBLOX Studio и узнаем основы языка программирования Lua.', 'https://bytic.ru/courses/leto-2023/gejm-dizajn-v-roblox-studio.html'],
    ['COSPACES И ROBLOX STUDIO', 'На летних каникулах приглашаем ребят погрузиться в мир виртуальной реальности, создать свои собственные 3D-миры, а также поработать в ROBLOX Studio и изучить основы языка программирования Lua.', 'https://bytic.ru/courses/leto-2023/cospaces-i-roblox-studiokopiya-scratch,-lego-wedo-2.0.html'],
    ['SCRATCH + LEGO WEDO 2.0 (ПРОГРАММИРОВАНИЕ + РОБОТОТЕХНИКА)', 'Мы будем программировать в Scratch, это блочный визуальный язык программирования, похожий на конструктор LEGO, а также собирать роботов из настоящих кубиков и программировать их.', 'https://bytic.ru/courses/leto-2023/scratch,-lego-wedo-2.0.html'],
    ['BRAWL STARS, ROBLOX, MINECRAFT', 'Мы окунемся в мир создания игр, программирования и 3D-моделирования. Мы построим свой трехмерный мир, запрограммируем игру c героем Minecraft и создадим 3D-героя.', 'https://bytic.ru/courses/leto-2023/brawl-stars,-roblox,-minecraft.html'],
    ['KODU GAME LAB, COSPACES EDU, LEGO WEDO 2.0', f'{kody}', 'https://bytic.ru/courses/leto-2023/kopiya-czifrovoj-xudozhnik.html'],
    ['РИСОВАНИЕ ПЕСКОМ', 'Песочное рисование – это рисование картин движениями рук на специальном стеклянном столе при помощи света и тени. Это не только современный вид творчества, но и эффективный метод, помогающий развить внутренний мир ребенка', 'https://bytic.ru/courses/doshkolnoe-otdelenie/risovanie-peskom.html'],
    ['РОБОТОТЕХНИКА LEGО. КОСМИЧЕСКИЕ ПРИКЛЮЧЕНИЯ', 'Можно ли обойтись без роботов в космосе? Какую работу они там выполняют? Что умеют современные роботы? Узнаем ответы на эти и другие вопросы на наших летних занятиях. Мы соберем космических роботов и научимся управлять ими.', 'https://bytic.ru/courses/leto-2023/robototexnika-lego-dlya-doshkolnikov.html'],
]

with open('Russian_language.txt', 'r', encoding='utf-8') as f:
    Rus = f.read()
with open('Math.txt', 'r', encoding='utf-8') as f:
    math = f.read()

lst5 = [['МАТЕМАТИКА', f'{math}', 'https://bytic.ru/courses/leto-2023/kopiya-matematika.html'],
    ['РУССКИЙ ЯЗЫК', f'{Rus}', 'https://bytic.ru/courses/leto-2023/russkij-yazyik.html'],
    ['ОСНОВЫ 3D ГРАФИКИ В ПРОГРАММЕ BLENDER', 'Профессиональные 3D-художники используют Blender для создания компьютерной графики. Программа позволяет моделировать интерьеры и персонажей, настраивать освещение, симулировать физику и частицы. С помощью инструментов Blender можно создать масштабные сцены для виртуальной реальности, фильмов и игр.\nНа занятиях вы создадите 3D-модель, узнаете основы скульптинга, будете настраивать освещение, поработаете с текстурами и материалами.', 'https://bytic.ru/courses/leto-2023/osnovyi-3d-grafiki-v-programme-blender.html'],
    ['ЦИФРОВОЙ ХУДОЖНИК', 'Курс подойдет тем ребятам, кто очень хочет попробовать свои силы в цифровом дизайне, по пока не знает, с чего начать.\nОсвоив ключевые инструменты профессиональной программы Adobe Illustrator, вы создадите свои первые digital art шедевры!', 'https://bytic.ru/courses/leto-2023/czifrovoj-xudozhnik.html'],
    ['ГЕЙМ ДИЗАЙН В ROBLOX STUDIO', 'На летних каникулах приглашаем ребят погрузиться в увлекательный мир разработки игр и сделать первый шаг к освоению востребованной профессии!\nОсвоим базовые инструменты для разработки игр в ROBLOX Studio и узнаем основы языка программирования Lua.', 'https://bytic.ru/courses/leto-2023/gejm-dizajn-v-roblox-studio.html'],
    ['COSPACES И ROBLOX STUDIO', 'На летних каникулах приглашаем ребят погрузиться в мир виртуальной реальности, создать свои собственные 3D-миры, а также поработать в ROBLOX Studio и изучить основы языка программирования Lua.', 'https://bytic.ru/courses/leto-2023/cospaces-i-roblox-studiokopiya-scratch,-lego-wedo-2.0.html'],
        ['ИНЖЕНЕРНЫЙ ДИЗАЙН', 'На занятиях мы будем читать чертежи и создадим по ним трехмерные детали. Сделаем компьютерную сборку деталей и напечатаем их на 3D-принтере.  Мы поработаем с измерительными инструментами. Проведем замеры и выполним обратное проектирование деталей.', 'https://bytic.ru/courses/leto-2023/inzhenernyij-dizajn.html']]
for i in range(len(lst0)):
    cur.execute(f"""INSERT INTO courses0(id, name, description, link)
       VALUES({i}, '{lst0[i][0]}', '{lst0[i][1]}', '{lst0[i][2]}');""")
for i in range(len(lst1)):
    cur.execute(f"""INSERT INTO courses1(id, name, description, link)
       VALUES({i}, '{lst1[i][0]}', '{lst1[i][1]}', '{lst1[i][2]}');""")
for i in range(len(lst5)):
    cur.execute(f"""INSERT INTO courses5(id, name, description, link)
       VALUES({i}, '{lst5[i][0]}', '{lst5[i][1]}', '{lst5[i][2]}');""")
conn.commit()