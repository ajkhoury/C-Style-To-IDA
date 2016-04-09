import re

def get_input(prompt):
    print prompt,
    lines = []
    line = raw_input()
    while line != "":
        line = line.replace(" ", "").replace("\t", "")
        lines.append(line)
        line = raw_input()
    lines = ''.join(lines)
    return lines

def main():
    byte_array_str = get_input("Enter C-Style byte array:")
    if (byte_array_str):
        byte_array_str = byte_array_str[2:]
        byte_array_str = re.sub(',0x', ' ', byte_array_str)
        byte_array_str = byte_array_str.upper()
        wildcard = get_input("Enter wildcard (eg. 00 or CC):").upper()
        byte_array_str = re.sub(wildcard, '?', byte_array_str)       
        print("Converted byte array: " + byte_array_str)
    else:
        print("Error: invalid input")
    
if __name__ == "__main__":
    main()
