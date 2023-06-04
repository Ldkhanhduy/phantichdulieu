import pandas as pd
from scipy.stats import norm

pd.set_option('display.max_columns', None)  # Hiển thị tất cả các cột
pd.set_option('display.max_rows', None)  # Hiển thị tất cả các hàng
a = pd.read_excel("D:/Duy/honda_sample.xlsx")
danh_gia = ["0-2", "2.1-3", "3.1-4", "4.1-5"]
dk = [0, 2, 3, 4, 5]
a["Xếp loại"] = pd.cut(a["Consumer_Rating"], bins=dk, labels=danh_gia)
bang = pd.crosstab(index=a["Make"], columns=a["Xếp loại"])
print(bang)

#Số luợng mẫu
n = a.shape[0]
print("Số lượng mẫu:", n)
#Bảng giá trị
x = [1, 2.55, 3.55, 4.55]
f = [1, 18, 39, 442]
#Kì vọng
x_ = sum(i*j for i, j in zip(x, f))/n
print("Giá trị kì vọng:", x_)
#Độ lệch chuẩn hiệu chỉnh
s = (sum(i**2*j for i, j in zip(x, f))/(n-1))-x_**2 #Phương sai hiệu chỉnh
ss = s**0.5 #Độ lệch hiệu chỉnh
print("Độ lệch chuẩn hiệu chỉnh:", s)
#Giá trị u với alpha=0.99
u = abs(norm.ppf((1-0.99)/2))
print("Giá trị u với độ tin cậy là:", u)
#Giá trị sai số ước lượng
margin = u*ss/n**0.5
print("Khoảng sai số ước lượng là:", margin)
#Khoảng trung bình
print("Khoảng mức đánh giá trung bình là:", "(",x_-margin,",", x_+margin,")")



