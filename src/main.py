import time
import requests
import webbrowser

num = ['первый', 'второй', 'третий', 'четвертый', 'пятый']
name = ['Коронавирус', 'Еда ВК', 'Шаги ВК', 'ТНТ', 'Спорт ВК']
ids = ['7362610', '7695875', '7539087', '7857880', '7297191']
toks = []

print('''Привет
Это скрипт, который будет автоматически сменять эмодзи-статусы
Сначала тебе нужно получить шесть токенов.
Токены действуют 24 часа, так что потом придется получать новый
''')

vrem = int(input('Введите время между сменами (в секундах): '))

for i in range(5):
    print(f'''
Получаем {num[i]} токен ({name[i]})''')
    time.sleep(3)
    webbrowser.open(
        f'https://oauth.vk.com/authorize?client_id={ids[i]}&scope=1024&redirect_uri=https://oauth.vk.com/blank.html'
        f'&display=page&response_type=token&revoke=1',
        new=1, autoraise=True)
    tt = input(f'Введите {num[i]} токен (от = до &): ')
    toks.append(tt)
print('Запущено... Если что-то не работает, пишите мне в ВК vk.com/cry.crystal')
try:
    while True:
        for sid in range(1, 317):
            tt = 'no'
            if (0 < sid < 40) or (122 < sid < 126) or (sid == 127) or (130 < sid < 134) or (sid == 135) or (
                    sid == 136) or (137 < sid < 141):
                tt = toks[0]
            elif (171 < sid < 180) or (208 < sid < 217):
                tt = toks[1]
            elif 197 < sid < 205:
                tt = toks[2]
            elif 242 < sid < 248:
                tt = toks[3]
            elif (217 < sid < 242) or (sid == 249) or (291 < sid < 315):
                tt = toks[4]
            if tt != 'no':
                req = requests.get(
                    'https://api.vk.com/method/status.setImage?access_token=' + tt + '&v=5.123&status_id=' + str(sid))
                time.sleep(vrem)
except:
    print('error?')
