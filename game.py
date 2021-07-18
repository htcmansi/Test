# Created by Mansi Raut
 
import random
choose=[7,chr(178),chr(1),'~',chr(219),chr(177),0]
n1=random.choice(choose)
n2=random.choice(choose)
n3=random.choice(choose)
list=[n1,n2,n3]
score=0
print('  _______________ ')
print(' |  ___________  |')
print(' | |___________| |  0')
print(' |  ___________  |  |')
print(' | |   |   |   | |  |')
print(' | |',n1,'|',n2,'|',n3,'| |_ |')
print(' | |___|___|___| |_',chr(41))
print(' |_______________|')
print('/    Manu
  ',chr(92))
print('|_________________|')
print(' |______________|')
print('')
count=list.count(7)
score+=500*count
count=list.count(chr(178))
score+=250*count
count=list.count(chr(1))
score+=10*count
count=list.count('~')
score+=5*count
count=list.count(chr(219))
score+=50*count
count=list.count(chr(177))
score+=100*count
print('Your Score : ',score)
print('Highest score : 1500\n')
print('====================================')

