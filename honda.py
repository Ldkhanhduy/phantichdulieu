import pandas as p
import random as r

def sample(link):
    ga = p.read_csv(link, index_col=None)
    ga1 = ga[ga["Year"]<2023]
    mau = p.DataFrame()
    a = r.sample(range(3411), 500)
    for i in range(len(a)):
        mau = mau.append(ga1[a[i]-1:a[i]])

    mau.to_excel("D:/Duy/honda_sample.xlsx")
    print("Mẫu lấy được:")
    print(mau)

if __name__ == '__main__':
    a = "D:/Baitap/BT_EXCEL/honda_sell_data.csv"
    sample(a)