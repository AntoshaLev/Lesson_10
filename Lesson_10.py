# Задание_1
class Matrix:
    def __init__(self, matrix_data):
        self.__matrix = matrix_data

        m_rows = len(self.__matrix)
        self.__matrix_size = frozenset([(m_rows, len(row)) for row in self.__matrix])

        if len(self.__matrix_size) != 1:
            raise ValueError("Invalid matrix size")

    def __add__(self, other: "Matrix") -> "Matrix":

        if self.__matrix_size != other.__matrix_size:
            raise ValueError(f"Matrix sizes difference")

        result = []

        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])

        return Matrix(result)

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])


if __name__ == '__main__':
    matrix1 = Matrix([[1, 4], [8, 8]])
    print(matrix1)

    matrix2 = Matrix([[10, 20], [30, 40]])
    print(matrix2)

    print(matrix1 + matrix2)

# Задание 2

from abc import ABC, abstractmethod

from typing import Any


class AbstractClothes(ABC):

    @property
    @abstractmethod
    def tissue_required(self):
        pass

    @property
    @abstractmethod
    def measuring(self):
        pass

    @abstractmethod
    def _calc_tissue_required(self):
        pass


class Clothes(AbstractClothes):
    _clothes = []

    def __init__(self, name: str, measuring: Any):
        self.name = name
        self._measuring = measuring
        self._tissue_required = None

        self._clothes.append(self)

    def _calc_tissue_required(self):
        raise NotImplemented

    @property
    def tissue_required(self) -> float:
        if not self._tissue_required:
            self._calc_tissue_required()

        return self._tissue_required

    @property
    def measuring(self) -> Any:
        return self._measuring

    @measuring.setter
    def measuring(self, measuring: Any):
        self._measuring = measuring
        self._tissue_required = None

    @property
    def total_tissue_required(self):
        return sum([item.tissue_required for item in self._clothes])


class Coat(Clothes):

    def _calc_tissue_required(self):
        self._tissue_required = round(self.measuring / 6.5 + 0.5, 2)

    @property
    def V(self) -> Any:
        return self.measuring

    @V.setter
    def V(self, size: Any):
        self.measuring = size

    def __str__(self):
        return f"Для пошива пальто {self.measuring} размера " \
               f"требуется {self.tissue_required} кв. метров ткани"


class Suit(Clothes):

    def _calc_tissue_required(self):
        self._tissue_required = round(2 * self.measuring * 0.01 + 0.3, 2)

    @property
    def H(self) -> Any:
        return self.measuring

    @H.setter
    def H(self, height: Any):
        self.measuring = height

    def __str__(self):
        return f"Для пошива костюма на рост {self.measuring} см. " \
               f"требуется {self.tissue_required} кв. метров ткани"


coat = Coat('Пальто', 9)
print(coat)
coat.V = 12
print(coat)

suit = Suit('Костюм', 168)
print(suit)
suit.H = 175
print(suit)


# Задание 3
class Cell:
    def __init__(self, count: int):
        self._count = count

    def __add__(self, other: "Cell") -> "Cell":
        return Cell(self._count + other._count)

    def __sub__(self, other: "Cell") -> "Cell":
        if self._count > other._count:
            return Cell(self._count - other._count)

        print(f"{self._count} - {other._count}: impossible operation")

    def __mul__(self, other: "Cell") -> "Cell":
        return Cell(self._count * other._count)

    def __truediv__(self, other: "Cell") -> "Cell":
        return Cell(self._count // other._count)

    def make_order(self, per_row: int) -> str:
        rows, tail = self._count // per_row, self._count % per_row
        return '\n'.join(['*' * per_row] * rows + (['*' * tail] if tail else []))

    def __str__(self) -> str:
        return f"Клетка состоит из {self._count} ячеек"


c1 = Cell(17)
c2 = Cell(13)
print(c1)
print(c2)

print(c1 + c2)
print((c1 + c2).make_order(8))
