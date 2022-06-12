import hashlib

def verification(message,public,podpis):# Функция для проверки подписи
    mhash = int(hashlib.sha256(message.encode()).hexdigest(), 16)# Хэшируем сообщение
    mhash = int(bin(mhash)[2:])# Бинарим хэшированное сообщение
    mhash = str(mhash)
    q = len(mhash)
    check=[]# Здесь храним созданную(новую) подпись, для проверки на подлинность
    podpis_hex=[]# Здесь храним хэшированную (оригинальную) подпись
    r=0
    l=len(podpis)

    for i in range(q):
        #Создадим (новую) подпись ,по открытому ключу
        if mhash[i]==str(0):
           check.append(public[r])
        if mhash[i]==str(1):
            check.append(public[r+1])
        r=r+2

    for i in range(l):
        podpis_hex.append(int(bin(int(hashlib.sha256(str(podpis[i]).encode()).hexdigest(), 16))[2:]))
        #Хэшируем и бинарим (оригинальную) подпись

    if check != podpis_hex:#Сравниваем (оригинальную) подпись и (новую)
            return False
    return True# Если подписи совпадают, то значит сообщение является действительным

def make_podpis(mhash,keys):# Функция, для создания подписи
                    # из сообщения и секретного ключа

    mhash = str(mhash)# Cообщение(хэшированное+бинарное)
    q=len(mhash)
    podpis = []# Здесь храним подпись
    r=0

    for i in range(q):
        if mhash[i]==str(0):#Если бит в хеше сообщения равен нулю то,
                  # берём первое число из пары секретного ключа
           podpis.append(keys[r])

        if mhash[i]==str(1):#Если бит в хеше сообщения равен единице то,
                  # берём второе число из пары секретного ключа
            podpis.append(keys[r+1])
        r=r+2

    return podpis#Возврощаем подпись



def keys_pub( keys_privat ):# Функция, для создания открытого ключа
                            # из секретного
    keys_pub=[]
    l=len(keys_privat)

    for i in range(l):
        keys_pub.append([0] * l)

    for i in range(l):
        keys_pub[i] = int(bin(int(hashlib.sha256(str(keys_privat[i]).encode()).hexdigest(), 16))[2:])
        #Хэшируем и бинарим секретный ключ
    return keys_pub# Возврощаем открытый ключ

def keys_privat_read():# Функция, где мы считываем сгениривованный ключ
                       # из первой лаб.работы
    file = open("keys.txt", "r")
    listt = []
    keys_privat = []# Здесь мы будем хранить секретный ключ

    while True:
        line = file.readline()
        if not line:
            break
        listt.append(line.strip())
    l= len(listt)

    for i in range(l):
        keys_privat.append([0] * l)
    for i in range(l):
        keys_privat[i] = int(listt[i])

    return keys_privat# Возворащем секретный ключ

#Начало программы
keys_privat = keys_privat_read()# Вызываем функцию, для считывания секретного ключа
keys_pub=keys_pub(keys_privat)# Вызываем функцию, для создания открытого ключа
print("=========================================================")
message=input("Введите текст: ")# Вводим сообщение
mhash = int(hashlib.sha256(message.encode()).hexdigest(), 16)# Хэшируем сообщение
mhash = int(bin(mhash)[2:])# Бинарим сообщение
print("Хеш-функция сообщения: ",mhash)
podpis=make_podpis(mhash,keys_privat)# Вызываем функцию, для создания подписи
print("Подпись сообщения :",podpis)
print("Подпись соотвествует сообщению: ",verification(message,keys_pub,podpis))# Вызываем функцию,
                                                                   # для проверки подписи
print("=========================================================")