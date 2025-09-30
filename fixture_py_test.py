from typing import assert_type
import pytest

class Fruit:
    def __init__(self, name):
        self.name = name
        # self.cubed = False

    def cube(self):
        # self.cubed = True
        pass


class FruitSalad:
    def __init__(self, *fruit_bowl):
        self.fruit = fruit_bowl
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()


# Arrange
@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana"), Fruit("Graphes"), Fruit("orange")]


def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    assert all(fruit for fruit in fruit_salad.fruit)

    assert len(fruit_salad.fruit) == 4

    assert fruit_salad.fruit[3].name == "orange"


@pytest.fixture
def first_entry():
    return "a"


# Arrange
@pytest.fixture
def order(first_entry):
    return [first_entry]


def test_string(order):
    # Act
    order.append("b")

    # Assert
    assert order == ["a", "c"]