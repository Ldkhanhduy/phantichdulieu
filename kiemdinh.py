import pandas as pd
import scipy.stats as sst

#Kiểm định giả thiết
print("Với giả thiết H0: tỉ lệ xe cũ không giảm\nGiả thiết đối H1: Tỉ lệ xe cũ giảm")
mau2 = pd.read_csv("D:/Baitap/BT_EXCEL/honda_sell_data.csv", index_col=None)
mau2 = mau2[mau2["Year"]==2023]
# mau = p.read_excel("D:/Duy/honda_sample.xlsx", index_col=None)
# print(mau["Condition"].value_counts())
a = pd.crosstab(index=mau2["Make"], columns=mau2["Condition"])
#Số lượng xe bán trong năm 2023
n = mau2.shape[0]
print("Số lượng xe bán trong 2023:", n)
#Số lượng xe cũ bán trong 2023
m = int(a["Used"])
print("Số lượng xe cũ bán trong 2023:", m)
#Tỉ lệ năm 2023
f = m/n
print("Tỉ lệ xe cũ bán trong 2023:", f)
#Tỉ lệ các năm trước
ff = 0.57
print("Tir lệ ở các năm trước:", ff)
print("Độ chính xác:", 0.05)
#Độ lệch chuẩn của ước lượng tỉ lệ
s = (ff*(1-ff)/n)**0.5
print("Độ lệch chuẩn:", s)
#Giá trị z-score
z = (ff-f)/s
print("Giá trị z:", z)
#Giá trị p-value với độ chính xác 5%
p = 1 - sst.norm.cdf(abs(z))
print("Giá trị p-value:", p)

if p > 0.05:
    print("Tỉ lệ bán xe cũ không giảm")
else:
    print("Bác bỏ H0. Suy ra tỉ lệ bán xe cũ có giảm")
