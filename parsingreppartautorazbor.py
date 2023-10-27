import json
from turtle import pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import requests
from bs4 import BeautifulSoup
import os
import shutil
import csv

headers = {
    "Accept" : "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

url = "https://yugrazbor.ru/catalog/auto"
service = Service(executable_path="C:\\Dev\\parsingselenium\\chromedriver\\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36")
driver = webdriver.Chrome(service=service, options=options)

""" with open("index_catalog.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
all_avto_hrefs = soup.find_all(class_="block-brands__item-link cursor-pointer")

all_avto_dict = {}
all_avto_dict_model = {}

for item in all_avto_hrefs:
    item_text = item.text
    item_text = item_text.replace("\n","")
    item_href = "https://yugrazbor.ru" + item.get("data-url")
    
    if item_text != "Колёса":
        all_avto_dict[item_text] = item_href
    

for model, model_href in all_avto_dict.items():
    
    if os.path.exists(model):
        print("Папки уже есть")
        break
    else:
        os.mkdir(model)
    
    
    driver.get(url=model_href)
    time.sleep(2)

    with open(f"{model}/{model}.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)
    with open(f"{model}/{model}.html", encoding="utf-8") as file:
        src_a = file.read()
    soup = BeautifulSoup(src_a, "lxml")
    all_avto_model_hrefs = soup.find_all(class_="block-brands__item-link cursor-pointer")
    
    for item_a in all_avto_model_hrefs:
        name_model = item_a.text
        
        name_model = name_model.replace("\n","")
        if os.path.exists(model):
            os.chdir(f"{model}")
            if os.path.exists(name_model):
                print("Папки уже есть")
                continue
            else:
                os.mkdir(name_model) # создание папок моделей в папках авто
                os.chdir('../') # подняться на уровень вверх

        name_href_model = "https://yugrazbor.ru" + item_a.get("data-url")
        all_avto_dict_model[name_model] = name_href_model
        #print(f"{name_model}: {name_href_model}")
with open("projects_data.json", "a", encoding="utf-8") as file:
     json.dump(all_avto_dict_model, file, indent=4, ensure_ascii=False)

for model, model_href in all_avto_dict.items():        
    shutil.rmtree(model)    
    #except Exception as ex:       
    #    print(ex)

with open('projects_data.json') as f:
    templates = json.load(f)

model_and_year = {}
for name, name_href in templates.items():
    driver.get(url=name_href)
    time.sleep(1)
        
    #os.mkdir('data')
    with open(f"{name}.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)
    with open(f"{name}.html", encoding="utf-8") as file:
        src_avto = file.read()
    soup = BeautifulSoup(src_avto, "lxml")
    model_avto = soup.find_all(class_="block-brands__item-link cursor-pointer")
    for item_n in model_avto:
        model_avto_name = item_n.text
        #print(model_avto_name)
        model_avto_name = model_avto_name.replace("\n","")
        href = "https://yugrazbor.ru" + item_n.get("data-url")
        #print(f"{model_avto_name}: {href}")
        model_and_year[model_avto_name] = href
    os.remove(f"{name}.html")
with open("modelu.json", "a", encoding="utf-8") as file:
    json.dump(model_and_year, file, indent=4, ensure_ascii=False) """        

""" with open('modelu.json', encoding="utf-8") as modelu_f:
    templates_f = json.load(modelu_f)

cards ={}
number_id = 0
for name_cards, cards_href in templates_f.items():
    name_cards = name_cards.replace("/","_")
    driver.get(url=cards_href)
    time.sleep(1)
    #print(name_cards, cards_href)
    with open(f"{name_cards}.html", "w", encoding="utf-8") as file:
        file.write(driver.page_source)
    with open(f"{name_cards}.html", encoding="utf-8") as file:
        info_card = file.read()
    soup = BeautifulSoup(info_card, "lxml")
    card_avto = soup.find_all(class_="img-bg img-bg--product-card")
    count_page = soup.find_all(class_="fs-6 fw-bold text-gray-700")
    #print(count_page)
    for page in count_page:
        page_text = page.text
        num_page = ""
        # print(page_text)
        num = ["0","1","2","3","4","5","6","7","8","9"]
        for char in page_text:
            if char in num:
                num_page = num_page + char
        print(num_page)
        pages = int(int(num_page) / 16)
        if int(num_page) > 16:
            cards_href = cards_href + "?page="
            for i in range(1, pages+2):
                # print(i)
                cards_href_i = cards_href + str(i)
                name_cards_i = name_cards + str(i)
                print(cards_href_i)
                with open(f"{name_cards_i}.html", "w", encoding="utf-8") as file:
                    file.write(driver.page_source)
                with open(f"{name_cards_i}.html", encoding="utf-8") as file:
                    info_card = file.read()
                soup = BeautifulSoup(info_card, "lxml")
                card_avto = soup.find_all(class_="img-bg img-bg--product-card")
                for item_card in card_avto:
                    href_spare_part = "https://yugrazbor.ru" + item_card.get("href")
                    # print(href_spare_part)
                    number_id += 1
                    print(number_id)
                    cards[number_id] = href_spare_part
                    #print(f"{number_id}: {href_spare_part}")
                os.remove(f"{name_cards_i}.html")
        else:
            for item_card in card_avto:
                href_spare_part = "https://yugrazbor.ru" + item_card.get("href")
                #print(href_spare_part)
                number_id += 1
                print(number_id)
                cards[number_id] = href_spare_part
                #print(f"{number_id}: {href_spare_part}")
    # print(name_cards, cards_href)
    os.remove(f"{name_cards}.html")
with open("cards_part.json", "a", encoding="utf-8") as file:
    json.dump(cards, file, indent=4, ensure_ascii=False) """

""" with open('cards_part.json', encoding="utf-8") as cards_repart:
    all_repart = json.load(cards_repart)

repeat = []
new_table = {}
povtor = 0
for number_card, href_repart in all_repart.items():
    if href_repart in repeat:
        print("Нашлась такая")
        povtor += 1
    else:
        repeat.append(href_repart)
        new_table[number_card] = href_repart

with open("new_table_href.json", "a", encoding="utf-8") as file:
    json.dump(new_table, file, indent=4, ensure_ascii=False) """

# cur_date = datetime.now().strftime("%d_%m_%Y")

with open(f"data_cur_date.csv", "w", encoding="utf-8") as file_data:
    writer = csv.writer(file_data)

    writer.writerow(
        (
            "Внутренний номер",
            "Запчасть",
            "Марка",
            "Модель",
            "Производитель",
            "Год",
            "Состояние",
            "Цена",
            "Ссылка",
        )
    )

with open('new_table_href.json', encoding="utf-8") as cards_repart:
    new_table = json.load(cards_repart)
spisok_part = []


for number_card, href_repart in new_table.items():
    r = requests.get(href_repart)
    if r.status_code == 200:
        driver.get(url=href_repart)
        time.sleep(1)
        #print(number_card, href_repart)
        with open(f"{number_card}.html", "w", encoding="utf-8", newline='') as file:
            file.write(driver.page_source)

        with open(f"{number_card}.html", encoding="utf-8") as file:
            info = file.read()

        soup = BeautifulSoup(info, "lxml")
        table = soup.find_all("td")
        price = soup.find("nobr").text.replace("\u202f", " ")
        name_part = soup.find(class_="product__title").text
        # print(name_part)
        A = []
        n = 0

        for attr in table:
            name_attr = attr.text.replace("\n","")
            A.append(name_attr)
            n += 1
        # print(A[0])

        #print(repeat)
        in_number = A[1]
        mark_model = 0
        model_model = 0
        manufacturer = 0
        year = 0
        state = 0
        print(in_number)
        for k in range(n-1):
            
            if A[k] == "Марка":
                mark_model = str(A[k+1])
            if A[k] == "Модель":
                model_model = (str(A[k+1]))
            if A[k] == "Производитель":
                manufacturer = (A[k+1])
            if A[k] == "Год":
                year = (str(A[k+1]))
            if A[k] == "Состояние":
                state = (A[k+1])
        spisok_part.append(
            {
            "Внутренний номер": in_number,
            "Запчасть": name_part,
            "Марка": mark_model, 
            "Модель": model_model, 
            "Производитель": manufacturer, 
            "Год": year, 
            "Состояние":state, 
            "Цена": price, 
            "Ссылка": href_repart
            }
        )

        file = open(f"data_cur_date.csv", "a", encoding="utf-8", newline='')
        writer = csv.writer(file)

        writer.writerow(
            (
                in_number,
                name_part,
                mark_model,
                model_model,
                manufacturer,
                year,
                state,
                price,
                href_repart
            )
        )
        file.close()

        os.remove(f"{number_card}.html")


    
      
with open("all_part.json", "a", encoding="utf-8") as file:
    json.dump(spisok_part, file, indent=4, ensure_ascii=False)  


#os.remove('cards_part.json')
#os.remove('projects_data.json')    
#os.remove('modelu.json')

driver.close()
driver.quit()