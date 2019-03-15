#!/usr/bin/env python
# coding: utf-8

# In[95]:


#import
import csv 

#open csv
f = open('fuzzy\DataTugas2.csv')
data = csv.reader(f)

x = []
y = []

for row in data:
    x.append(row[2])
    y.append(row[1])
    
del x[0]
del y[0]
#print (x[0])

def Fnaik (x, a, b):
    naik = (x-a)/(b-a)
    return naik
    
def Fturun (x, a, b):
    turun = -(x-b)/(b-a)
    return turun
       
    
def kPendapatan(y):
    pen=y
    rendah = 0.7
    sedang_kiri = 0.3
    sedang_kanan = 1.4
    tinggi = 1.0
    pendapatan_rendah = 0
    pendapatan_sedang = 0
    pendapatan_tinggi = 0
    keanggotaan = 0
    
    #rendah
    if pen<sedang_kiri:
        pendapatan_rendah = 1
        keanggotaan = pendapatan_rendah
    #rendah-sedang
    elif y<rendah and y>sedang_kiri:
        pendapatan_sedang = Fnaik(y, sedang_kiri, rendah)
        pendapatan_rendah = Fnaik(y, sedang_kiri, rendah)
        if pendapatan_sedang > pendapatan_rendah:
            keanggotaan = pendapatan_rendah
        else:
            keanggotaan = pendapatan_sedang
    #sedang
    elif y>rendah and y<tinggi:
        pendapatan_sedang = 1
        keanggotaan = pendapatan_sedang
    #sedang-tinggi
    elif y<sedang_kanan and y>tinggi:
        pendapatan_sedang = Fturun(y, tinggi, sedang_kanan)
        pendapatan_tinggi = Fnaik(y, tinggi, sedang_kanan)
        if pendapatan_sedang > pendapatan_tinggi:
            keanggotaan = pendapatan_sedang
        else:
            keanggotaan = pendapatan_tinggi
    #tinggi
    elif y>sedang_kanan:
        pendapatan_tinggi = 1
        keanggotaan = pendapatan_tinggi
    
    return keanggotaan


def kHutang(x):
    rendah = 25.000
    sedang_kiri = 15.000
    sedang_kanan = 75.000
    tinggi = 60.000
    hutang_rendah = 0
    hutang_sedang = 0
    hutang_tinggi = 0
    keanggotaan = 0
    
    #rendah
    if x>sedang_kiri:
        hutang_rendah = 1
        keanggotaan = hutang_rendah
    #rendah-sedang
    elif y<rendah and y>sedang_kiri:
        hutang_sedang = Fnaik(y, sedang_kiri, rendah)
        hutang_rendah = Fnaik(y, sedang_kiri, rendah)
        if hutang_sedang > hutang_rendah:
            keanggotaan = hutang_rendah
        else:
            keanggotaan = hutang_sedang
    #sedang
    elif y>rendah and y<tinggi:
        hutang_sedang = 1
        keanggotaan = hutang_sedang
    #sedang-tinggi
    elif y<sedang_kanan and y>tinggi:
        hutang_sedang = Fturun(y, tinggi, sedang_kanan)
        hutang_tinggi = Fnaik(y, tinggi, sedang_kanan)
        if hutang_sedang > hutang_tinggi:
            keanggotaan = hutang_sedang
        else:
            keanggotaan = hutang_tinggi
    #tinggi
    elif y>sedang_kanan:
        hutang_tinggi = 1
        keanggotaan = hutang_tinggi
            
    return keanggotaan

def inferensi(self):
    if self.kPendapatan(rendah) and self.kHutang(rendah):
        tidak = min(x,y)
        print ("tidak", tidak)
    #belumselesai
        
def sugeno(hasil, ya, tdk):
    #ya = 
    #tidak
    hasil = (ya*50 + tdk*100)/(ya+tdk)
    print (hasil)
    
#if sugeno(87.313,kPendapatan,kHutang) >= 80.000:
#    print ("ya")
#else:
#    print("Tidak")
print (x)
print (y)
        
        
 
# menutup file csv
f.close()



