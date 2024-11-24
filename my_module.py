def alphavit():
    offset = 1072  # Начальное значение, с которого начинается range
    end = 32  # Количество символов в диапазоне
    d = {i - offset: chr(i) for i in range(offset, offset + end)}
    return d

# Кодируем строку в числовые коды
def encode_val(word):
    list_code = []
    d = alphavit()  # Получаем словарь символов
    reverse_d = {v: k for k, v in d.items()}  # Символ -- код

    for char in word:
        if char in reverse_d:  # Если символ есть в словаре
            list_code.append(reverse_d[char])  # Записываем его код
        else:
            list_code.append(char)  # Добавляем символ как есть
    return list_code


def normalize_code(code, d): # Приведение числового значения в диапазон словаря
    min_code = min(d.keys())
    max_code = max(d.keys())
    code_range = max_code - min_code + 1
    normalized = ((code - min_code) % code_range) + min_code  # Приведение в диапазон словаря
    return normalized

def comparator(value, key):
    len_key = len(key)
    dic = {}
    for i, val in enumerate(value):
        dic[i] = [val, key[i % len_key]]  # Привязываем к тексту ключ циклично
    return dic

def full_encode(value, key):
    dic = comparator(value, key)
    d = alphavit()
    lis = []
    for v in dic:
        if isinstance(dic[v][0], int):
            go = normalize_code(dic[v][0] + dic[v][1] + 1, d)
            lis.append(go)
        else:
            lis.append(dic[v][0])
    return lis

def full_decode(value, key):
    dic = comparator(value, key)
    d = alphavit()
    lis = []
    for v in dic:
        if isinstance(dic[v][0], int):
            go = normalize_code(dic[v][0] - dic[v][1] - 1, d)
            lis.append(go)
        else:
            lis.append(dic[v][0])
    return lis

# Преобразуем числовые коды обратно в строку
def decode_val(list_in):
    list_code = []
    d = alphavit()
    for code in list_in:
        if isinstance(code, int) and code in d:
            list_code.append(d[code])  # Находим соответствующий символ
        elif isinstance(code, str):
            list_code.append(code)
        else:
            print(f"Код '{code}' отсутствует в словаре! Оставляем без изменений.")
            list_code.append(str(code))
    return list_code