import socket
import threading
import map
import player
import settings
from settings import *


# клиент
def start():
    def read_sok():
        while True:
            try:
                data, addres = sor.recvfrom(1024)
                data2 = data.decode('utf-8')
                print(data2)
            except Exception as e:
                print('ошибка подключения')
            else:
                if data2[0] == '0':
                    get_name = data2[data2.find('[') + 1:data2.find(']')]
                    x = data2[data2.find('(') + 1:data2.find(',')]
                    y = data2[data2.find(',') + 1:data2.find(')')]
                    angle = data2[data2.find(')') + 1:]
                    gamers[get_name] = {'name': get_name, 'pos': {'x': float(x), 'y': float(y), 'angle': float(angle)}}

    # name = input("Введите ваше имя")
    sor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sor.bind(('', 0))  # Задаем сокет как клиент
    s = (name + ' Connect to server').encode('utf-8')
    sor.sendto(s, server)  # Уведомляем сервер о подключении
    send_pos(player_pos[0], player_pos[1], player_angle, server, name, sor)
    data = sor.recv(1024).decode('utf-8')
    map.text_map.clear()
    map.world_map.clear()
    while data != "Map sent":
        map.text_map.append(data)
        data = sor.recv(1024).decode('utf-8')
    print(map.text_map)
    map.get_map()
    potok = threading.Thread(target=read_sok, daemon=True).start()


def send_pos(x, y, angle, server=server, name=name, sor=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)):
    try:
        s = ('0[' + name + ']:(' + str(x) + ',' + str(y) + ')' + str(angle)).encode('utf-8')
        sor.sendto(s, server)
    except Exception as e:
        print('ошибка отправки:' + str(e))
