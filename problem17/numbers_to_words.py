#! /usr/bin/env python


num_to_word = {}
num_to_word[0] = "zero"
num_to_word[1] = "one"
num_to_word[2] = "two"
num_to_word[3] = "three"
num_to_word[4] = "four"
num_to_word[5] = "five"
num_to_word[6] = "six"
num_to_word[7] = "seven"
num_to_word[8] = "eight"
num_to_word[9] = "nine"
num_to_word[10] = "ten"
num_to_word[11] = "eleven"
num_to_word[12] = "twelve"
num_to_word[13] = "thirteen"
num_to_word[14] = "fourteen"
num_to_word[15] = "fifteen"
num_to_word[16] = "sixteen"
num_to_word[17] = "seventeen"
num_to_word[18] = "eighteen"
num_to_word[19] = "nineteen"
num_to_word[20] = "twenty"
num_to_word[30] = "thirty"
num_to_word[40] = "forty"
num_to_word[50] = "fifty"
num_to_word[60] = "sixty"
num_to_word[70] = "seventy"
num_to_word[80] = "eighty"
num_to_word[90] = "nighty"
num_to_word[100] = "hundred"
num_to_word[1000] = "thousand"

num_to_char_count = {}

for key in num_to_word:
    num_to_char_count[key] = len(num_to_word[key])

strlen = 0    
for x in range(0,1001):
    thousands = x//1000    
    x = x - (1000*thousands)    
    hundreds = x//100
    x = x - (100*hundreds)
    tens = x//10
    ones = x-(10*tens)

    out_str = ""

    
    if thousands != 0:
        out_str += " " + num_to_word[thousands] + " " + num_to_word[1000]
    if hundreds != 0:
        out_str += " " + num_to_word[hundreds] + " " + num_to_word[100]
        if tens != 0 or ones != 0:
            out_str += " and"
         
    if tens != 0:
        if tens == 1:
            tens = tens*10 + ones
            ones = 0
            out_str += " " + num_to_word[tens]
        else:
            out_str += " " + num_to_word[tens*10]
    if ones != 0:
        out_str += " " + num_to_word[ones]
    print(out_str.strip())
    
    out_str = out_str.replace(" ","")
    strlen += len(out_str)
        
print(strlen)
