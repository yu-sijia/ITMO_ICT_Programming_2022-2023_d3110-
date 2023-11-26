def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext=""
    for word in plaintext:
        if word.isupper():
            ciphertext += chr((ord(word) - 65 + shift) % 26 + 65)
        elif word.islower():
            ciphertext += chr((ord(word) - 97 + shift) % 26 + 97)
        else:
            ciphertext = ciphertext + word
    return ciphertext
a=encrypt_caesar("train")
print("Шифруем слово train, получаем слово: ", a)
a=encrypt_caesar("python")
print("Шифруем слово train, получаем слово: ", a)
a=encrypt_caesar("Python3.6")
print("Шифруем слово train, получаем слово: ",a)

def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext=""
    for word in ciphertext:
        if word.isupper():
            #公式P=(C-3) mod 26
            plaintext += chr((ord(word) - 65 - shift) % 26 + 65)
        elif word.islower():
            plaintext += chr((ord(word) - 97 - shift) % 26 + 97)
        else:
            plaintext = plaintext + word
    return plaintext
a=decrypt_caesar("wudlq")
print("Шифруем слово train, получаем слово: ", a)
a=decrypt_caesar("sbwkrq")
print("Шифруем слово train, получаем слово: ", a)

a=decrypt_caesar("Sbwkrq3.6")
print("Шифруем слово train, получаем слово: ", a)
