from key_generator import KeyGenerator


class EncryptingCodec:
    """
    This class is used for both encrypting and decrypting messages.
    """

    def __init__(self):
        self.keygen = KeyGenerator()

    def encrypt_message(self, sender_pubkey, sender_privkey, recipient_pubkey):
        pass

    def decrypt_message(self, sender_pubkey, recipient_pubkey):
        pass
