from typing import Any


class Ajxo:
	# "Ajxo" means "thing" in Esperanto.

	def __init__(self, a: Any, b: Any) -> None:
		self.a = a
		self.b = b

	def __repr__(self) -> str:
		return self.__class__.__name__\
			+ f"({repr(self.a)}, {repr(self.b)})"


__all__ = [Ajxo.__name__]
