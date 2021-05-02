import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from tkinter import *
from tkinter import scrolledtext

#HEADERS = {'user-agent': 'Mozilla/5.0 (Windows; U; Windows NT 6.1) AppleWebKit/533.28.5 (KHTML, like Gecko) Version/5.0.3 Safari/533.28.5'}
#HEADERS = {'user-agent': 'Opera/8.45 (Windows NT 5.1; en-US) Presto/2.8.232 Version/12.00'}
HEADERS = {'user-agent': 'Mozilla/5.0 (iPad; CPU OS 7_1_2 like Mac OS X; sl-SI) AppleWebKit/533.4.6 (KHTML, like Gecko) Version/4.0.5 Mobile/8B112 Safari/6533.4.6'}
# Headers need to be like a real user
def get_html(url, params=None):
    """
    Sending request to the site. Successful connection to the site is 200.
    Header uses here.
    :param url:
    :param params:
    :return:
    """
    return requests.get(url, headers=HEADERS, params=params)

def parsing(url):
    """
    Parsing site, using BeautifulSoup. Studied the structure of the site and brought out the element I needed.
    :param url:
    :return:
    """
    soup = bs(url, "lxml")
    elements = soup.find_all('div', class_="Specifications__row")
    data = {}
    for element in  elements:
        name = element.find('div',class_="Specifications__column Specifications__column_name").get_text(strip=True)
        value = element.find('div',class_="Specifications__column Specifications__column_value").get_text(strip=True)
        data.update({
            name: value
        })

    return data

def start_parser(web):
    """
    Main function.
    Here, I combined all the function for parsing content from the site
    :param web:
    :return:
    """
    html = get_html(web)
    if html.status_code==200:
        return  parsing(get_html(web).text)
    else:
        return print(html.status_code, ' NONE')


def find_dd(filename,name):
    """
    Function for output table in application
    :param filename:
    :param name:
    :return:
    """
    for i in filename['Name']:
        if name.lower() in i.lower():
            result = filename.groupby('Name').get_group(i)
            return result.drop(['Url', 'Unnamed: 0', 'In stock'], axis=1)
    else:
        return 'Nothing'

def find_ch(filename, name):
    """
    Function for output characteristics in application

    :param filename:
    :param name:
    :return:
    """
    for i in filename['Name']:
        if name.lower() in i.lower():
            result = filename.groupby('Name').get_group(i)
            a = result['Url'].tolist()[0]
            return pd.DataFrame([start_parser(a)]).T
    else:
        return 'Nothing'

# Using tkinter I created application

root = Tk()
root.config(bg='#37f3fa')
root.title('Citilink')
root.geometry('1000x700')

def show1():
    """
    Buttons function
    :return:
    """
    a = comp.get()
    kompyutery = pd.read_csv('kompyutery.csv')

    Ans = find_dd(kompyutery, comp.get())
    if a:
        text.delete(0.0, END)
        text.insert(0.0, Ans)
    else:
        text.delete(0.0, END)

def show2():
    a = lap.get()
    noutbuki = pd.read_csv('noutbuki.csv')

    Ans = find_dd(noutbuki,lap.get())
    if a:
        text.delete(0.0, END)
        text.insert(0.0, Ans)
    else:
        text.delete(0.0, END)

def show3():
    a = ult.get()
    ultrabuki = pd.read_csv('ultrabuki.csv')
    Ans = find_dd(ultrabuki, ult.get())
    if a:
        text.delete(0.0, END)
        text.insert(0.0, Ans)
    else:
        text.delete(0.0, END)

def show4():
    a = mono.get()
    monobloki = pd.read_csv('monobloki.csv')

    Ans = find_dd(monobloki, mono.get())
    if a:
        text.delete(0.0, END)
        text.insert(0.0, Ans)
    else:
        text.delete(0.0, END)

def show5():
    a = smart.get()
    smartfony = pd.read_csv('smartfony.csv')
    Ans = find_dd(smartfony, smart.get())
    if a:
        text.delete(0.0, END)
        text.insert(0.0, Ans)
    else:
        text.delete(0.0, END)

def show6():
    a = tab.get()
    planshety = pd.read_csv('planshety.csv')

    Ans = find_dd(planshety,tab.get())
    if a:
        text.delete(0.0, END)
        text.insert(0.0, Ans)
    else:
        text.delete(0.0, END)


def show_1():
    a = comp.get()
    kompyutery = pd.read_csv('kompyutery.csv')

    Ans = find_ch(kompyutery, comp.get())
    if a:
        txt.delete(0.0, END)
        txt.insert(0.0, Ans)
    else:
        txt.delete(0.0, END)

def show_2():
    a = lap.get()
    noutbuki = pd.read_csv('noutbuki.csv')

    Ans = find_ch(noutbuki, lap.get())
    if a:
        txt.delete(0.0, END)
        txt.insert(0.0, Ans)
    else:
        txt.delete(0.0, END)

def show_3():
    a = ult.get()
    ultrabuki = pd.read_csv('ultrabuki.csv')
    Ans = find_ch(ultrabuki, ult.get())
    if a:
        txt.delete(0.0, END)
        txt.insert(0.0, Ans)
    else:
        txt.delete(0.0, END)

