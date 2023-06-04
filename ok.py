import pandas as pd
import numpy as n
import matplotlib.pyplot as plt

# columns = ['name', 'age', 'gender', 'job']
# user1 = pd.DataFrame([['alice', 19, "F", "student"],
# ['john', 26, "M", "student"]],
# columns=columns)
# user2 = pd.DataFrame([['eric', 22, "M", "student"],
# ['paul', 58, "F", "manager"]],
# columns=columns)
# user3 = pd.DataFrame(dict(name=['peter', 'julie'],
# age=[33, 44], gender=['M', 'F'],
# job=['engineer', 'scientist']))
# users = pd.concat([user1, user2, user3])
# # print(users)
# user4 = pd.DataFrame(dict(name=['alice', 'john', 'eric',
# 'julie'], height=[165, 180, 175, 171]))
# users = pd.merge(users, user4, on="name")
# print(users)
# score= pd.DataFrame(dict(name= ['alice', 'duy', 'thinh', 'long', 'khoa'],score=[10,8,5,6,3]))
# users = pd.merge(users, score, on="name")
# print(users)
# staked = pd.melt(users, id_vars="name", var_name="variable",
# value_name="value")
# print(staked)
# # print(users.loc[2,:])


#Đọc file csv về biển qua các năm
# doc = pd.read_csv("D:/Baitap/NgonnguR/Dataset/Temperature.csv", index_col=None)
# doc = pd.DataFrame(doc)
# print("Đọc toàn bộ dữ liệu")
# print(doc)
# print("đọc một đối tượng, đọc một đối tượng theo một thuộc tính mùa")
# print(doc[4:8])
# print(doc[6:8]["Season"])
# print("sắp xếp theo một mặn tăng dần")
# print(doc.sort_values("Salinity"))
# print("nhóm theo mùa và tính trung bình của độ mặn và độ CHLFa")
# print(doc.pivot_table(index="Season", values=["Salinity","CHLFa"],aggfunc=n.mean))
# print("nhóm theo mùa và tính tổng độ mặn và độ CHLFa")
# print(doc.pivot_table(index="Season", values=["Salinity", "CHLFa"], aggfunc=n.sum))


ga = pd.read_csv("D:/Baitap/BT_EXCEL/honda_sell_data.csv", index_col=False)
# print("Bảng tổng số xe bán được theo từng năm phân theo loại dẫn động")
# ga_1 = pd.crosstab(index=ga["Year"],columns=ga["Drivetrain"])
# print(ga_1)
# ga_1.tail(5).plot.bar()
# plt.show()
# fig, ax = plt.subplots()
# ax.hist(ga["Consumer_Rating"], bins="auto",ec='b', fc='r', alpha=0.5, density=True, cumulative=True)
# ax.legend()
# plt.show()
# plt.hexbin(ga["Consumer_Rating"],ga["Year"],gridsize=30, cmap="Blues")
# plt.colorbar()
# plt.show()
# print(ga["Consumer_Rating"].value_counts())
# ga_1 = ga.pivot_table(index="Year", columns="Condition", values="Price", aggfunc=sum)
# plt.pie([ga_1["Honda Certified"].sum(), ga_1["Used"].sum(), ga_1["New"].sum()],
#         labels=["Honda Certified", "Used", "New"],autopct='%1.1f%%',
#         startangle=15, shadow=True, explode=(0.1,0,0))
# plt.title("Biểu đồ phần trăm doanh thu theo tình trạng xe")
# plt.show()
# ga_1 = ga["Exterior_Color"].value_counts().sort_values()
# ga_1.plot.barh(fontsize=5)
# plt.title("Biểu đồ biễu diễn màu xe bán được nhiều nhất")
# plt.xlabel("Số lượng")
# plt.show()
# ga.boxplot(column="Price", by="Year")
# plt.title("Biểu đồ hình hộp cho doanh thu theo từng năm")
# plt.xlabel("Năm")
# plt.ylabel("Doanh thu")
# plt.show()
# ga_1 = pd.crosstab(index=ga["Year"],columns=ga["Fuel_Type"])
# print(ga_1)
# ga_1.tail(5)[["Gasoline", "Hybrid"]].plot(marker="*")
# print("Bảng tổng số xe bán được theo loại động cơ qua các năm")
# print(ga_1)
# plt.title("Biểu đồ thể hiện số xe bán được theo hai loại máy nhiên liệu từ 2019-2023")
# plt.ylabel("Số lượng")
# plt.grid(True)
# # plt.show()
# fig, ax = plt.subplots()
# ax.plot(ga_1.tail(5)["Hybrid"])
# ax.plot(ga_1.tail(5)["Gasoline"])
# ax.legend()
# plt.show()
# ga_2 = ga["Engine"].value_counts()
# print("Bảng tổng số xe bán được theo loại động cơ")
# print(ga_2)
# ga_2.sort_values().plot.barh(fontsize=5)
# plt.title("BIểu đồ tổng số xe bán được theo loại động cơ")
# plt.xlabel("Số lượng")
# plt.show()
"""
    Bài toán ước lượng số 5: 
Kiểm định có sự khác nhau về giá thành trung bình giữa mẫu xe Civic Sport và Pilot Sport.

Giả thuyết Ho: Giá thành trung bình Civic Sport = Giá thành trung bình Pilot Sport
Đối thuyết H1: Giá thành trung bình Civic Sport ≠ Giá thành trung bình Pilot Sport




    Phương pháp: 
Để kiểm tra điều này, ta thu thập ngẫu nhiên gồm 500 chiếc xe của hãng 
Vì ta nghi ngờ về phương sai của hai mẫu xe này là không bằng nhau nên ta sẽ sử dụng
phương pháp Phép thử t - Welch's.

    Các bước giải quyết bài toán:
+)  Bước 1: Tạo hàm kiểm định ttest_ind()
+)  Bước 2: Lọc dữ liệu
+)  Bước 3: Tiến hành kiểm định
+)  Bước 4: Diễn giải kết quả
"""

