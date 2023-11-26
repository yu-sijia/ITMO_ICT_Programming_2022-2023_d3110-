def VigenereEncrypto(message, key):
    msLen = len(message)
    keyLen = len(key)
    message = message.upper()
    key = key.upper()
    raw = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""
    for i in range(0, msLen):
        j = i % keyLen
        if message[i] not in raw:
            ciphertext += message[i]
            continue
        encodechr = chr((ord(message[i]) - ord("A") + ord(key[j]) - ord("A")) % 26 + ord("A"))
        ciphertext += encodechr
    return ciphertext

def VigenereDecrypto(ciphertext, key):
    msLen = len(ciphertext)
    keyLen = len(key)
    key = key.upper()
    raw = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    plaintext = ""
    for i in range(0, msLen):
        j = i % keyLen
        if ciphertext[i] not in raw:
            plaintext += ciphertext[i]
            continue
        decodechr = chr((ord(ciphertext[i]) - ord("A") - ord(key[j]) - ord("A")) % 26 + ord("A"))
        plaintext += decodechr
    return plaintext

text = VigenereEncrypto("PYTHON", "A")
print("Шифруем слово train, получаем слово: ", text)
text = VigenereEncrypto("python", "a")
print("Шифруем слово train, получаем слово: ", text)
text = VigenereEncrypto("ATTACKATDAWN", "LEMON")
print("Шифруем слово train, получаем слово: ", text)
text = VigenereDecrypto("PYTHON", "A")
print("Шифруем слово train, получаем слово: ", text)
text = VigenereDecrypto("python", "a")
print("Шифруем слово train, получаем слово: ", text)
text = VigenereDecrypto("LXFOPVEFRNHR", "LEMON")
print("Шифруем слово train, получаем слово: ", text)

