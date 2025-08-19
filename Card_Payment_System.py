Card_Num = "1234 1234 1234 5678"
last_dig = Card_Num[15:]
hide_num = "X" * 4 + " "
Final_hide = hide_num*4 + last_dig
print(f"Recently detect the some amount from you card :{Final_hide}")