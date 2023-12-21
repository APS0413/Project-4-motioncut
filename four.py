def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def meter_to_feet(meter):
    return meter * 3.28084

def feet_to_meter(feet):
    return feet / 3.28084

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

def unit_converter():
    print("Welcome to the Unit Converter!")
    
    conversion_type = input("Select conversion type (T for Temperature, L for Length, W for Weight): ").upper()
    
    try:
        if conversion_type == "T":
            value = float(input("Enter the temperature value: "))
            source_unit = input("Enter the source unit (C for Celsius, F for Fahrenheit): ").upper()
            target_unit = input("Enter the target unit (C for Celsius, F for Fahrenheit): ").upper()

            if source_unit == "C" and target_unit == "F":
                result = celsius_to_fahrenheit(value)
                print(f"{value} Celsius is equal to {result} Fahrenheit.")
            elif source_unit == "F" and target_unit == "C":
                result = fahrenheit_to_celsius(value)
                print(f"{value} Fahrenheit is equal to {result} Celsius.")
            elif source_unit == target_unit:
                print("Source and target units are the same. No conversion needed.")
            else:
                print("Invalid source or target unit. Please enter 'C' or 'F'.")
                
        elif conversion_type == "L":
            value = float(input("Enter the length value: "))
            source_unit = input("Enter the source unit (M for Meter, F for Feet): ").upper()
            target_unit = input("Enter the target unit (M for Meter, F for Feet): ").upper()

            if source_unit == "M" and target_unit == "F":
                result = meter_to_feet(value)
                print(f"{value} Meter is equal to {result} Feet.")
            elif source_unit == "F" and target_unit == "M":
                result = feet_to_meter(value)
                print(f"{value} Feet is equal to {result} Meter.")
            elif source_unit == target_unit:
                print("Source and target units are the same. No conversion needed.")
            else:
                print("Invalid source or target unit. Please enter 'M' or 'F'.")
                
        elif conversion_type == "W":
            value = float(input("Enter the weight value: "))
            source_unit = input("Enter the source unit (KG for Kilograms, P for Pounds): ").upper()
            target_unit = input("Enter the target unit (KG for Kilograms, P for Pounds): ").upper()

            if source_unit == "KG" and target_unit == "P":
                result = kg_to_pounds(value)
                print(f"{value} Kilograms is equal to {result} Pounds.")
            elif source_unit == "P" and target_unit == "KG":
                result = pounds_to_kg(value)
                print(f"{value} Pounds is equal to {result} Kilograms.")
            elif source_unit == target_unit:
                print("Source and target units are the same. No conversion needed.")
            else:
                print("Invalid source or target unit. Please enter 'KG' or 'P'.")
                
        else:
            print("Invalid conversion type. Please enter 'T', 'L', or 'W'.")
            
    except ValueError:
        print("Invalid input. Please enter a numeric value for the conversion.")

if __name__ == "__main__":
    unit_converter()