def show_4():
    a = mono.get()
    monobloki = pd.read_csv('monobloki.csv')

    Ans = find_ch(monobloki, mono.get())
    if a:
        txt.delete(0.0, END)
        txt.insert(0.0, Ans)
    else:
        txt.delete(0.0, END)

def show_5():
    a = smart.get()
    smartfony = pd.read_csv('smartfony.csv')
    Ans = find_ch(smartfony, smart.get())
    if a:
        txt.delete(0.0, END)
        txt.insert(0.0, Ans)
    else:
        txt.delete(0.0, END)

def show_6():
    a = tab.get()
    planshety = pd.read_csv('planshety.csv')

    Ans = find_ch(planshety, tab.get())
    if a:
        txt.delete(0.0, END)
        txt.insert(0.0, Ans)
    else:
        txt.delete(0.0, END)


Label(root, text='Welcome to app', font=('Arial', 30, 'italic'), padx=15, relief=RAISED, bd=7).pack()

frame_top = Frame(root, bg='#00ff99', bd=5)
frame_top.place(relx=0.15, rely=0.1, relwidth=0.7, relheight=0.35)

Label(frame_top, text='Computers', font=('Arial', 13, 'bold'), relief=RAISED).grid(row=1, column=3)
Label(frame_top, text='Laptops', font=('Arial', 13, 'bold'), relief=RAISED).grid(row=2, column=3)
Label(frame_top, text='Ultrabooks', font=('Arial', 13, 'bold'), relief=RAISED).grid(row=3, column=3)
Label(frame_top, text='Monoblocks', font=('Arial', 13, 'bold'), relief=RAISED).grid(row=4, column=3)
Label(frame_top, text='Smartphones', font=('Arial', 13, 'bold'), relief=RAISED).grid(row=5, column=3)
Label(frame_top, text='Tablets', font=('Arial', 13, 'bold'), relief=RAISED).grid(row=6, column=3)

# Function  "Entry"  for inputs
comp = Entry(frame_top, bg='white', font=30)
comp.grid(row=1, column=6)
lap = Entry(frame_top, bg='white', font=30)
lap.grid(row=2, column=6)
ult = Entry(frame_top, bg='white', font=30)
ult.grid(row=3, column=6)
mono = Entry(frame_top, bg='white', font=30)
mono.grid(row=4, column=6)
smart = Entry(frame_top, bg='white', font=30)
smart.grid(row=5, column=6)
tab = Entry(frame_top, bg='white', font=30)
tab.grid(row=6, column=6)

# Buttons
Button(frame_top, text='Show table!',font=('Arial', 13, 'bold'), relief=RAISED, command=show1).grid(row=1, column=9)
Button(frame_top, text='Show table!',font=('Arial', 13, 'bold'), relief=RAISED, command=show2).grid(row=2, column=9)
Button(frame_top, text='Show table!',font=('Arial', 13, 'bold'), relief=RAISED, command=show3).grid(row=3, column=9)
Button(frame_top, text='Show table!',font=('Arial', 13, 'bold'), relief=RAISED, command=show4).grid(row=4, column=9)
Button(frame_top, text='Show table!',font=('Arial', 13, 'bold'), relief=RAISED, command=show5).grid(row=5, column=9)
Button(frame_top, text='Show table!',font=('Arial', 13, 'bold'), relief=RAISED, command=show6).grid(row=6, column=9)

Button(frame_top, text='Show characteristics!',font=('Arial', 13, 'bold'),relief=RAISED, command=show_1).grid(row=1, column=12)
Button(frame_top, text='Show characteristics!',font=('Arial', 13, 'bold'),relief=RAISED, command=show_2).grid(row=2, column=12)
Button(frame_top, text='Show characteristics!',font=('Arial', 13, 'bold'),relief=RAISED, command=show_3).grid(row=3, column=12)
Button(frame_top, text='Show characteristics!',font=('Arial', 13, 'bold'),relief=RAISED, command=show_4).grid(row=4, column=12)
Button(frame_top, text='Show characteristics!',font=('Arial', 13, 'bold'),relief=RAISED, command=show_5).grid(row=5, column=12)
Button(frame_top, text='Show characteristics!',font=('Arial', 13, 'bold'),relief=RAISED, command=show_6).grid(row=6, column=12)

# Creating frame for output
frame_bottom = Frame(root, bg='#7249c4', bd=10)
frame_bottom.place(relx=0.1, rely=0.48, relwidth=0.8, relheight=0.5)

info = Label(frame_bottom, text='Answer - Table', bg='#e7dbff', font=40)
info.grid(row=0, column=0, stick='we')

info = Label(frame_bottom, text='Answer - characteristics', bg='#e7dbff', font=40)
info.grid(row=2, column=0, stick='we')
# ScrolledText for scrolling
text = scrolledtext.ScrolledText(frame_bottom, width=95, height=9)
text.grid(row=1, column=0,stick='we')
txt = scrolledtext.ScrolledText(frame_bottom, width=95, height=9)
txt.grid(row=3, column=0,stick='we')
root.resizable(width=False, height=False)

root.mainloop()