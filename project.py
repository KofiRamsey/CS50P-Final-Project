import math
import statistics

history = []

print(r'''
.------------------------------------------------.
|  _____      _            _       _             |
| / ____|    | |          | |     | |            |
|| |     __ _| | ___ _   _| | __ _| |_ ___  _ __ |
|| |    / _` | |/ __| | | | |/ _` | __/ _ \| '__||
|| |___| (_| | | (__| |_| | | (_| | || (_) | |   |
| \_____\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   |
'------------------------------------------------'
''')


def main():
    while True:
        print("--------------------------------------")
        print("Choose an option:")
        print("1. Arithmetic Operations")
        print("2. Area Calculations")
        print("3. Perimeter Calculations")
        print("4. Volume Calculations")
        print("5. Unit Conversions")
        print("6. Pythagorean Theorem")
        print("7. Statistics Calculations")
        print("8. View History")
        print("9. Exit")
        print("--------------------------------------")

        choice = input("Enter your choice (1-9): ")

        try:
            if choice == '1':
                arithmetic_operations()
            elif choice == '2':
                area_calculations()
            elif choice == '3':
                perimeter_calculations()
            elif choice == '4':
                volume_calculations()
            elif choice == '5':
                unit_conversion()
            elif choice == '6':
                pythagorean_theorem()
            elif choice == '7':
                statistics_calculations()
            elif choice == '8':
                view_history()
            elif choice == '9':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"An error occurred: {e}")


def arithmetic_operations():
    print("Arithmetic Operations:")

    expression = input("Enter the arithmetic expression (e.g., 1 + 2 * 3 / 4): ")

    try:
        result = eval(expression)
        print(f"Result: {result}")
        history.append((expression, result))
    except Exception as e:
        print(f"Error: {e}. Invalid expression.")


def area_calculations():
    print("Area Calculations:")
    shape = input("Enter shape (rectangle, circle, triangle, square, parallelogram): ").lower()

    try:
        if shape == 'rectangle':
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            result = rectangle_area(width, height)
            print(f"Area: {result}")
            history.append((f"Rectangle Area: width={width}, height={height}", result))
        elif shape == 'circle':
            radius = float(input("Enter radius: "))
            result = circle_area(radius)
            print(f"Area: {result}")
            history.append((f"Circle Area: radius={radius}", result))
        elif shape == 'triangle':
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            result = triangle_area(base, height)
            print(f"Area: {result}")
            history.append((f"Triangle Area: base={base}, height={height}", result))
        elif shape == 'square':
            side = float(input("Enter side length: "))
            result = square_area(side)
            print(f"Area: {result}")
            history.append((f"Square Area: side={side}", result))
        elif shape == 'parallelogram':
            base = float(input("Enter base: "))
            height = float(input("Enter height: "))
            result = parallelogram_area(base, height)
            print(f"Area: {result}")
            history.append((f"Parallelogram Area: base={base}, height={height}", result))
        else:
            print("Invalid shape.")
    except ValueError as e:
        print(f"Error: {e}. Invalid input.")


def rectangle_area(width, height):
    return width * height


def circle_area(radius):
    return math.pi * radius ** 2


def triangle_area(base, height):
    return 0.5 * base * height


def square_area(side):
    return side ** 2


def parallelogram_area(base, height):
    return base * height


def perimeter_calculations():
    print("Perimeter Calculations:")
    shape = input("Enter shape (rectangle, circle, triangle, square, pentagon, hexagon): ").lower()

    try:
        if shape == 'rectangle':
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            result = rectangle_perimeter(width, height)
            print(f"Perimeter: {result}")
            history.append((f"Rectangle Perimeter: width={width}, height={height}", result))
        elif shape == 'circle':
            radius = float(input("Enter radius: "))
            result = circle_perimeter(radius)
            print(f"Perimeter: {result}")
            history.append((f"Circle Perimeter: radius={radius}", result))
        elif shape == 'triangle':
            side1 = float(input("Enter first side: "))
            side2 = float(input("Enter second side: "))
            side3 = float(input("Enter third side: "))
            result = triangle_perimeter(side1, side2, side3)
            print(f"Perimeter: {result}")
            history.append((f"Triangle Perimeter: side1={side1}, side2={side2}, side3={side3}", result))
        elif shape == 'square':
            side = float(input("Enter side length: "))
            result = square_perimeter(side)
            print(f"Perimeter: {result}")
            history.append((f"Square Perimeter: side={side}", result))
        elif shape == 'pentagon':
            side = float(input("Enter side length: "))
            result = pentagon_perimeter(side)
            print(f"Perimeter: {result}")
            history.append((f"Pentagon Perimeter: side={side}", result))
        elif shape == 'hexagon':
            side = float(input("Enter side length: "))
            result = hexagon_perimeter(side)
            print(f"Perimeter: {result}")
            history.append((f"Hexagon Perimeter: side={side}", result))
        else:
            print("Invalid shape.")
    except ValueError as e:
        print(f"Error: {e}. Invalid input.")


