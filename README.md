# 🔐 Projeto Ransomware Educacional em Python

Este projeto foi desenvolvido como parte do desafio de Cibersegurança da DIO. O objetivo é demonstrar, de forma **educacional e ética**, como funciona a criptografia de arquivos com Python.

> ⚠️ **Uso estritamente educacional. Não utilize esse código em sistemas sem autorização.**

---

## 📂 Estrutura

- `encrypter.py` → Criptografa os arquivos
- `decrypter.py` → Descriptografa os arquivos usando a chave gerada
- `secret.key` → Arquivo de chave criptográfica (gerado automaticamente)
- `/images/` → (Opcional) Capturas de tela do projeto em execução

---

## 📌 Como funciona

1. O `encrypter.py` percorre todos os arquivos da pasta onde está sendo executado e os criptografa com uma chave gerada.
2. A chave é salva em um arquivo chamado `secret.key`.
3. Para reverter, basta executar o `decrypter.py` na mesma pasta.

---

## 🛠️ Requisitos

- Python 3.x
- Biblioteca `cryptography`

Instale com:

```bash
pip install cryptography
```

▶️ Como usar

🔒 Criptografar arquivos:

```bash
python encrypter.py

```

🔓 Descriptografar arquivos:

```bash
python decrypter.py

```

📷 Capturas de tela
Crie uma pasta chamada /images e salve prints como:

```
/images/encryption_success.png  
/images/decryption_success.png
```

Use o Markdown para inserir:
```

![Criptografia concluída](images/encryption_success.png)

```
