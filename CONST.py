bytic_address_1 = 'Сиреневый бульвар, 11, Троицк, Москва'  # адрес байтика на сиреневом
bytic_address_2 = 'микрорайон В, 39, Троицк, Москва'  # адрес байтика на сиреневом
geocoder_uri = "http://geocode-maps.yandex.ru/1.x/"  # для запроса статик апи


MAIN_MENU, MENU_1, MENU_5, QUE_1, QUE_5 = range(5)  # для возврата CommandHandler'а
MENU_1_1, MENU_1_2 = 11, 12  # для вызова ф-ций menu_1_1 и menu_1_2
GROUPS_1 = 'groups_1_4'  # для вызова ф-ции groups_1
COURSES = 121  # для ф-ции курсов 1-4 классов
ADDRESS = 'address'

TOKEN = '6013111011:AAF8HwDbWB22mjumWf5i3spHsslf3tnjFh8'  # токен бота


# расписание нахождения в Байтике для смен
with open('ordinary.txt', 'r', encoding='utf-8') as ordinar:
    ordinary = ordinar.read()

# описание летних смен (1-й и 2-й)
with open('description_1.txt', 'r', encoding='utf-8') as desk:
    desk_1 = desk.read()
# with open('description_2.txt', 'r', encoding='utf-8') as desk:
#     desk_2 = desk.read()
