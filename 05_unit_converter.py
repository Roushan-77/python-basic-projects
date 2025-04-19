def length():
    print("\nLength/Distance Converter:")
    print("Common Units:")
    print("1. Millimeter (mm)")
    print("2. Centimeter (cm)")
    print("3. Meter (m)")
    print("4. Kilometer (km)")
    print("5. Inch (in)")
    print("6. Foot (ft)")
    print("7. Yard (yd)")
    print("8. Mile (mi)")

    # Conversion rates from meter (base unit)
    units_in_meters = {
        1: 0.001,    # mm to meters
        2: 0.01,     # cm to meters
        3: 1,        # m to meters
        4: 1000,     # km to meters
        5: 0.0254,   # in to meters
        6: 0.3048,   # ft to meters
        7: 0.9144,   # yd to meters
        8: 1609.34   # mi to meters
    }

    unit_names = {
        1: "Millimeter (mm)",
        2: "Centimeter (cm)",
        3: "Meter (m)",
        4: "Kilometer (km)",
        5: "Inch (in)",
        6: "Foot (ft)",
        7: "Yard (yd)",
        8: "Mile (mi)"
    }

    while True:
        try:
            from_unit = int(input("\nEnter the number corresponding to the unit you want to convert from: "))
            to_unit = int(input("Enter the number corresponding to the unit you want to convert to: "))
            value = float(input("Enter the value to convert: "))

            if from_unit in units_in_meters and to_unit in units_in_meters:
                value_in_meters = value * units_in_meters[from_unit]
                result = value_in_meters / units_in_meters[to_unit]

                print(f"\n{value} {unit_names[from_unit]} is equal to {result:.4f} {unit_names[to_unit]}")
                break
            else:
                print("Invalid unit selected. Please choose from the listed options.\n")
        except ValueError:
            print("Invalid input. Please enter valid numbers.\n")




def mass():
    print("\nMass/Weight Converter:")
    print("Common Units:")
    print("1. Milligram (mg)")
    print("2. Gram (g)")
    print("3. Kilogram (kg)")
    print("4. Metric Tonne (t)")
    print("5. Ounce (oz)")
    print("6. Pound (lb)")
    print("7. Stone (st)")

    # Conversion rates from kilogram (base unit)
    units_in_kg = {
        1: 0.000001,     # mg to kg
        2: 0.001,        # g to kg
        3: 1,            # kg to kg
        4: 1000,         # tonne to kg
        5: 0.0283495,    # oz to kg
        6: 0.453592,     # lb to kg
        7: 6.35029       # stone to kg
    }

    unit_names = {
        1: "Milligram (mg)",
        2: "Gram (g)",
        3: "Kilogram (kg)",
        4: "Metric Tonne (t)",
        5: "Ounce (oz)",
        6: "Pound (lb)",
        7: "Stone (st)"
    }

    while True:
        try:
            from_unit = int(input("\nEnter the number corresponding to the unit you want to convert from: "))
            to_unit = int(input("Enter the number corresponding to the unit you want to convert to: "))
            value = float(input("Enter the value to convert: "))

            if from_unit in units_in_kg and to_unit in units_in_kg:
                value_in_kg = value * units_in_kg[from_unit]
                result = value_in_kg / units_in_kg[to_unit]

                print(f"\n{value} {unit_names[from_unit]} is equal to {result:.4f} {unit_names[to_unit]}")
                break  
            else:
                print("Invalid unit selection. Please choose from the listed options.\n")
        except ValueError:
            print("Invalid input. Please enter valid numbers.\n")


def time():
    print("\nTime Converter:")
    print("Common Units:")
    print("1. Seconds")
    print("2. Minutes")
    print("3. Hours")
    print("4. Days")
    print("5. Weeks")
    print("6. Months (30 days avg)")
    print("7. Years (365 days avg)")

    # Conversion rates to seconds (base unit)
    units_in_seconds = {
        1: 1,            # Second
        2: 60,           # Minute = 60 seconds
        3: 3600,         # Hour = 3600 seconds
        4: 86400,        # Day = 86400 seconds
        5: 604800,       # Week = 7 * 86400 seconds
        6: 2592000,      # Month (30 days avg)
        7: 31536000      # Year (365 days avg)
    }

    unit_names = {
        1: "Seconds",
        2: "Minutes",
        3: "Hours",
        4: "Days",
        5: "Weeks",
        6: "Months",
        7: "Years"
    }

    while True:
        try:
            from_unit = int(input("\nEnter the number corresponding to the unit you want to convert from: "))
            to_unit = int(input("Enter the number corresponding to the unit you want to convert to: "))
            value = float(input("Enter the value to convert: "))

            if from_unit in units_in_seconds and to_unit in units_in_seconds:
                value_in_seconds = value * units_in_seconds[from_unit]
                result = value_in_seconds / units_in_seconds[to_unit]

                print(f"\n{value} {unit_names[from_unit]} is equal to {result:.4f} {unit_names[to_unit]}")
                break  
            else:
                print("Invalid unit selection. Please choose from the listed options.\n")
        except ValueError:
            print("Invalid input. Please enter valid numbers.\n")


