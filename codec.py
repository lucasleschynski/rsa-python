from key_generator import KeyGenerator
from key import Key, PublicKey, PrivateKey


class EncryptingCodec:
    """
    This class is used for both encrypting and decrypting messages.
    """

    def __init__(self):
        pass

    def encrypt_message(self, sender_key: Key, recipient_public_key: PublicKey):
        pass

    def decrypt_message(self, sender_key: Key, recipient_public_key: PublicKey):
        pass
