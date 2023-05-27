import pandas as p

docdulieu = p.read_csv("D:/Baitap/BT_EXCEL/honda_sell_data.csv", index_col=None)
print(docdulieu[docdulieu["Year"]<2023])
