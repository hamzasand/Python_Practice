## Menu generater
item_1 = "Baryani"
item_2 = "Palao"
item_3 = "Kheer"
item_4 = "Qurma"

price_item_1 = "RS.300"
price_item_2 = "RS.400"
price_item_3 = "RS.500"
price_item_4 = "RS.600"

len_dash_1 = 20 - len(item_1) - len(price_item_1)
len_dash_2 = 20 - len(item_2) - len(price_item_2)
len_dash_3 = 20 - len(item_3) - len(price_item_3)
len_dash_4 = 20 - len(item_4) - len(price_item_4)
print(item_1 + "-"*len_dash_1 + price_item_1 + "\n" +
      item_2 + "-"*len_dash_2 + price_item_2 + "\n" +
      item_3 + "-"*len_dash_3 + price_item_3 + "\n" +
      item_4 + "-"*len_dash_4 + price_item_4)