def rectangle_perimeter(width, height):
    return 2 * (width + height)


def circle_perimeter(radius):
    return 2 * math.pi * radius


def triangle_perimeter(side1, side2, side3):
    return side1 + side2 + side3


def square_perimeter(side):
    return 4 * side


def pentagon_perimeter(side):
    return 5 * side


def hexagon_perimeter(side):
    return 6 * side


def volume_calculations():
    print("Volume Calculations:")
    shape = input("Enter shape (cylinder, sphere, cuboid, cube, cone, pyramid): ").lower()

    try:
        if shape == 'cylinder':
            radius = float(input("Enter radius: "))
            height = float(input("Enter height: "))
            result = cylinder_volume(radius, height)
            print(f"Volume: {result}")
            history.append((f"Cylinder Volume: radius={radius}, height={height}", result))
        elif shape == 'sphere':
            radius = float(input("Enter radius: "))
            result = sphere_volume(radius)
            print(f"Volume: {result}")
            history.append((f"Sphere Volume: radius={radius}", result))
        elif shape == 'cuboid':
            length = float(input("Enter length: "))
            width = float(input("Enter width: "))
            height = float(input("Enter height: "))
            result = cuboid_volume(length, width, height)
            print(f"Volume: {result}")
            history.append((f"Cuboid Volume: length={length}, width={width}, height={height}", result))
        elif shape == 'cube':
            side = float(input("Enter side length: "))
            result = cube_volume(side)
            print(f"Volume: {result}")
            history.append((f"Cube Volume: side={side}", result))
        elif shape == 'cone':
            radius = float(input("Enter radius: "))
            height = float(input("Enter height: "))
            result = cone_volume(radius, height)
            print(f"Volume: {result}")
            history.append((f"Cone Volume: radius={radius}, height={height}", result))
        elif shape == 'pyramid':
            base_area = float(input("Enter base area: "))
            height = float(input("Enter height: "))
            result = pyramid_volume(base_area, height)
            print(f"Volume: {result}")
            history.append((f"Pyramid Volume: base_area={base_area}, height={height}", result))
        else:
            print("Invalid shape.")
    except ValueError as e:
        print(f"Error: {e}. Invalid input.")


def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height


def sphere_volume(radius):
    return 4 / 3 * math.pi * radius ** 3


def cuboid_volume(length, width, height):
    return length * width * height


def cube_volume(side):
    return side ** 3


def cone_volume(radius, height):
    return 1 / 3 * math.pi * radius ** 2 * height


def pyramid_volume(base_area, height):
    return 1 / 3 * base_area * height


