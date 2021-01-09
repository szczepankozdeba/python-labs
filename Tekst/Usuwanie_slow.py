#!/usr/bin/env python3

with open("in_file.txt", "r") as input_file:
    text = input_file.read()
    input_file.close()

text = text.replace(" sie "," ").replace(" i "," ").replace(" oraz "," ").replace(" nigdy "," ").replace(" dlaczego "," ")

with open("out_file.txt", "w") as output_file:
    output_file.write(text)
    output_file.close()