def temperature():
    print("\nTemperature Converter:")
    print("Common Units:")
    print("1. Celsius (°C)")
    print("2. Fahrenheit (°F)")
    print("3. Kelvin (K)")

    unit_names = {
        1: "Celsius (°C)",
        2: "Fahrenheit (°F)",
        3: "Kelvin (K)"
    }

    while True:
        try:
            from_unit = int(input("\nEnter the number corresponding to the unit you want to convert from: "))
            to_unit = int(input("Enter the number corresponding to the unit you want to convert to: "))
            value = float(input("Enter the temperature value to convert: "))

            if from_unit == to_unit:
                result = value
            elif from_unit == 1 and to_unit == 2:  # Celsius to Fahrenheit
                result = (value * 9/5) + 32
            elif from_unit == 1 and to_unit == 3:  # Celsius to Kelvin
                result = value + 273.15
            elif from_unit == 2 and to_unit == 1:  # Fahrenheit to Celsius
                result = (value - 32) * 5/9
            elif from_unit == 2 and to_unit == 3:  # Fahrenheit to Kelvin
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == 3 and to_unit == 1:  # Kelvin to Celsius
                result = value - 273.15
            elif from_unit == 3 and to_unit == 2:  # Kelvin to Fahrenheit
                result = (value - 273.15) * 9/5 + 32
            else:
                print("Invalid unit selection. Please try again.\n")
                continue

            print(f"\n{value} {unit_names[from_unit]} is equal to {result:.2f} {unit_names[to_unit]}")
            break 

        except ValueError:
            print("Invalid input. Please enter valid numbers.\n")


def speed():
    print("\nSpeed Converter:")
    print("Units:")
    print("1. Meters per second (m/s)")
    print("2. Kilometers per hour (km/h)")
    print("3. Miles per hour (mph)")
    print("4. Knots")

    unit_names = {
        1: "Meters per second (m/s)",
        2: "Kilometers per hour (km/h)",
        3: "Miles per hour (mph)",
        4: "Knots"
    }

    # Conversion factors to meters per second (base unit)
    units_in_mps = {
        1: 1,                   # m/s
        2: 1000 / 3600,         # km/h
        3: 1609.34 / 3600,      # mph
        4: 1852 / 3600          # knots
    }

    while True:
        try:
            from_unit = int(input("\nEnter the number corresponding to the unit you want to convert from (1-4): "))
            to_unit = int(input("Enter the number corresponding to the unit you want to convert to (1-4): "))
            value = float(input("Enter the speed value to convert: "))

            if from_unit in units_in_mps and to_unit in units_in_mps:
                value_in_mps = value * units_in_mps[from_unit]
                result = value_in_mps / units_in_mps[to_unit]
                print(f"\n{value} {unit_names[from_unit]} is equal to {result:.4f} {unit_names[to_unit]}")
                break
            else:
                print("Invalid unit selection. Please choose between 1 and 4.\n")

        except ValueError:
            print("Invalid input. Please enter numeric values only.\n")


