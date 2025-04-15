from rectangles import Rectangle
from points import Point
import pytest

#pozwoliłem sobie nie testować funkcji które testowaliśmy we wcześniejszych zadaniach bo sprowadzało by się to do przepisywania 
#tego samego w innej konwencji. Mam nadzieje że to nie problem :)

@pytest.fixture
def recA():
    return Rectangle(1, 2, 3, 4)

@pytest.fixture
def recB():
    return Rectangle(2, 2, 4, 6)

def test_init():
    with pytest.raises(ValueError, match="nieprawidłowe punkty"):
        Rectangle(10, 10, 5, 5)

def test_from_points(recA, recB):
    assert recA == Rectangle.from_points(Point(1, 2), Point(3, 4))
    assert recB == Rectangle.from_points(Point(2, 2), Point(4, 6))
    with pytest.raises(ValueError, match="nieprawidłowe punkty"):
        Rectangle.from_points(Point(4, 4), Point(2, 2))

def test_center(recA, recB):
    assert recA.center == Point(2, 3)
    assert recB.center == Point(3, 4)

def test_bottom(recA, recB):
    assert recA.bottom == 2
    assert recB.bottom == 2

def test_top(recA, recB):
    assert recA.top == 4
    assert recB.top == 6

def test_left(recA, recB):
    assert recA.left == 1
    assert recB.left == 2

def test_right(recA, recB):
    assert recA.right == 3
    assert recB.right == 4

def test_topright(recA, recB):
    assert recA.topright == Point(3, 4)
    assert recB.topright == Point(4, 6)

def test_bottomleft(recA, recB):
    assert recA.bottomleft == Point(1, 2)
    assert recB.bottomleft == Point(2, 2)

def test_topleft(recA, recB):
    assert recA.topleft == Point(recA.left, recA.top)
    assert recA.topleft == Point(1, 4)
    assert recB.topleft == Point(2, 6)

def test_bottomright(recA, recB):
    assert recA.bottomright == Point(3, 2)
    assert recB.bottomright == Point(4, 2)


if __name__ == "__main__":
    pytest.main()