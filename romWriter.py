from dictionary import *

rom = bytearray([] * 256) # 0xea is the opcode for "NOP" (6502)
rom[0] = 0xa9 # 0xa9 is opcode for LDA (load accu with memory)
rom[1] = 0x42 # 0x42 is the value which should be loaded into the accu
rom[2] = 0x8d # 0x8d is the opcode for STA (store accu in memory)
rom[3] = 0x00
rom[4] = 0x60 # accu content should be stored at address $6000
rom[0xfc] = 0x00 #
rom[0xfd] = 0xFF # set program start address to $FF00 (after RESET)
with open("rom3.bin", "wb") as out_file:
out_file.write(rom);