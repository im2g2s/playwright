from cryptography.fernet import Fernet
class EncryptDecrypt:
    @staticmethod
    def decrypted_text(str):
        key_str = '7UOOeXBDSgXNsE5BOTp2v5IrEFMjy0tOPuP78hPlsrg='
        key = bytes(key_str, 'utf-8')
        f = Fernet(key)
        arr = bytes(str, 'utf-8')
        userPassDecrypted = f.decrypt(arr)
        pwd = userPassDecrypted.decode()
        return pwd