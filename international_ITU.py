#!/usr/bin/python

import winsound as wsnd

message = raw_input("Enter your plaintext (lowercase and numbers) -> ")

morse_short = 300
morse_long = 600
morse_freq = 400

ITU_code ={ # 0 = short, 1 = long
        'a' : '01',
        'b' : '1000',
        'c' : '1010',
        'd' : '100',
        'e' : '0',
        'f' : '0010',
        'g' : '110',
        'h' : '0000',
        'i' : '00',
        'j' : '0111',
        'k' : '101',
        'l' : '0100',
        'm' : '11',
        'n' : '10',
        'o' : '111',
        'p' : '0110',
        'q' : '1101',
        'r' : '010',
        's' : '000',
        't' : '1',
        'u' : '001',
        'v' : '0001',
        'w' : '011',
        'x' : '1001',
        'y' : '1011',
        'z' : '1100',
        ' ' : '', # space is nothing
        '1' : '01111',
        '2' : '00111',
        '3' : '00011',
        '4' : '00001',
        '5' : '00000',
        '6' : '10000',
        '7' : '11000',
        '8' : '11100',
        '9' : '11110',
        '0' : '11111'}

def convert_beeps():
    ITU_message = ""
    for char in message:
        ITU_message += ITU_code[char.lower()]
    return ITU_message

def zero_to_beep(itu_msg):
    for char in itu_msg:
        if char == '0':
            wsnd.Beep(morse_freq, morse_short)
        elif char == '1':
            wsnd.Beep(morse_freq, morse_long)
        else:
            print "you broke me"
    return "done"

def main():
    zero_to_beep(convert_beeps())
    

if __name__ == "__main__": main()
