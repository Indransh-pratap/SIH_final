from cryptography.fernet import Fernet

key = Fernet.generate_key().decode()

with open(r"D:\SIH final\SIH_final\mysite\.env", "w") as f:
    f.write(f"ENCRYPTION_KEY={key}")
