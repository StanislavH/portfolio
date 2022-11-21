import socket
from map import text_map
from settings import socket_num

# сервер
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', socket_num))
clients = []  # Массив где храним адреса клиентов
print('Start Server')
while 1:
    try:
        data, addres = sock.recvfrom(1024)
        data2 = data.decode('utf-8')
    except Exception as e:
        print('ошибка получения:' + str(e))
        sock.close()
        break
    else:
        print(data2)
        if addres not in clients:
            clients.append(addres)  # Если такого клиента нету , то добавить
            i = 1
            for s in text_map:
                sock.sendto((s).encode('utf-8'), addres)  # Отправить карту игроку
                i += 1
            # Контроль доставки
            sock.sendto(("Map sent").encode('utf-8'), addres)
        for client in clients:
            if client == addres:
                continue  # Не отправлять данные клиенту, который их прислал
            sock.sendto(data, client)  # Отправить позицию игрока
        print(clients)
            # Контроль доставки
