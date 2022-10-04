# how to make a password generator in python :)
from pickletools import read_uint8
import random

x = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'J', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
y = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
int = "1","2","3","4","5","6","7","8","9","0"
symbols = "!","@","#","$","%","&","^","7","-","_","="
# all these files will be given in the github project file as well :)

ran1 = random.choice(x)
ran2 = random.choice(y)
ran3 = random.choice(int)
ran4 = random.choice(symbols)
ran5 = random.choice(int)
ran6 = random.choice(symbols)
ran7 = random.choice(x)
ran8 = random.choice(symbols)

pswrd = ran1+ran2+ran3+ran4+ran5+ran6+ran7+ran8 
# since most platforms support 8 word limit passwords, im gonna use only 8 words :)

print(pswrd)