def volume():
    print("\nVolume Converter:")
    print("Units:")
    print("1. Milliliters (ml)")
    print("2. Liters (L)")
    print("3. Cubic centimeters (cc)")
    print("4. Cubic meters (m³)")
    print("5. Teaspoon (tsp)")
    print("6. Tablespoon (tbsp)")
    print("7. Fluid ounces (fl oz)")
    print("8. Cups")
    print("9. Pints")
    print("10. Gallons")

    unit_names = {
        1: "Milliliters (ml)",
        2: "Liters (L)",
        3: "Cubic centimeters (cc)",
        4: "Cubic meters (m³)",
        5: "Teaspoon (tsp)",
        6: "Tablespoon (tbsp)",
        7: "Fluid ounces (fl oz)",
        8: "Cups",
        9: "Pints",
        10: "Gallons"
    }

    # All conversions to Liters (base unit)
    units_in_liters = {
        1: 0.001,        # ml
        2: 1,            # L
        3: 0.001,        # cc
        4: 1000,         # m³
        5: 0.00492892,   # tsp
        6: 0.0147868,    # tbsp
        7: 0.0295735,    # fl oz
        8: 0.24,         # cups (standard metric cup)
        9: 0.473176,     # pint
        10: 3.78541      # gallon
    }

    while True:
        try:
            from_unit = int(input("\nEnter the number corresponding to the unit you want to convert from (1-10): "))
            to_unit = int(input("Enter the number corresponding to the unit you want to convert to (1-10): "))
            value = float(input("Enter the volume value to convert: "))

            if from_unit in units_in_liters and to_unit in units_in_liters:
                value_in_liters = value * units_in_liters[from_unit]
                result = value_in_liters / units_in_liters[to_unit]
                print(f"\n{value} {unit_names[from_unit]} is equal to {result:.4f} {unit_names[to_unit]}")
                break
            else:
                print("Invalid unit selection. Please choose between 1 and 10.\n")

        except ValueError:
            print("Invalid input. Please enter numeric values only.\n")


def area():
    print("\nArea Converter:")
    print("Units:")
    print("1. Square meter (m²)")
    print("2. Square kilometer (km²)")
    print("3. Square foot (ft²)")
    print("4. Square yard (yd²)")
    print("5. Acre")
    print("6. Hectare")

    unit_names = {
        1: "Square meter (m²)",
        2: "Square kilometer (km²)",
        3: "Square foot (ft²)",
        4: "Square yard (yd²)",
        5: "Acre",
        6: "Hectare"
    }

    # All conversions to Square Meters (base unit)
    units_in_square_meters = {
        1: 1,               # m²
        2: 1e6,             # km²
        3: 0.092903,        # ft²
        4: 0.836127,        # yd²
        5: 4046.86,         # acre
        6: 10000            # hectare
    }

    while True:
        try:
            from_unit = int(input("\nEnter the number corresponding to the unit you want to convert from (1-6): "))
            to_unit = int(input("Enter the number corresponding to the unit you want to convert to (1-6): "))
            value = float(input("Enter the area value to convert: "))

            if from_unit in units_in_square_meters and to_unit in units_in_square_meters:
                value_in_square_meters = value * units_in_square_meters[from_unit]
                result = value_in_square_meters / units_in_square_meters[to_unit]
                print(f"\n{value} {unit_names[from_unit]} is equal to {result:.4f} {unit_names[to_unit]}")
                break
            else:
                print("Invalid unit selection. Please choose between 1 and 6.\n")

        except ValueError:
            print("Invalid input. Please enter numeric values only.\n")


def data_storage():
    print("\nData Storage Converter:")
    print("Units:")
    print("1. Bit (bit)")
    print("2. Byte (B)")
    print("3. Kilobyte (KB)")
    print("4. Megabyte (MB)")
    print("5. Gigabyte (GB)")
    print("6. Terabyte (TB)")

    unit_names = {
        1: "Bit (bit)",
        2: "Byte (B)",
        3: "Kilobyte (KB)",
        4: "Megabyte (MB)",
        5: "Gigabyte (GB)",
        6: "Terabyte (TB)"
    }

    # Conversion rates to Byte (base unit)
    units_in_bytes = {
        1: 1 / 8,        # bit to byte
        2: 1,            # byte to byte
        3: 1024,         # KB to bytes
        4: 1024 * 1024,  # MB to bytes
        5: 1024 * 1024 * 1024,  # GB to bytes
        6: 1024 * 1024 * 1024 * 1024  # TB to bytes
    }

    while True:
        try:
            from_unit = int(input("\nEnter the number corresponding to the unit you want to convert from (1-6): "))
            to_unit = int(input("Enter the number corresponding to the unit you want to convert to (1-6): "))
            value = float(input("Enter the value to convert: "))

            if from_unit in units_in_bytes and to_unit in units_in_bytes:
                value_in_bytes = value * units_in_bytes[from_unit]
                result = value_in_bytes / units_in_bytes[to_unit]
                print(f"\n{value} {unit_names[from_unit]} is equal to {result:.4f} {unit_names[to_unit]}")
                break
            else:
                print("Invalid unit selection. Please choose between 1 and 6.\n")

        except ValueError:
            print("Invalid input. Please enter numeric values only.\n")


