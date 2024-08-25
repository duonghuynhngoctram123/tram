# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 08:49:59 2024

@author: Student
"""

print("=========MENU=========")
print("1.Hu tieu")
print("2.Chao long")
print("3.Banh canh")
print("4.Bun rieu")
print("5.Pho bo")
print("======================")
a=int(input("Nhập lựa chọn"))
if a==1:
    print("Món bạn chọn là Hủ tiếu")
elif a==2:
    print("Món bạn chọn là Cháo lòng")
elif a==3:
    print("Món bạn chọn là Bánh canh")
elif a==4:
    print("Món bạn chọn là Bún riêu")
elif a==5:
    print("Món bạn chọn là Phở bò")
elif a>4 or a<1:
    print("Món bạn chọn hok có trong menu")
    print("=====================")
    
