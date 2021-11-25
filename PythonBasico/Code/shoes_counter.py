#! /usr/bin/env python3
from collections import Counter

x = int(input())#number of shoes
shoes_size = input().split(' ')#shoes size
N = int(input()) #number of customers

customers = []
for i in range(0,N):
    customers.append(input().split(' '))

print(customers)
