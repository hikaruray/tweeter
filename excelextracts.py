from openpyxl import load_workbook

book = load_workbook("C:/Users/MNishihira/Desktop/tweetlist (Autosaved).xlsx")

ws = book['Vocal']

all_rows = list(ws.rows)
all_column = list(ws.columns)

tweetlist = []
for cell in all_column[1]:
    tweetlist.append(cell.value)

hashtaglist = []
for tag in all_column[3]:
    hashtaglist.append(tag.value)

url_list = []
for url in all_column[5]:
    url_list.append(url.value)

final_list = []
for num in range(3,101):
    full_tweet = f"{tweetlist[num]} \n \n {url_list[num]} \n {hashtaglist[num]}"
    final_list.append(full_tweet)

