import hashlib
#1. Hacer un Hash de una cadena de texto de 8 bits
string_8bits = "12345678"
hash_object1 = hashlib.sha256(string_8bits.encode())
hash_hex1 = hash_object1.hexdigest()

print("Hash of the 8-bit string: ", hash_hex1)

#2.Hacer un HASH de una cadena de texto de 1024 bits

string_1024bits = "1234567812345678123456781234567812345678123456781234567812345678"
hash_object2 = hashlib.sha256(string_1024bits.encode())
hash_hex2 = hash_object2.hexdigest()
print("Hash of the 1024-bit string: ", hash_hex2)

#3. Hacer un HASH de un archivo.pdf
def generate_hash(file_path):
    with open(file_path, "rb") as f:
        contents = f.read()
        hash_object = hashlib.sha256(contents)
        hash_hex = hash_object.hexdigest()
        return hash_hex

#path para el pdf
file_path = "C:/Users/franc/OneDrive/Desktop/SEG INF/SEG_INFORMATICA/Hash/pdf_folder/holamundo.pdf"
hash_hex = generate_hash(file_path)
print("Hash of the PDF file: ", hash_hex)

