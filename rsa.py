from key_generator import KeyGenerator
from codec import EncryptingCodec
from key import Key


class RSA:
    """
    Class that encapsulates all RSA functionality.
    Allows user to:
        generate keys, encrypt/decrypt messages
    """

    def __init__(self) -> None:
        self.key_generator = KeyGenerator()
        self.message_manager = EncryptingCodec()

    def encrypt_message(self, message: str):
        pass
