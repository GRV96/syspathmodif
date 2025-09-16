class Point:

	def __init__(self, x: int, y: int) -> None:
		self._x = x
		self._y = y

	def __repr__(self) -> str:
		return self.__class__.__name__\
			+ f"({self._x}, {self._y})"

	@property
	def x(self) -> int:
		return self._x

	@property
	def y(self) -> int:
		return self._y


__all__ = [Point.__name__]
