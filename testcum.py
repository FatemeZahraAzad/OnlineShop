import csv
lst =[]
with open('user.csv','r') as file:
    reader = csv.DictReader(file)
    reader2 = list(reader)
    for i in reader2:
        lst.append(f"{i['store_name']} : {i['Login_time']} to {i['Exit_time']}")
final_new_menu = list(dict.fromkeys(lst))
for i in final_new_menu:
    print(i)         # None : None to None ?!

test="چیزی که کاربر انتخاب میکنه"
with open('goods.csv','r') as file:   # r+
    reader = csv.DictReader(file)
    for i in reader:
        if test in i['store']:
            print(f"   {i['product_name']} >> {i['brand']} brand | For the price of {i['price']} Toman")
        else:
            print("The store name entered in the application list is not available")

#buy.buy.selection_of_goods

#________________________________________________________________(نمایش اسم فروشگاه ها برای مشتری و انتخاب یکی)
test = "ok"
with open('goods.csv','r') as file:   # r+
    reader = csv.DictReader(file)
    for i in reader:
        if test in i['store']:
            print(f"   {i['product_name']} >> {i['brand']} brand | For the price of {i['price']} Toman")
    else:
        print("The store name entered in the application list is not available\nPlease try again later")

#buy.buy.selection_of_goods

#_______________________________________________________________(جست و جوی فروشگاه سپس اقدام به خرید)

test = "icecream"                               #سه تا شرط میگیره اینجا
with open('goods.csv','r') as file:       #چون که بر اساس اسم و برند و قیمت جست و جو کنه
    reader = csv.DictReader(file)
    for i in reader:
        if test in i['product_name']:
            print(i)
    else:
        print("The store name entered in the application list is not available\nPlease try again later")
#___________________________________________________________________(جست و جوی کالا)

#(فاکتور داراییه قسمتی هست که نشون بده خرید تایید شده اس یا نه)نمایش پیش فاکتور!!!!!!!!!!!!!!

#__________________________________________________________________

# تایی خرید یا ویرایش ان(مند ادیت تمرین 7)

#____________________________________________________________________

#خروج و ذخیره سبد خرید مشتری