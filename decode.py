import string

ciphertext = bytes.fromhex("16112b141173380a01150721122e15366d0504020337145c002e151f0734302d1f5f143021291d1c")

known_plain = b"THM{"

key_partial = [ciphertext[i] ^ known_plain[i] for i in range(4)]

print(f"Partial key (first 4 bytes): {''.join(chr(k) for k in key_partial)}")

charset = string.ascii_letters + string.digits

print("\nTrying all alphanumeric candidates for key[4]:\n")
for c in charset:
    key = bytes(key_partial + [ord(c)])
    decrypted = bytes(ciphertext[i] ^ key[i % 5] for i in range(len(ciphertext)))
    try:
        text = decrypted.decode('utf-8')
        if text.startswith("THM{") and text.endswith("}"):
            print(f"KEY FOUND: {''.join(chr(k) for k in key)}")
            print(f"   Decrypted content: {text}\n")
    except:
        pass