def unit_conversion():
    print("Unit Conversions:")
    conversion_type = input("Enter conversion type (length, area, volume, weight, temperature, speed, time, "
                            "digital_storage): ").lower()

    try:
        if conversion_type == 'length':
            length = float(input("Enter length: "))
            from_unit = input("From unit (meters, kilometers, miles, yards): ").lower()
            to_unit = input("To unit (meters, kilometers, miles, yards): ").lower()
            result = convert_length(length, from_unit, to_unit)
            print(f"Converted length: {result} {to_unit}")
            history.append((f"Length Conversion: {length} {from_unit} to {result} {to_unit}", result))
        elif conversion_type == 'area':
            area = float(input("Enter area: "))
            from_unit = input("From unit (square_meters, square_kilometers, square_miles, square_yards): ").lower()
            to_unit = input("To unit (square_meters, square_kilometers, square_miles, square_yards): ").lower()
            result = convert_area(area, from_unit, to_unit)
            print(f"Converted area: {result} {to_unit}")
            history.append((f"Area Conversion: {area} {from_unit} to {result} {to_unit}", result))
        elif conversion_type == 'volume':
            volume = float(input("Enter volume: "))
            from_unit = input("From unit (liters, cubic_meters, gallons, cubic_inches): ").lower()
            to_unit = input("To unit (liters, cubic_meters, gallons, cubic_inches): ").lower()
            result = convert_volume(volume, from_unit, to_unit)
            print(f"Converted volume: {result} {to_unit}")
            history.append((f"Volume Conversion: {volume} {from_unit} to {result} {to_unit}", result))
        elif conversion_type == 'weight':
            weight = float(input("Enter weight: "))
            from_unit = input("From unit (grams, kilograms, pounds, ounces): ").lower()
            to_unit = input("To unit (grams, kilograms, pounds, ounces): ").lower()
            result = convert_weight(weight, from_unit, to_unit)
            print(f"Converted weight: {result} {to_unit}")
            history.append((f"Weight Conversion: {weight} {from_unit} to {result} {to_unit}", result))
        elif conversion_type == 'temperature':
            temperature = float(input("Enter temperature: "))
            from_unit = input("From unit (celsius, fahrenheit, kelvin): ").lower()
            to_unit = input("To unit (celsius, fahrenheit, kelvin): ").lower()
            result = convert_temperature(temperature, from_unit, to_unit)
            print(f"Converted temperature: {result} {to_unit}")
            history.append((f"Temperature Conversion: {temperature} {from_unit} to {result} {to_unit}", result))
        elif conversion_type == 'speed':
            speed = float(input("Enter speed: "))
            from_unit = input("From unit (meters_per_second, kilometers_per_hour, miles_per_hour): ").lower()
            to_unit = input("To unit (meters_per_second, kilometers_per_hour, miles_per_hour): ").lower()
            result = convert_speed(speed, from_unit, to_unit)
            print(f"Converted speed: {result} {to_unit}")
            history.append((f"Speed Conversion: {speed} {from_unit} to {result} {to_unit}", result))
        elif conversion_type == 'time':
            time = float(input("Enter time: "))
            from_unit = input("From unit (seconds, minutes, hours, days): ").lower()
            to_unit = input("To unit (seconds, minutes, hours, days): ").lower()
            result = convert_time(time, from_unit, to_unit)
            print(f"Converted time: {result} {to_unit}")
            history.append((f"Time Conversion: {time} {from_unit} to {result} {to_unit}", result))
        elif conversion_type == 'digital_storage':
            storage = float(input("Enter storage: "))
            from_unit = input("From unit (bytes, kilobytes, megabytes, gigabytes, terabytes): ").lower()
            to_unit = input("To unit (bytes, kilobytes, megabytes, gigabytes, terabytes): ").lower()
            result = convert_digital_storage(storage, from_unit, to_unit)
            print(f"Converted storage: {result} {to_unit}")
            history.append((f"Digital Storage Conversion: {storage} {from_unit} to {result} {to_unit}", result))
        else:
            print("Invalid conversion type.")
    except ValueError as e:
        print(f"Error: {e}. Invalid input.")
    except Exception as e:
        print(f"An error occurred: {e}")


def convert_length(value, from_unit, to_unit):
    units = {'meters': 1, 'kilometers': 1000, 'miles': 1609.34, 'yards': 0.9144}
    if from_unit in units and to_unit in units:
        return value * units[from_unit] / units[to_unit]
    else:
        raise ValueError("Invalid length units")


def convert_area(value, from_unit, to_unit):
    units = {'square_meters': 1, 'square_kilometers': 1e6, 'square_miles': 2.58999e6, 'square_yards': 0.836127}
    if from_unit in units and to_unit in units:
        return value * units[from_unit] / units[to_unit]
    else:
        raise ValueError("Invalid area units")


def convert_volume(value, from_unit, to_unit):
    units = {'liters': 1, 'cubic_meters': 1000, 'gallons': 3.78541, 'cubic_inches': 0.0163871}
    if from_unit in units and to_unit in units:
        return value * units[from_unit] / units[to_unit]
    else:
        raise ValueError("Invalid volume units")


