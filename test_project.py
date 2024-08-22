import pytest
from project import (
    rectangle_area, circle_area, triangle_area, square_area, parallelogram_area,
    rectangle_perimeter, circle_perimeter, triangle_perimeter, square_perimeter,
    pentagon_perimeter, hexagon_perimeter, cylinder_volume, sphere_volume,
    cuboid_volume, cube_volume, cone_volume, pyramid_volume,
    convert_length, convert_area, convert_volume, convert_weight,
    convert_temperature, convert_speed, convert_time, convert_digital_storage
)


def test_rectangle_area():
    assert rectangle_area(5, 10) == 50
    assert rectangle_area(7, 3) == 21


def test_circle_area():
    assert circle_area(7) == pytest.approx(153.938, 0.001)


def test_triangle_area():
    assert triangle_area(10, 5) == 25


def test_square_area():
    assert square_area(4) == 16


def test_parallelogram_area():
    assert parallelogram_area(6, 3) == 18


def test_rectangle_perimeter():
    assert rectangle_perimeter(5, 10) == 30


def test_circle_perimeter():
    assert circle_perimeter(7) == pytest.approx(43.982, 0.001)


def test_triangle_perimeter():
    assert triangle_perimeter(3, 4, 5) == 12


def test_square_perimeter():
    assert square_perimeter(4) == 16


def test_pentagon_perimeter():
    assert pentagon_perimeter(6) == 30


def test_hexagon_perimeter():
    assert hexagon_perimeter(7) == 42


def test_cylinder_volume():
    assert cylinder_volume(3, 7) == pytest.approx(197.920, 0.001)


def test_sphere_volume():
    assert sphere_volume(5) == pytest.approx(523.598, 0.001)


def test_cuboid_volume():
    assert cuboid_volume(4, 5, 6) == 120


def test_cube_volume():
    assert cube_volume(3) == 27


def test_cone_volume():
    assert cone_volume(3, 9) == pytest.approx(84.823, 0.001)


def test_pyramid_volume():
    assert pyramid_volume(20, 9) == pytest.approx(60, 0.001)


def test_convert_length():
    assert convert_length(1000, 'meters', 'kilometers') == 1
    assert convert_length(1, 'miles', 'meters') == 1609.34


def test_convert_area():
    assert convert_area(1, 'square_miles', 'square_kilometers') == pytest.approx(2.58999, 0.001)


def test_convert_volume():
    assert convert_volume(1, 'liters', 'gallons') == pytest.approx(0.264172, 0.001)


def test_convert_weight():
    assert convert_weight(1, 'kilograms', 'grams') == 1000
    assert convert_weight(1, 'pounds', 'grams') == pytest.approx(453.592, 0.001)


def test_convert_temperature():
    assert convert_temperature(0, 'celsius', 'fahrenheit') == 32
    assert convert_temperature(32, 'fahrenheit', 'celsius') == 0


def test_convert_speed():
    assert convert_speed(10, 'kilometers_per_hour', 'meters_per_second') == pytest.approx(2.77778, 0.001)


def test_convert_time():
    assert convert_time(1, 'hours', 'minutes') == 60


def test_convert_digital_storage():
    assert convert_digital_storage(1, 'gigabytes', 'megabytes') == 1024
