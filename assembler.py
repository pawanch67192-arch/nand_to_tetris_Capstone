# Hack assembler: turns Prog.asm into Prog.hack
# Roll no. 2501730411, K = 11
# Extra feature (11 mod 3 = 2): warn if the same label is written twice.
#
# Run:  python assembler.py Box.asm

import sys

# comp part -> "a c1 c2 c3 c4 c5 c6"
COMP = {
    "0": "0101010", "1": "0111111", "-1": "0111010",
    "D": "0001100", "A": "0110000", "M": "1110000",
    "!D": "0001101", "!A": "0110001", "!M": "1110001",
    "-D": "0001111", "-A": "0110011", "-M": "1110011",
    "D+1": "0011111", "A+1": "0110111", "M+1": "1110111",
    "D-1": "0001110", "A-1": "0110010", "M-1": "1110010",
    "D+A": "0000010", "D+M": "1000010",
    "D-A": "0010011", "D-M": "1010011",
    "A-D": "0000111", "M-D": "1000111",
    "D&A": "0000000", "D&M": "1000000",
    "D|A": "0010101", "D|M": "1010101",
}

JUMP = {
    "": "000", "JGT": "001", "JEQ": "010", "JGE": "011",
    "JLT": "100", "JNE": "101", "JLE": "110", "JMP": "111",
}


def predefined_symbols():
    symbols = {"SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4,
               "SCREEN": 16384, "KBD": 24576}
    for i in range(16):
        symbols["R" + str(i)] = i
    return symbols


def first_pass(lines, symbols):
    """Remove comments and blank lines, and record every label."""
    instructions = []
    label_lines = {}   # label -> line number where it was first written

    for number, line in enumerate(lines, start=1):
        line = line.split("//")[0]          # cut off the comment
        line = "".join(line.split())        # cut out all spaces and tabs
        if line == "":
            continue

        if line.startswith("(") and line.endswith(")"):
            label = line[1:-1]
            if label in label_lines:
                # Extra feature: duplicate label warning
                print(f"Warning: line {number}: label ({label}) was already "
                      f"written on line {label_lines[label]}. "
                      f"The first one is used.")
            else:
                label_lines[label] = number
                # A label points to the next real instruction
                symbols[label] = len(instructions)
        else:
            instructions.append(line)

    return instructions


def second_pass(instructions, symbols):
    """Turn every instruction into 16 bits."""
    output = []
    next_variable = 16

    for line in instructions:
        if line.startswith("@"):                    # A-instruction
            value = line[1:]
            if value.isdigit():
                address = int(value)
            else:
                if value not in symbols:            # new variable
                    symbols[value] = next_variable
                    next_variable += 1
                address = symbols[value]
            output.append(format(address, "016b"))
        else:                                       # C-instruction
            dest, jump = "", ""
            if "=" in line:
                dest, line = line.split("=")
            if ";" in line:
                line, jump = line.split(";")
            comp = line

            d_bits = ""
            for register in "ADM":
                d_bits += "1" if register in dest else "0"

            output.append("111" + COMP[comp] + d_bits + JUMP[jump])

    return output


def main():
    if len(sys.argv) != 2 or not sys.argv[1].endswith(".asm"):
        print("Usage: python assembler.py Program.asm")
        return

    asm_name = sys.argv[1]
    hack_name = asm_name[:-4] + ".hack"

    with open(asm_name) as file:
        lines = file.readlines()

    symbols = predefined_symbols()
    instructions = first_pass(lines, symbols)
    binary = second_pass(instructions, symbols)

    with open(hack_name, "w") as file:
        for code in binary:
            file.write(code + "\n")

    print(f"Done: {hack_name} ({len(binary)} instructions)")


if __name__ == "__main__":
    main()
