import numpy
import random

answer_addition = 1
answer_subtraction = 2
answer_multiplication = 3
answer_random = 4
answer_input = 5

while True:
    try:
       choice_1 = int(input("Toplama için 1, çıkartma için 2, çarpma işlemi için 3'e basın.  "))
       if (choice_1 < 1 or choice_1 > 3):
           print("Geçerli bir değer girin.")
           continue
    except ValueError:
        print("Geçerli bir değer girin.")
        continue
    break
while True:
    try:
       Row_1    = int(input("İlk matris için sıra sayısı girin: "))
    except ValueError:
        print("Geçerli bir değer girin.")
        continue
    break
while True:
    try:
       Column_1 = int(input("İlk matris için sütun sayısı girin: "))
    except ValueError:
        print("Geçerli bir değer girin.")
        continue
    break
while True:
    try:
       Row_2    = int(input("İkinci matris için sıra sayısı girin: "))
    except ValueError:
           print("Geçerli bir değer girin.")
           continue
    break
while True:
    try:
       Column_2 = int(input("İkinci matris için sütun sayısı girin: "))
    except ValueError:
        print("Geçerli bir değer girin.")
        continue
    break
while True:
    try:
       choice_2 = int(input("Sayıların rastgele mi yoksa elle mi girileceğini seçin. Rastgele için 4, elle giriş için 5: "))
       if (choice_2 < 4 or choice_2 > 5):
           print("Geçerli bir değer girin.")
           continue
    except ValueError:
        print("Geçerli bir değer girin.")
        continue
    break

x=Row_1
y=Column_1
z=Row_2
w=Column_2

matrix_A =[]
matrix_B =[]

def addition_input(x,y,z,w): 
    if (x==z) and (z==w):
        eleman_sayısı_1 = str(x*y)
        print("İlk matris için "+eleman_sayısı_1+" tane eleman girin. Girilen her elemandan sonra enter tuşuna basın. ") 
        numpy.matrix_A = [] 
        for i in range(x): 
            a =[] 
            for j in range(y):  
                while True:
                    try:
                      a.append(int(input())) 
                    except ValueError:
                        print("Geçerli bir değer girin.")
                        continue
                    break
            matrix_A.append(a) 
        print("İlk matris: ")
        print(matrix_A)
        eleman_sayısı_2 = str(z*w)
        print("İkinci matris için "+eleman_sayısı_2+" elemanlarını  girin. Girilen her elemandan sonra enter tuşuna basın.  ")
        numpy.matrix_B =[]
        for i in range(z):
            b = []
            for j in range(w):
                while True:
                    try:
                       b.append(int(input()))
                    except ValueError:
                        print("Geçerli bir değer girin.")
                        continue
                    break
            matrix_B.append(b)
        print("İkinci matris: ")
        print(matrix_B)
        print("İlk ve ikinci matrisin toplamı:  ")
        print(numpy.add(matrix_A,matrix_B))
    else:
        print("Toplama işlemi için matris boyutları aynı olmalı.")

def addition_random(x,y,z,w):
    if (x==z) and (z==w):
        choice_random = int(input("Matris elemanları için maximum sayıyı girin: "))
        numpy.matrix_A = []
        numpy.matrix_B = []
        A = numpy.random.randint(choice_random, size= (x,y))
        B = numpy.random.randint(choice_random, size=(z,w))
        print("İlk random matris: ")
        print(A)
        print("İkinci random matris: ")
        print(B)
        print("İlk ve ikinci matrisin toplamı:  ")
        print(numpy.add(A,B))        
    else:
        print("Toplama işlemi için matris boyutları aynı olmalı.")     

