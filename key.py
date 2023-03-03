from typing import Tuple

PublicKey = Tuple[int, int]
PrivateKey = int


class Key:
    def __init__(
        self, public_key: PublicKey, private_key: PrivateKey, nbits: int
    ) -> None:
        """This class represents a keypair (public + private key) as a single object

        Args:
            public_key (tuple[int, int]): Tuple containing n and e values
            private_key (int): d value
            nbits (int): Number of bits
        """
        self.public_key = public_key
        self.private = private_key
        self.nbits = nbits
