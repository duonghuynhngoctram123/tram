# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:59:47 2024

@author: Student
"""

a= "Đại học Quốc gia, Khu phố 6, P. Linh Trung, Q. Thủ Đức, Tp. HCM"
s= a.split(", ")
print("Bảng 1")
for b in s:
    print(b)
print('')
print("Bảng 2")
s1= a.replace("P.", " ").replace("Q.", "").replace("Tp.","")
s2= s1.split(", ")
for c in s2:
    print(c)