import pandas as pd
import numpy as np


def searchWord(search):
    matching_indices = df.index[search == df['abbr']].tolist()
    # print(matching_indices)
    if matching_indices:
        for index in matching_indices:    
            searchList = df.loc[index].values
            
            print("=" * 20)
            print(f"縮寫：{searchList[0]}\n全名：{searchList[1]} \n中文：{searchList[2]}\n備註：{searchList[3]}\n")
    else:
        print('not found\n是否寫入？')
        answer = input("y/n：")
        if(answer.lower() == 'y'):
            writeWord(search)
        else:
            print('End the program')
        
        
        
def writeWord(search):
    abbr = (search.strip()).upper()
    fullName = input("輸入全名 enter跳過：")
    chinese = input("輸入中文：")
    note = input("輸入備註 enter跳過：")
    # 創建一個 DataFrame
    data = {
        'abbr': abbr,
        'full-name': fullName,
        'chinese':chinese,
        'note': note,
    }
    
    df = pd.DataFrame(data, index=[length-2])
    df.to_csv('wordSearch.csv', index=False, mode="a+", header=False)
    print("寫入完成")
    




df = pd.read_csv("wordSearch.csv")
target = list(df['abbr'].values)
length = len(target)

while True:
    enter = (input('搜尋（輸入 q 退出）：').strip()).upper()
    
    if enter == 'Q':
        break
    searchWord(enter)
