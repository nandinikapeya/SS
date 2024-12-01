n = int(input("Enter a number:"))
g = int(input("Enter another number:"))

x = int(input("Enter a number that A owns:"))
y = int(input("Enter a number that B owns:"))

A = (g**x) %n
B = (g**y) %n

K1 = (B**x) %n
K2 = (A**y) %n

print(K1)
print(K2)