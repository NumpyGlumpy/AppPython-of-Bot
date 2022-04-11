from kivy.app import App
import requests
from bs4 import BeautifulSoup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config

Config.set("graphics", "resizeable", 0)
Config.set("graphics", "width", 400)
Config.set("graphics", "height", 600)
class Application(App):
    def click(self, instance):
        weather = "https://www.gismeteo.ru/weather-kazan-4364/now/"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
        full_page = requests.get(weather, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "unit unit_temperature_c"})
        self.label.text = convert[0].text

    def click1(self, instance):
        dollar_rub = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&newwindow=1&sxsrf=APq-WBtX-jj9qj6wzbPnCM7S5JK9rH2bjA%3A1648062948319&ei=5HE7YvOPE5GfgQbgkYmgAQ&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+r&gs_lcp=Cgdnd3Mtd2l6EAEYADIHCCMQsQIQJzIHCCMQsQIQJzIECAAQQzIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIHCAAQyQMQCjIECAAQCjoHCCMQsAMQJzoHCAAQRxCwAzoKCAAQRxCwAxDJA0oECEEYAEoECEYYAFC1AViUAmD7BmgBcAF4AYABgwWIAY4GkgEHMC4xLjUtMZgBAKABAcgBCsABAQ&sclient=gws-wiz"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
        full_page = requests.get(dollar_rub, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde SwHCTb"})
        self.label.text = convert[0].text

    def click2(self, instance):
        euro_rub = "https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%BA%D1%83%D1%80%D1%81+%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+&aqs=chrome.0.0i20i263i512j0i512l5j69i57j69i61.6463j1j7&sourceid=chrome&ie=UTF-8"

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'}
        full_page = requests.get(euro_rub, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll("span", {"class": "DFlfde SwHCTb"})
        self.label.text = convert[0].text

    def build(self):
        but_together = BoxLayout()
        grid = GridLayout(cols=1)
        my_but = Button(text="Погода в Казани: ", font_size=24, background_color="cyan", on_press=self.click)
        think_of_name = Button(text="Курс доллара: ", font_size=24, background_color="green",
                               on_press=self.click1)
        euro = Button(text="Курс евро: ", font_size=24, background_color="cyan", on_press=self.click2)
        self.label = Label(text="___", font_size=100)
        but_together.add_widget(my_but)
        but_together.add_widget(think_of_name)
        but_together.add_widget(euro)
        grid.add_widget(but_together)
        grid.add_widget(self.label)
        return grid


if __name__ == "__main__":
    Application().run()
