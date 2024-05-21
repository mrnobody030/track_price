import requests , time , openpyxl 
from bs4 import BeautifulSoup


proxies = {
    'http': "http://213.233.177.134:80"
}
#get the web page url
def add_price (url,excel):
    source=requests.get(url,proxies=proxies)
#take the price and date from the webspage 
    soup = BeautifulSoup(source.text,"html.parser")
    price = soup.find("p" , class_="MuiTypography-root MuiTypography-body1 muirtl-22intj").text
    date = soup.find("h1" , class_="MuiTypography-root MuiTypography-h1 muirtl-kj2ua").text[11:]
#find the excel file
    excelfile = openpyxl.load_workbook(excel)
    sheet1 = excelfile.active
#check if the date is alredy there or not 
#if its not in the xxl file then add it
    for x in range(1,999999):
        if sheet1["A" + str(x)].value == None:
            if sheet1["A" + str(x-1)].value == date:
                return("program was sucessful BUT this date alredy exist in the list")
            else:
                sheet1["A" + str(x)].value = date
                sheet1["B" + str(x)].value = price
                return("the prices and date secessfully got added to the list")
            break
    excelfile.save(excel)

while True:
    print(add_price(r"https://karnameh.com/car-price/arisun",r"xlsx_files\Arisan.xlsx"))
    time.sleep(120)
    print(add_price(r"https://karnameh.com/car-price?search=%D8%A7%D9%85%E2%80%8C%D9%88%DB%8C%E2%80%8C%D8%A7%D9%85+X55+Pro+%D8%A7%DA%A9%D8%B3%D9%84%D9%86%D8%AA",r"xlsx_files\mvm.xlsx"))
    time.sleep(120)
    print(add_price(r"https://karnameh.com/car-price?search=%D9%BE%DA%98%D9%88+%D9%BE%D8%A7%D8%B1%D8%B3+%D8%AF%D9%88%DA%AF%D8%A7%D9%86%D9%87+%D8%B3%D9%88%D8%B2",r"xlsx_files\pejo pars.xlsx"))
    time.sleep(120)
    print(add_price(r"https://karnameh.com/car-price?search=%DA%A9%D9%88%DB%8C%DB%8C%DA%A9+%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9+R",r"xlsx_files\Quick.xlsx"))
    time.sleep(120)
    print(add_price(r"https://karnameh.com/car-price?search=%D8%AA%D8%A7%D8%B1%D8%A7+%D8%A7%D8%AA%D9%88%D9%85%D8%A7%D8%AA%DB%8C%DA%A9+V2",r"xlsx_files\tara.xlsx"))
    time.sleep(120)
    print(add_price(r"https://karnameh.com/car-price?search=%D8%B1%D8%A7%D9%86%D8%A7+%D9%BE%D9%84%D8%A7%D8%B3",r"xlsx_files\rana.xlsx"))

    time.sleep(60*60*6)
