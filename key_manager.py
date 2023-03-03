from key_generator import KeyGenerator
from key import Key


class KeyManager:
    def __init__(self):
        self.key_generator = KeyGenerator()

    def generate_keypair(self, nbits: int) -> Key:
        return self.key_generator.generate_key(nbits)

    def import_public_key(self, source: Key) -> None:
        pass

    def export_public_key(self, to_export: Key) -> None:
        pass
