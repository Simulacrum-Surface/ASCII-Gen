#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

# Getting some facts about the txt output
file = open("test.txt", "r")
counter = 0
liste = []
for line in file:
    x = len(line)
    liste.append(x)
    counter += 1
print(liste)
print("lines: " + str(counter))