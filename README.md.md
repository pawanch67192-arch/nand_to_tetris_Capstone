# Capstone Project: Make the Computer Draw a Box

**Course:** Nand to Tetris -- I (ETCCNT301)\
**University:** K.R. Mangalam University\
**Student:** Pawan Chauhan\
**Roll No.:** 2501730411

## Project Overview

This project implements the Hack computer and a Python-based assembler,
then uses them to run a Hack assembly program that draws a black box on
the screen while a key is pressed. The box disappears when the key is
released.

The project is divided into three parts:

1.  **Building the computer:** HDL implementations of the CPU, Memory,
    and Computer chips.
2.  **Assembler:** A two-pass Python assembler that converts `.asm`
    files into 16-bit Hack machine instructions.
3.  **Box program:** A Hack assembly program (`Box.asm`) that draws the
    personalised rectangle.

## Personalised Box Settings

The personal number `K` is the last two digits of the roll number.

  Item                                                 Value
  --------------------------- ------------------------------
  K                                                       11
  Starting row                                            11
  Height                               20 rows (rows 11--30)
  Width                          64 pixels (4 words per row)
  First screen word address                            16736
  Extra assembler feature       Warning for duplicate labels

The box starts at screen address `16384 + (32 × 11) = 16736`.

## Project Files

The main files used in this project are:

-   `CPU.hdl` --- Hack CPU implementation.
-   `Memory.hdl` --- Hack memory implementation.
-   `Computer.hdl` --- Connects the CPU, memory, and ROM.
-   `assembler.py` --- Converts Hack assembly programs into machine
    code.
-   `Box.asm` --- Draws the personalised box on the screen.

The project also uses the Nand2Tetris test scripts and test programs.

## Requirements

-   Python 3
-   Nand2Tetris Software Suite (Hardware Simulator and CPU Emulator)
-   The HDL files and Hack assembly test files included with the project

No external Python packages are required for the assembler if it uses
only Python's standard library.

## Running the Assembler

Open a terminal in the project directory and run:

``` bash
python assembler.py Box.asm
```

To assemble the official test programs, for example:

``` bash
python assembler.py tests/Add.asm
python assembler.py tests/Max.asm
python assembler.py tests/Rect.asm
python assembler.py tests/Pong.asm
```

The assembler generates a corresponding `.hack` file containing 16-bit
binary instructions.

## How the Box Program Works

1.  The program checks the keyboard memory address (`KBD`, address
    `24576`).
2.  If no key is pressed, it uses `0` as the fill value. If a key is
    pressed, it uses `-1` to fill the screen words with black pixels.
3.  It starts drawing at address `16736`, which is row 11 of the screen.
4.  It writes the fill value to 4 consecutive words for each row.
5.  It repeats this for 20 rows, adding 32 to the address to move to the
    next screen row.
6.  It continuously checks the keyboard, so the box appears only while a
    key is held.

## Testing

The project report records successful Hardware Simulator results for the
following tests:

  Test                 Chip                Steps Result
  -------------------- ---------- -------------- --------
  `CPU.tst`            CPU                    52 Passed
  `Memory.tst`         Memory       Not recorded Passed
  `ComputerAdd.tst`    Computer               17 Passed
  `ComputerMax.tst`    Computer               30 Passed
  `ComputerRect.tst`   Computer               69 Passed

The assembler was also run on these programs:

  Program        Instructions generated
  ------------ ------------------------
  `Add.asm`                           6
  `Max.asm`                          16
  `Rect.asm`                         25
  `Pong.asm`                      27483
  `Box.asm`                          41

## Running the Box Program

1.  Run the assembler command to generate `Box.hack`.
2.  Open the Nand2Tetris CPU Emulator.
3.  Load `Box.hack`.
4.  Enable the keyboard and run the program.
5.  Hold a key to display the black box; release the key to clear it.

## Learning Outcome

This project helped me understand how the CPU, memory, machine
instructions, and assembler work together. It also gave me practical
experience with HDL chip connections, symbol handling in an assembler,
and writing a Hack assembly program that interacts with the screen and
keyboard.

------------------------------------------------------------------------

**Author:** Pawan Chauhan\
**Roll No.:** 2501730411