def energy():
    print("\nEnergy Converter:")
    print("Units:")
    print("1. Joules (J)")
    print("2. Kilojoules (kJ)")
    print("3. Calories (cal)")
    print("4. Kilocalories (kcal)")
    print("5. Watt-hour (Wh)")
    print("6. Kilowatt-hour (kWh)")

    unit_names = {
        1: "Joules (J)",
        2: "Kilojoules (kJ)",
        3: "Calories (cal)",
        4: "Kilocalories (kcal)",
        5: "Watt-hour (Wh)",
        6: "Kilowatt-hour (kWh)"
    }

    # Conversion rates to Joules (base unit)
    units_in_joules = {
        1: 1,                        # Joules to Joules
        2: 1000,                     # Kilojoules to Joules
        3: 4.184,                    # Calories to Joules
        4: 4184,                     # Kilocalories to Joules
        5: 3600,                     # Watt-hour to Joules (1 Wh = 3600 J)
        6: 3600000                  # Kilowatt-hour to Joules (1 kWh = 3600000 J)
    }

    while True:
        try:
            from_unit = int(input("\nEnter the number corresponding to the unit you want to convert from (1-6): "))
            to_unit = int(input("Enter the number corresponding to the unit you want to convert to (1-6): "))
            value = float(input("Enter the value to convert: "))

            if from_unit in units_in_joules and to_unit in units_in_joules:
                value_in_joules = value * units_in_joules[from_unit]
                result = value_in_joules / units_in_joules[to_unit]
                print(f"\n{value} {unit_names[from_unit]} is equal to {result:.4f} {unit_names[to_unit]}")
                break
            else:
                print("Invalid unit selection. Please choose between 1 and 6.\n")

        except ValueError:
            print("Invalid input. Please enter numeric values only.\n")


def pressure():
    print("\nPressure Converter:")
    print("Units:")
    print("1. Pascal (Pa)")
    print("2. Bar")
    print("3. Atmosphere (atm)")
    print("4. mmHg")
    print("5. psi")

    unit_names = {
        1: "Pascal (Pa)",
        2: "Bar",
        3: "Atmosphere (atm)",
        4: "mmHg",
        5: "psi"
    }

    # Conversion rates to Pascals (base unit)
    units_in_pascals = {
        1: 1,              # Pascal to Pascal
        2: 100000,         # Bar to Pascal
        3: 101325,         # Atmosphere to Pascal
        4: 133.322,        # mmHg to Pascal
        5: 6894.76         # psi to Pascal
    }

    while True:
        try:
            from_unit = int(input("\nEnter the number corresponding to the unit you want to convert from (1-5): "))
            to_unit = int(input("Enter the number corresponding to the unit you want to convert to (1-5): "))
            value = float(input("Enter the value to convert: "))

            if from_unit in units_in_pascals and to_unit in units_in_pascals:
                value_in_pascals = value * units_in_pascals[from_unit]
                result = value_in_pascals / units_in_pascals[to_unit]
                print(f"\n{value} {unit_names[from_unit]} is equal to {result:.4f} {unit_names[to_unit]}")
                break
            else:
                print("Invalid unit selection. Please choose between 1 and 5.\n")

        except ValueError:
            print("Invalid input. Please enter numeric values only.\n")


options = {
    1: length,
    2: mass,
    3: time,
    4: temperature,
    5: speed,
    6: volume,
    7: area,
    8: data_storage,
    9: energy,
    10: pressure
}


def main():
    print("\nWelcome to the Unit Converter\n")
    
    while True:
        print("Choose what you want to convert:")
        print("1. Length/Distance")
        print("2. Mass/Weight")
        print("3. Time")
        print("4. Temperature")
        print("5. Speed")
        print("6. Volume")
        print("7. Area")
        print("8. Data Storage")
        print("9. Energy")
        print("10. Pressure")

        try:
            i = int(input("Enter your choice (1 to 10): "))
            if i in options:
                print()  
                options[i]()  
            else:
                print("Please choose a valid option from 1 to 10.\n")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.\n")
            continue

        
        again = input("\nDo you want to convert another unit? (yes/no): ").strip().lower()
        if again not in ['yes', 'y']:
            print("\nThanks for using the Unit Converter. Goodbye!")
            break



if __name__ == "__main__":
    main()