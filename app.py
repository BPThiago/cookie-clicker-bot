from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import keyboard

class CookieClicker:
    def __init__(self) -> None:
        url = "https://orteil.dashnet.org/cookieclicker/"
        self.driver = webdriver.Firefox()
        self.driver.get(url)
        sleep(5)
    

    def select_lang(self, lang: str):
        if lang not in {"EN", "FR", "DE", "NL", "CS", "PL", "IT", "ES", "PT-BR", "JA", "ZH-CN", "KO", "RU"}:
            lang = "EN"
        self.driver.find_element(By.ID, f"langSelect-{lang}").click()
        sleep(5)


    def click_cookie(self, qtd: int): 
        cookie = self.driver.find_element(By.ID, "bigCookie")
        for _ in range(qtd):
            cookie.click()


    def buy_items(self):
        try:
            items = self.driver.find_elements(By.CLASS_NAME, "enabled")
            for i in reversed(items):
                i.click()
        except:
            pass  # There is no items to buy

    
    def exit_traffic_advertisement(self):
        try:
            self.driver.find_element(By.XPATH, "/html/body/div[1]/div/a[1]").click()
        except:
            pass
    

    def clean_achievement_list(self):
        try:
            while True:
                self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div[9]/div[1]/div[1]").click()
        except:
            pass  # There is no achievement to clean

    
    def switch_menu(self):
        self.driver.find_element(By.ID, "prefsButton").click()


    def load_state(self):
        try:
            self.clean_achievement_list()
            self.switch_menu()
            self.driver.find_element(By.XPATH, '//*[@id="menu"]/div[3]/div/div[5]/a[2]').click()
            self.switch_menu()
        except:
            pass


    def save_state(self):
        try:
            self.clean_achievement_list()
            self.switch_menu()
            self.driver.find_element(By.XPATH, '//*[@id="menu"]/div[3]/div/div[5]/a[1]').click()
            self.switch_menu()
        except:
            pass


    def exit(self, save: bool):
        if save:
            self.save_state()
            sleep(2)
        self.driver.quit()


if __name__ == "__main__":
    web = CookieClicker()
    web.exit_traffic_advertisement()
    web.select_lang("PT-BR")
    while not keyboard.is_pressed("p"):
        if keyboard.is_pressed("u"):
            web.clean_achievement_list()
        elif keyboard.is_pressed("o"):
            web.save_state()
        elif keyboard.is_pressed("i"):
            web.load_state()
        web.click_cookie(5)
        web.buy_items()
    web.exit(True)