def subtraction_input(x,y,z,w):
    if (x==z) and (z==w):
        eleman_sayısı_1 = str(x*y)
        print("İlk matris için "+eleman_sayısı_1+" tane eleman girin. Girilen her elemandan sonra enter tuşuna basın. ")
        numpy.matrix_A = [] 
        for i in range(x): 
            a =[] 
            for j in range(y):  
                while True:
                    try:
                       a.append(int(input())) 
                    except ValueError:
                        print("Geçerli bir değer girin.")
                        continue
                    break
            matrix_A.append(a) 
        print("İlk matris:  ")
        print(matrix_A)
        eleman_sayısı_2= str(z*w)
        print("İkinci matris için "+eleman_sayısı_2+" tane eleman girin. Girilen her elemandan sonra enter tuşuna basın. ")
        numpy.matrix_B =[]
        for i in range(z):
            b = []
            for j in range(w):
                while True:
                    try:
                      b.append(int(input()))
                    except ValueError:
                        print("Geçerli bir değer girin.")
                        continue
                    break
            matrix_B.append(b)
        print("İkinci matris: ")
        print(matrix_B)
        print("İki matrisin çıkartması: ")
        print(numpy.subtract(matrix_A,matrix_B))
    else:
        print("Çıkartma işlemi için matris boyutları aynı olmalı.")

def subtraction_random(x,y,z,w):
    if (x==z) and (z==w):
        choice_random = int(input("Matris elemanları için maximum sayıyı girin: "))
        numpy.matrix_A = []
        numpy.matrix_B = []
        A = numpy.random.randint(choice_random, size= (x,y))
        B = numpy.random.randint(choice_random, size=(z,w))
        print("İlk random matris:  ")
        print(A)
        print("İkinci random matris: ")
        print(B)
        print("İki matrisin çıkartması: ")
        print(numpy.subtract(A,B))        
    else:
        print("Çıkartma işlemi için matris boyutları aynı olmalı. ")

def multiplication_input(x,y,z,w):
    if (y == z):
        eleman_sayısı_1 = str(x*y)
        print("İlk matris için "+eleman_sayısı_1+" tane eleman girin. Girilen her elemandan sonra enter tuşuna basın.  ")
        numpy.matrix_A = [] 
        for i in range(x): 
            a =[] 
            for j in range(y):  
                while True:
                    try:
                       a.append(int(input())) 
                    except ValueError:
                        print("Geçerli bir değer girin.")
                        continue
                    break
            matrix_A.append(a) 
        print("İlk matris: ")
        print(matrix_A)
        eleman_sayısı_2 = str(z*w)
        print("İkinci matris için "+eleman_sayısı_2+" tane eleman girin. Girilen her elemandan sonra enter tuşuna basın. ")
        numpy.matrix_B =[]
        for i in range(z):
            b = []
            for j in range(w):
                while True:
                    try:
                      b.append(int(input()))
                    except ValueError:
                        print("Geçerli bir değer girin. ")
                        continue
                    break
            matrix_B.append(b)
        print("İkinci matris: ")
        print(matrix_B)
        print("İki matrisin çarpımı:  ")
        print(numpy.dot(matrix_A,matrix_B))
    else:
        print("İşlemin gerçekleştirilebilmesi için ilk matrisin sütunu ile ikinci matrisin satırı aynı olmalı. ")

def multiplication_random(x,y,z,w):
    if (y == z):
        choice_random = int(input("Matris elemanları için maximum sayıyı girin: "))
        numpy.matrix_A = []
        numpy.matrix_B = []
        A = numpy.random.randint(choice_random, size= (x,y))
        B = numpy.random.randint(choice_random, size=(z,w))
        print("İlk random matris: ")
        print(A)
        print("İkinci random matris: ")
        print(B)
        print("İki matrisin çarpımı:  ")
        print(numpy.dot(A,B))        
    else:
        print("İşlemin gerçekleştirilebilmesi için ilk matrisin sütunu ile ikinci matrisin satırı aynı olmalı.")

if (choice_1 == answer_addition):
    if (choice_2 == answer_random):
        addition_random(x, y,z, w)
    elif (choice_2 == answer_input):
        addition_input(x, y, z, w)
elif (choice_1 == answer_subtraction):
    if (choice_2 == answer_random):
        subtraction_random(x,y,z,w)
    elif (choice_2 == answer_input):
        subtraction_input(x,y,z,w)
elif (choice_1 == answer_multiplication):
    if (choice_2 == answer_random):
        multiplication_random(x,y,z,w)
    elif (choice_2 == answer_input):
        multiplication_input(x,y,z,w)
