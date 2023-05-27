import pandas as pd
import numpy as n
from openpyxl import load_workbook
import matplotlib.pyplot as plt

#Tạo bảng
mau = pd.read_excel("D:/Duy/honda_sample.xlsx", index_col=None)
# danh_gia = ["Kém", "Trung bình", "Khá", "Tốt"]
# dk = [0, 2, 3, 4, 5]
# mau["Xếp loại"] = pd.cut(mau["Consumer_Rating"], bins=dk, labels=danh_gia)
# print("Bảng tổng lượt đánh giá qua các năm theo mức độ xếp loại")
# bang1 = pd.crosstab(index=mau["Year"], columns=mau["Xếp loại"])
# print(bang1)
#
# #lưu vào excel
# df = pd.read_excel("D:/Duy/honda_sample.xlsx", sheet_name="Sheet2")
# merged_df = pd.concat([df, bang1], ignore_index=False)
# book = load_workbook("D:/Duy/honda_sample.xlsx")
# writer = pd.ExcelWriter("D:/Duy/honda_sample.xlsx", engine='openpyxl')
# writer.book = book
# merged_df.to_excel(writer, sheet_name="Sheet2", index=False)
# writer.save()
#
# #VẼ đồ thị
# bang1.plot.bar()
# plt.xlabel("Năm")
# plt.ylabel("Lượt đánh giá (Triệu)")
# plt.title("Biểu đồ lượt đánh giá qua các năm")
# plt.grid(True)
# plt.show()
