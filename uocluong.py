import statsmodels.stats.proportion as prop
import pandas as pd

#Bài toán ước lượng tỉ lệ xe c bán được từ trước nay đến 2022
mau = pd.read_excel("D:/Duy/honda_sample.xlsx", index_col=None)
a = pd.crosstab(index=mau["Make"], columns=mau["Condition"]) #bang tan so 
#Số lượng mẫu
n = mau.shape[0]
print("Số lượng mẫu:", n)
#Số lượng xe cũ
m = int(a["Used"])
print("Số lượng xe cũ:", m)
#Tỉ lệ mẫu
f = m/n
print("Tỉ lệ mẫu:", f)
#Với độ tin cậy 95%, khoảng ước lượng tỉ lệ là
khoang = prop.proportion_confint(m, n, alpha=0.05) #ham tinh khoang uoc luong ti le
print("Với độ tin cậy là 95%, khoảng ước lượng tỉ lệ bán xe cũ là:", khoang)
