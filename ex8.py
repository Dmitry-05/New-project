# 8 Написать функцию XOR_cipher, принимающая 2 аргумента: строку, которую нужно
# зашифровать, и ключ шифрования, которая возвращает строку, зашифрованную
# путем применения функции XOR (^) над символами строки с ключом. Написать
# также функцию XOR_uncipher, которая по зашифрованной строке и ключу
# восстанавливает исходную строку.

def XOR_cipher(string_, key):
    string_ = bytearray(string_.encode('utf-8'))
    key = key.encode('utf-8')
    for i in range(len(string_)):
        string_[i] = string_[i] ^ key[0]
    return string_.decode('utf-8')


def XOR_uncipher(string_, key):
    return XOR_cipher(string_, key)


string_ = "Some string"
key = "2"
cipher_string = XOR_cipher(string_, key)
print(cipher_string)
print(XOR_uncipher(cipher_string, key))
