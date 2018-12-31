from Squirtle import Squirtle
from collections import OrderedDict

model = Squirtle()
fields = OrderedDict([])
key = 'squirtle'
value = ''
#model.generate_csv()
print("Welcome to Squirtle DATA Scrapper")
data_format = input("Export data format ? [CSV/JSON]")
model.page_url = input("Web page URL with pagination included (ex : website.tn/index.php?pgn=) :")
is_download = input("Would you like to Download images into a Folder ? [Y/N]")
if is_download == "Y":
    model.isDownload = True
    model.dir = input("Name the folder to save images into : ")

model.max_pages = int (input("Max pages to scrapp :"))
model.limit_per_page = input("Limit of Items to scrapp per page [None]:")
if model.limit_per_page == 'None':
    model.limit_per_page = None
else:
    model.limit_per_page = int(model.limit_per_page)

model.item_selector = input("DOM selector of link which contains item link :")

print("Now passing to the Step 2 :")
print("In this step you need to introduce each element you want to extract :")
print("Please note that ID will be generated and Link will be saved Automatically :")
key = input("Field Name :")

while key != '':
    value = input("DOM Selector :")
    key = input("Field Name :")
    fields[key] = value

model.fields = fields

if data_format == 'CSV':
    model.generate_csv()
elif data_format == 'JSON':
    model.get_json()
