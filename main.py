from my_module import encode_val , full_encode, full_decode, decode_val

if __name__ == "__main__":
    print("Добро пожаловать в программу шифрования/дешифрования!")
    print("Выберите действие:")
    print("1 - Шифр Цезаря")
    print("2 - Шифр Виженера")
    choice_shifer = input("Введите 1 или 2: ")

    if choice_shifer not in ["1", "2"]:
        print("Ошибка: вы выбрали неверный вариант. Перезапустите программу.")
        exit()

    if choice_shifer == "1":
        print("Выберите действие:")
        print("1 - Шифруем")
        print("2 - ДЕшифруем")
        choice_cezar = input("Введите 1 или 2:")

        if choice_cezar == "1":
            alphavit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            word_input = input("Введите сообщение: ")
            word = word_input.lower
            displace = int(input("Введите ключ (число): "))
            print("\nШифруем сообщение...")
            itog = ''
            for index in word_input:
                mesto = alphavit.find(index)
                new_mesto = mesto + displace
                if index in alphavit:
                    itog += alphavit[new_mesto % len(alphavit)]
                else:
                    itog += index
            print(itog)
        elif choice_cezar == "2":
            alphavit = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
            word_input = input("Введите сообщение: ")
            word = word_input.lower
            displace = int(input("Введите ключ (число): "))
            print("\nШифруем сообщение...")
            itog = ''
            for index in word_input:
                mesto = alphavit.find(index)
                new_mesto = mesto - displace
                if index in alphavit:
                    itog += alphavit[new_mesto % len(alphavit)]
                else:
                    itog += index
            print(itog)

    elif choice_shifer == "2":
        print("Выберите действие:")
        print("1 - Шифруем")
        print("2 - ДЕшифруем")
        choice_vizhener = input("Введите 1 или 2: ")
        word_input = input("Введите сообщение: ")
        word = word_input.lower()
        key_input = input("Введите ключ (слово или символы): ")
        key = key_input.lower()

        if choice_vizhener == "1":
            key_encoded = encode_val(key)
            print("\nШифруем сообщение...")
            value_encoded = encode_val(word)
            shifre = full_encode(value_encoded, key_encoded)
            shifre_text = ''.join(decode_val(shifre))
            print("Результат шифрования:", shifre_text)
        elif choice_vizhener == "2":
            key_encoded = encode_val(key)
            print("\nДешифруем сообщение...")
            encoded_text = encode_val(word)  # Кодируем сообщение в числовые коды
            decoded = full_decode(encoded_text, key_encoded)  # Дешифруем сообщение
            decode_word_list = decode_val(decoded)  # Преобразуем числовые коды обратно в текст
            print("Результат дешифрования:", ''.join(decode_word_list))

