def hex_to_decimal(color):
    hex = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4,
           "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
           "A": 10, "B": 11, "C": 12, "D": 13, "E": 14,
           "F": 15}

    decimal_value = hex.get(color[0]) * 16 + hex.get(color[1]) * 1
    return decimal_value


def decimal_to_hex(color):
    decimal = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4",
               5: "5", 6: "6", 7: "7", 8: "8", 9: "9",
               10: "A", 11: "B", 12: "C", 13: "D", 14: "E",
               15: "F"}
    quotient = color // 16
    remainder = color % 16
    hex_quotient = decimal.get(quotient)
    hex_remainder = decimal.get(remainder)

    return hex_quotient + hex_remainder
