from number_converter import hex_to_decimal, decimal_to_hex


def rgb_to_hex(*colorvalues: int):
    r_rgb, g_rgb, b_rgb = (colorvalues[0], colorvalues[1], colorvalues[2])

    hexcode = ""
    r = decimal_to_hex(r_rgb)
    hexcode += str(r)
    g = decimal_to_hex(g_rgb)
    hexcode += str(g)
    b = decimal_to_hex(b_rgb)
    hexcode += str(b)

    return hexcode


def rgb_to_cmyk(*colorvalues: int):
    r, g, b = (colorvalues[0], colorvalues[1], colorvalues[2])

    if r == 0 and g == 0 and b == 0:
        c_percentage, y_percentage, m_percentage, k_percentage = (0, 0, 0, 100)
        
        return c_percentage, y_percentage, m_percentage, k_percentage 

    r_bin = r / 255
    g_bin = g / 255
    b_bin = b / 255

    k = 1 - max(r_bin, g_bin, b_bin)
    if k == 1:
        cymk_code = "0%, 0%, 0%, 100%"

    c = (1 - r_bin - k) / (1 - k)
    y = (1 - g_bin - k) / (1 - k)
    m = (1 - b_bin - k) / (1 - k)

    c_percentage = int(round(c * 100))
    y_percentage = int(round(y * 100))
    m_percentage = int(round(m * 100))
    k_percentage = int(round(k * 100))

    return c_percentage, y_percentage, m_percentage, k_percentage 

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def hex_to_rgb(colorvalue: str):
    r_rgb, g_rgb, b_rgb = (colorvalue[1:3], colorvalue[3:5], colorvalue[5:7])

    r = hex_to_decimal(r_rgb)
    g = hex_to_decimal(g_rgb)
    b = hex_to_decimal(b_rgb)
    
    return r, g, b


def hex_to_cymk(colorvalue: str):
    r, g, b = hex_to_rgb(colorvalue)
    c, y, m, k = rgb_to_cmyk(r, g, b)

    return c, y, m, k

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def cymk_to_rgb(*colorvalues: int):
    c_percentage, y_percentage, m_percentage, k_percentage = (colorvalues[0], colorvalues[1], colorvalues[2], colorvalues[3])

    if k_percentage == 100:
        r, g, b = (0, 0, 0)
        return r, g, b

    c = c_percentage / 100
    y = y_percentage / 100
    m = m_percentage / 100
    k = k_percentage / 100

    r_norm = 255 * (1 - c) * (1 - k)
    g_norm = 255 * (1 - y) * (1 - k)
    b_norm = 255 * (1 - m) * (1 - k)
    
    r = int(round(r_norm))
    g = int(round(g_norm))
    b = int(round(b_norm))
    
    return r+1, g+1, b+1


def cymk_to_hex(*colorvalues):
    r, g, b = cymk_to_rgb(*colorvalues)
    hex_code = rgb_to_hex(r, g, b)
    
    return hex_code
