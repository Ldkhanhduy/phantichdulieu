import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd
import matplotlib.pyplot as plt

mau = pd.read_csv("D:/Baitap/BT_EXCEL/honda_sell_data.csv", index_col=None)

a1 = mau[mau["Consumer_Rating"]==0]
a2 = mau[mau["Consumer_Rating"]==1]
a3 = mau[mau["Consumer_Rating"]==2]
a4 = mau[mau["Consumer_Rating"]==3]
a5 = mau[mau["Consumer_Rating"]==4]
a6 = mau[mau["Consumer_Rating"]==5]
a1 = a1.append(a2)
a1 = a1.append(a3)
a1 = a1.append(a4)
a1 = a1.append(a5)
a1 = a1.append(a6)
bang1 = a1.pivot_table(columns="Consumer_Rating", values="Price", aggfunc=sum)
print("Bảng doanh thu theo mức đánh giá")
print(bang1) #Bảng số liệu doanh thu theo mức đánh giá
plt.scatter(bang1.columns, bang1.tail(1))
plt.xlabel("Mức đánh giá")
plt.ylabel("USD")
plt.title("Biểu đồ doanh thu theo mức đánh giá")
plt.show()

x = np.array(bang1.columns).reshape(-1, 1) #Biến độc lập
y = np.array(bang1.tail(1)) #Biến phụ thuộc
hoiquy = LinearRegression().fit(x[:3], y[0][:3])
print("Hệ số tương quan mẫu:", np.corrcoef(x[:3].reshape(1, -1), y[0][:3]))
print("a=", hoiquy.coef_)
print("b=", hoiquy.intercept_)
print("Mô hình hồi quy theo mẫu từ 1,5 đến 4,0 là: y=", hoiquy.coef_[0],"x",hoiquy.intercept_)
print("Hệ số xác định:", hoiquy.score(x[:3], y[0][:3]))

#Dự đoán
print("Dự đoán doanh thu ở mức 4.2 theo xu hướng từ mức 2.0-4.0:", hoiquy.coef_*4.2+hoiquy.intercept_)
#Mô hình hồi quy
a = np.linspace(start=2, stop=5, num=7)
b = hoiquy.coef_*a+hoiquy.intercept_
plt.scatter(bang1.columns, bang1.tail(1))
plt.plot(a, b, color="r")
plt.xlabel("Mức đánh giá")
plt.ylabel("USD")
plt.title("Biểu đồ doanh thu theo mức đánh giá")
plt.show()

