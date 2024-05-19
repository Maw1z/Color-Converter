from color_converter import rgb_to_hex, rgb_to_cmyk, hex_to_rgb, hex_to_cymk, cymk_to_rgb, cymk_to_hex
from get import get_rgb, get_hex, get_cymk

while True:
    try:
        print("""
            1. RGB to Hex
            2. RGB to CYMK
            3. Hex to RGB
            4. Hex to CYMK
            5. CYMK to RGB
            6. CYMK to Hex
            7. Quit
        """)
        
        user_input = input("Enter choice: ")
        user_input_int = int(user_input)
        if user_input_int == 1:
            r_rgb = get_rgb("R")
            g_rgb = get_rgb("G")
            b_rgb = get_rgb("B")
            
            hex_value = rgb_to_hex(r_rgb, g_rgb, b_rgb)
            print(f"The hexadecimal value for this color is: #{hex_value}")
            
        elif user_input_int == 2:
            r_rgb = get_rgb("R")
            g_rgb = get_rgb("G")
            b_rgb = get_rgb("B")
            
            cymk_value = rgb_to_cmyk(r_rgb, g_rgb, b_rgb)
            print(f"The CYMK value for this color is: {cymk_value[0]}%, {cymk_value[1]}%, {cymk_value[2]}%, {cymk_value[3]}%")
            
        elif user_input_int == 3:
            hex_code = get_hex()
            
            rgb_value = hex_to_rgb(hex_code)
            print(f"The RGB value for this color is: {rgb_value[0]}, {rgb_value[1]}, {rgb_value[2]}")
            
        elif user_input_int == 4:
            hex_code = get_hex()
            
            cymk_value = hex_to_cymk(hex_code)
            print(f"The CYMK value for this color is: {cymk_value[0]}%, {cymk_value[1]}%, {cymk_value[2]}%, {cymk_value[3]}%")
    
        elif user_input_int == 5:
            c_percentage = get_cymk("C")
            m_percentage = get_cymk("M")
            y_percentage = get_cymk("Y")
            k_percentage = get_cymk("K")
            
            rgb_value = cymk_to_rgb(c_percentage, m_percentage, y_percentage, k_percentage)
            print(f"The RGB value for this color is: {rgb_value[0]}, {rgb_value[1]}, {rgb_value[2]}")
                
        elif user_input_int == 6:
            c_percentage = get_cymk("C")
            m_percentage = get_cymk("M")
            y_percentage = get_cymk("Y")
            k_percentage = get_cymk("K")
            
            hex_code = cymk_to_hex(c_percentage, m_percentage, y_percentage, k_percentage)
            print(f"The hexadecimal value for this color is: #{hex_code}")        
            
        elif user_input_int == 7:
            quit("Thank you")
            
        else:
            print("Invalid choice, please enter your choice again")
            
    except ValueError:
        print("Invalid input. Please enter an integer value.")
        