from cryptography.fernet import Fernet
import os

# Carrega a chave secreta salva anteriormente
def load_key():
    return open("secret.key", "rb").read()

# Lista de extensões que podem ser descriptografadas
ALLOWED_EXTENSIONS = [".txt", ".pdf", ".jpg", ".docx"]

# Função de descriptografia
def decrypt_files(directory, key):
    fernet = Fernet(key)

    for root, dirs, files in os.walk(directory):
        for file in files:
            # Verifica se o arquivo tem uma extensão permitida
            if not any(file.lower().endswith(ext) for ext in ALLOWED_EXTENSIONS):
                continue

            filepath = os.path.join(root, file)
            try:
                with open(filepath, "rb") as f:
                    encrypted_data = f.read()
                decrypted_data = fernet.decrypt(encrypted_data)
                with open(filepath, "wb") as f:
                    f.write(decrypted_data)
                print(f"[+] Decrypted: {filepath}")
            except Exception as e:
                print(f"[!] Failed to decrypt {filepath}: {e}")

if __name__ == "__main__":
    key = load_key()
    target_folder = "."  # Pasta atual
    decrypt_files(target_folder, key)
