u"""Exemplo do capítulo 4."""


class EvenOnly(list):
    """..."""

    def append(self, integer):
        """..."""
        if not isinstance(integer, int):
            raise TypeError("Somente inteiros podem ser adicionados.")
        if integer % 2:
            raise ValueError("Somente números pares podem ser adicionados.")
        super().append(integer)
