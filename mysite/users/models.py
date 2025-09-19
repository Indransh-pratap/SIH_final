from django.db import models
from .utils_crypto import encrypt_text, decrypt_text

class UserData(models.Model):
    _name = models.TextField()
    _email = models.TextField()

    @property
    def name(self):
        return decrypt_text(self._name) if self._name else None

    @name.setter
    def name(self, value):
        self._name = encrypt_text(value)

    @property
    def email(self):
        return decrypt_text(self._email) if self._email else None

    @email.setter
    def email(self, value):
        self._email = encrypt_text(value)
