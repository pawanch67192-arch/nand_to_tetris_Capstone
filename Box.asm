// Box.asm  -  Roll no. 2501730411, K = 11
// While any key is pressed, show a black box. Release the key: box disappears.
//   starts at row 11
//   20 rows tall
//   64 pixels wide (4 words), from the left edge
// Start address = SCREEN + 32*11 = SCREEN + 352

(LOOP)
    @KBD
    D=M             // D = key code (0 = no key)
    @BLACK
    D;JNE           // a key is pressed -> black

    @color
    M=0             // no key -> white
    @DRAW
    0;JMP

(BLACK)
    @color
    M=-1            // all 16 bits are 1 -> black

(DRAW)
    @SCREEN
    D=A
    @352            // 32 * 11
    D=D+A
    @addr
    M=D             // addr = first word of the box

    @20
    D=A
    @rows
    M=D             // 20 rows left to draw

(ROW)
    @color
    D=M
    @addr
    A=M
    M=D             // word 1
    A=A+1
    M=D             // word 2
    A=A+1
    M=D             // word 3
    A=A+1
    M=D             // word 4

    @32
    D=A
    @addr
    M=D+M           // go down one row

    @rows
    MD=M-1          // rows = rows - 1
    @ROW
    D;JGT           // more rows left -> draw the next one

    @LOOP
    0;JMP           // check the keyboard again
