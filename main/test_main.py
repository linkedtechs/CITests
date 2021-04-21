import main
from main import Square, double


def test_mocking_classes(mocker):
    sq = mocker.MagicMock()
    sq.calculate_area.return_value = 1
    assert sq.calculate_area() ==  1

def test_mocking_double(mocker):
    mocker.patch.object(main, 'CONSTANT', 2)
    expected = 4  
    actual = double()  # now it returns 4, not 2

    assert expected == actual