#   BƯỚC 1: TẠO HÀM KIỂM ĐỊNH TTEST_IND
#   Mã nguồn hàm ttest_ind do chính tay tôi tạo ra
from scipy.stats import t


def ttest_ind(data1, data2):
    # Kiểm tra đầu vào:
    if len(data1) == 0 or len(data2) == 0:
        raise ValueError("Mảng dữ liệu rỗng!")

    # Tính mean của mỗi mẫu
    mean1 = sum(data1) / len(data1)
    mean2 = sum(data2) / len(data2)

    # Tính phương sai của mỗi mẫu
    # Tuân theo phân phối student
    # Công thức tính phương sai là: σ^2 = (∑(i=1)→n〖(x_i - x_ngang)^2〗) / (n-1)
    variance1 = sum((x - mean1) ** 2 for x in data1) / (len(data1) - 1)
    variance2 = sum((x - mean2) ** 2 for x in data2) / (len(data2) - 1)

    # Tính độ lệch chuẩn của mỗi mẫu
    std1 = variance1 ** 0.5  # std1 = sqrt(variance1)
    std2 = variance2 ** 0.5  # std2 = sqrt(variance2)  

    # Tính thống kê kiểm định t
    # Tính phương sai tổng hợp
    pooled_variance = ((len(data1) - 1) * variance1 + (len(data2) - 1) * variance2) / (len(data1) + len(data2) - 2)
    # Tính giá trị t
    t_statistic = (mean1 - mean2) / (pooled_variance * (1 / len(data1) + 1 / len(data2))) ** 0.5

    # Tính xác suất ý nghĩa p-value
    # Tính bậc tự do
    """
        Bậc tự do là gì?
        Bậc tự do đề cập đến số lượng các giá trị độc lập tối đa của một hệ, 
    là các giá trị có thể thay đổi tự do trong mẫu dữ liệu. 
    """
    degrees_of_freedom = len(data1) + len(data2) - 2

    # Tính điểm giới hạn (giá trị gàng) critical_value
    critical_value = t.ppf(0.975, degrees_of_freedom)  # 0.475 = 1-alpha/2; với alpha=1-95%

    # Tính giá trị p
    # Thứ nhất, vì p-value là tích phân của miền ý nghĩa. Thứ 2, là vì miền này đối xứng
    # => Nhân 2
    p_value = 2 * (1 - abs(t.cdf(t_statistic, df=degrees_of_freedom)))

    # Trả về giá trị của t và p
    return t_statistic, p_value


#   BƯỚC 2: LỌC DỮ LIỆU
import pandas as pd
import numpy as np

# đọc dữ liệu MẪU
df = pd.read_excel("D:/Duy/honda_sample.xlsx")

# dữ liệu của mẫu xe Civic Sport
# print("Bảng Mẫu xe Civic Sport và Giá")
# print(df[139:154][["Model", "Price"]])
print("Danh sách Giá thành của mẫu xe Civic Sport")
data_civic = np.array(df[139:154]["Price"])
print(data_civic)

# dữ liệu của mẫu xe Pilot Sport
# print("Bảng Mẫu xe Pilot Sport và Giá")
# print(df[409:437][["Model", "Price"]])
print("Danh sách Giá thành của mẫu xe Pilot Sport")
data_pilot = np.array(df[409:437]["Price"])
print(data_pilot)

#   BƯỚC 3: TIẾN HÀNH KIỂM ĐỊNH
t_statistic, p_value = ttest_ind(data1=data_civic, data2=data_pilot)

#   BƯỚC 4: DIỄN GIẢI KẾT QUẢ

print("Thống kê kiểm định t=", t_statistic)

print("Với độ tin cậy là 95% thì giả thuyết Ho đúng với xác suất ý nghĩa p=", p_value)
