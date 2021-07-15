"""
    wiki scraping is a small program aimed at learning Beautifulsoup 
    and collecting biographies by name.
    
    technologies:
        beautifulsoup
        request
        python
        
    Ultilidades:
        Coletar dados da biografia e coletar dados
"""

from time import strftime  #  save the date
from bs4 import BeautifulSoup  #  Walk over the desired tag 
import requests  #  Make tag or site request

def salve_data(info):
    """
    After analyzing the biography and capturing the data, save_data()
    will save the data in a .txt file
    """
    time = strftime("%Y/%m/%d")  #  
    with open(f"{name}.txt", "a") as file:
        file.write(f"Biografia de {name} criada em {time}")  #  File title with name and date
        file.write(info)  #  Write the bibliography in the file

def get_info(soup):
    """
    Changing the html will make three attempts to look for the class 
    with different infoboxes, so it will return info.
    """
    try:
        info = soup.find('table', {'class': 'infobox infobox infobox_v2'}).text
        return info
    except:
        try:
            info = soup.find('table', {'class': 'infobox'}).text
            return info
        except:
            try:
                info = soup.find('table', {'class': 'infobox infobox_v2'}).text
                return info
            except:
                pass

def main():
    global name
    #  Entry with the name of the bibliography, remove spaces and capitalize initials to work.
    name = str(input("Nome da biografia: ")).strip().title()
    #  url formatting
    url = f"https://pt.wikipedia.org/wiki/{name}"
    #  making url request
    response = requests.get(url)
    #  Getting in text from url with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    salve_data(get_info(soup))
    
if __name__ == "__main__":
    main()