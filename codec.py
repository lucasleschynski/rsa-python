from typing import Any
from key import Key, PublicKey, PrivateKey
from utils.helpers import mod_exp


class EncryptingCodec:
    """
    This is a static class that is used for handling message encryption/decryption
    """

    @staticmethod
    def encrypt_message(message: int, recipient_public_key: PublicKey) -> int:
        """Computes ciphertext c such that c and m^e are congruent modulo n

        Args:
            message (int): message ciphertext
            recipient_public_key (PublicKey): Recipient's public key

        Returns:
            int: Encrypted message
        """
        n = recipient_public_key[0]
        e = recipient_public_key[1]
        m = message
        ciphertext = mod_exp(m, e, n)

        if ciphertext < n:
            return ciphertext
        else:
            raise ValueError("ciphertext c is greater than public key n")

    @staticmethod
    def decrypt_message(ciphertext: int, recipient_key: Key) -> Any:
        """Decrypts ciphertext to produce original message.

        Args:
            ciphertext (int): ciphertext to decrypt
            recipient_key (Key): message recipient key for decryption

        Returns:
            Any: Decrypted message in desired format
        """
        d = recipient_key.private
        print(f"d in decode: {int(d)}")
        d = int(d)
        n = recipient_key.public_key[0]
        return mod_exp(ciphertext, d, n)