def convert_weight(value, from_unit, to_unit):
    units = {'grams': 1, 'kilograms': 1000, 'pounds': 453.592, 'ounces': 28.3495}
    if from_unit in units and to_unit in units:
        return value * units[from_unit] / units[to_unit]
    else:
        raise ValueError("Invalid weight units")


def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return value * 9 / 5 + 32
        elif to_unit == 'kelvin':
            return value + 273.15
        elif to_unit == 'celsius':
            return value
        else:
            raise ValueError("Invalid temperature unit")
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5 / 9
        elif to_unit == 'kelvin':
            return (value - 32) * 5 / 9 + 273.15
        elif to_unit == 'fahrenheit':
            return value
        else:
            raise ValueError("Invalid temperature unit")
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9 / 5 + 32
        elif to_unit == 'kelvin':
            return value
        else:
            raise ValueError("Invalid temperature unit")
    else:
        raise ValueError("Invalid temperature unit")


def convert_speed(value, from_unit, to_unit):
    units = {'meters_per_second': 1, 'kilometers_per_hour': 0.277778, 'miles_per_hour': 0.44704}
    if from_unit in units and to_unit in units:
        return value * units[from_unit] / units[to_unit]
    else:
        raise ValueError("Invalid speed units")


def convert_time(value, from_unit, to_unit):
    units = {'seconds': 1, 'minutes': 60, 'hours': 3600, 'days': 86400}
    if from_unit in units and to_unit in units:
        return value * units[from_unit] / units[to_unit]
    else:
        raise ValueError("Invalid time units")


def convert_digital_storage(value, from_unit, to_unit):
    units = {'bytes': 1, 'kilobytes': 1024, 'megabytes': 1024 ** 2, 'gigabytes': 1024 ** 3, 'terabytes': 1024 ** 4}
    if from_unit in units and to_unit in units:
        return value * units[from_unit] / units[to_unit]
    else:
        raise ValueError("Invalid digital storage units")


def pythagorean_theorem():
    print("Pythagorean Theorem:")
    print("1. Solve for hypotenuse (c)")
    print("2. Solve for side a")
    print("3. Solve for side b")

    option = input("Choose an option (1-3): ")

    try:
        if option == '1':
            a = float(input("Enter side a: "))
            b = float(input("Enter side b: "))
            result = math.sqrt(a ** 2 + b ** 2)
            print(f"Hypotenuse (c): {result}")
            history.append((f"Pythagorean Theorem: a={a}, b={b}", result))
        elif option == '2':
            c = float(input("Enter hypotenuse (c): "))
            b = float(input("Enter side b: "))
            result = math.sqrt(c ** 2 - b ** 2)
            print(f"Side a: {result}")
            history.append((f"Pythagorean Theorem: c={c}, b={b}", result))
        elif option == '3':
            c = float(input("Enter hypotenuse (c): "))
            a = float(input("Enter side a: "))
            result = math.sqrt(c ** 2 - a ** 2)
            print(f"Side b: {result}")
            history.append((f"Pythagorean Theorem: c={c}, a={a}", result))
        else:
            print("Invalid option.")
    except ValueError as e:
        print(f"Error: {e}. Invalid input.")
    except Exception as e:
        print(f"An error occurred: {e}")


def statistics_calculations():
    print("Statistics Calculations:")

    try:
        data = list(map(float, input("Enter numbers separated by space: ").split()))

        if not data:
            print("No data provided.")
            return

        mean_result = statistics.mean(data)
        print(f"Mean: {mean_result}")

        median_result = statistics.median(data)
        print(f"Median: {median_result}")

        try:
            mode_result = statistics.mode(data)
        except statistics.StatisticsError:
            mode_result = "No unique mode"
        print(f"Mode: {mode_result}")

        history.append((f"Statistics Calculations: data={data}", {
            'Mean': mean_result,
            'Median': median_result,
            'Mode': mode_result
        }))
    except ValueError as e:
        print(f"Error: {e}. Invalid input.")
    except Exception as e:
        print(f"An error occurred: {e}")


def view_history():
    print("Calculation History:")
    if not history:
        print("No history available.")
    for entry in history:
        print(f"Expression: {entry[0]}, Result: {entry[1]}")


if __name__ == "__main__":
    main()
