#!/usr/bin/env python3

with open("in_file.txt", "r") as input_file:
    text = input_file.read()
    input_file.close()

text = text.replace(" i "," oraz ").replace(" oraz "," i ").replace(" nigdy "," prawie ").replace(" dlaczego "," czemu ")

with open("out_file.txt", "w") as output_file:
    output_file.write(text)
    output_file.close()