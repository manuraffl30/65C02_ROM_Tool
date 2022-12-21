from dictionary import *

rom = bytearray([cmd_IMPLIED["NOP"][0]] * 256)

rom[0xFC] = 0x00 #
rom[0xFD] = 0xFF # set program start address to $FF00 (after RESET)


#------------------------------
rom[0] = cmd_IMMEDIATE["LDA"][0]
rom[1] = 0x42 
#LDA #$42
#------------------------------
rom[2] = cmd_ABSOLUTE["ASL"][0]
#Shift Left
#------------------------------
rom[3] = cmd_ABSOLUTE["STA"][0]
rom[4] = 0x00
rom[5] = 0x60 
#STA $6000
#------------------------------


with open("rom.bin", "wb") as out_file:
    out_file.write(rom);