# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
n = int(input())
seqN = int(input())
for i in range(n):
    print((seqN)**i, end=' ')