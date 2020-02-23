;this is the test

.section.data
x: 0x0000,0x1234
y: .word 0x001c

.section.text
    addi x0,x2,0x01f0
    lui x1,0x11ef0
    addi x0,x1,y
    addi x0,x0,0x0000 ;nop
sum:
    add x3,x1,x2
    bge x3,x2,sum