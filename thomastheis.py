# Modul random importieren
import random

# Zufallsgenerator initialisieren

random.seed()

a = random.randint(1,10)
b = random.randint(1,10)
c = a + b

print "task:", a, " + ", b

z = raw_input ("please instert result >> ")

print "your input >> ", z
print "result >> ", c



