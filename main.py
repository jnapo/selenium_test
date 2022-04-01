import time
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import title_is
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())


def test_input():
    driver.find_element(By.CSS_SELECTOR, "[aria-label='Pokaż/Ukryj Pole Wyszukiwania']").click()
    print("Wyszukuje fraze \'Technik programista\'")
    driver.find_element(By.CSS_SELECTOR, "[aria-label='Wpisz szukaną frazę']").send_keys(
        'technik programista' + Keys.ENTER)
    driver.implicitly_wait(5)
    print("Wchodzę w szczegóły")
    driver.find_element(By.LINK_TEXT, "Technik programista").click()
    print("Zapisuje screena")
    driver.save_screenshot("programista_szczegoly.png")
    driver.find_element(By.CLASS_NAME, "custom-logo").click()


def test_page_responsiveness():
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    print("Robie screena dolnej czesci strony")
    driver.save_screenshot("dol-strony.png")
    driver.execute_script("window.scrollTo(document.body.scrollHeight,0)")
    print("Sprawdzam responsywność strony")
    driver.set_window_size(400, 1800)
    driver.save_screenshot("waska-strona.png")
    driver.maximize_window()
    driver.save_screenshot("max-strona.png")


def test_social_links():
    parent = driver.window_handles[0]
    print("Sprawdzam link do facebooka")
    driver.find_element(By.CLASS_NAME, "facebook").click()
    time.sleep(1)
    child = driver.window_handles[1]
    driver.switch_to.window(child)
    driver.find_element(By.CSS_SELECTOR,
                        "[aria-label='Zezwól na korzystanie z niezbędnych i opcjonalnych plików cookie']").click()
    time.sleep(1)
    driver.save_screenshot("facebook.png")
    driver.close()
    driver.switch_to.window(parent)
    print("Sprawdzam link do instagrama")
    driver.find_element(By.CLASS_NAME, "instagram").click()
    time.sleep(1)
    child = driver.window_handles[1]
    driver.switch_to.window(child)
    driver.find_element(By.CLASS_NAME, "aOOlW").click()
    time.sleep(1)
    driver.save_screenshot("instagram.png")
    driver.close()
    driver.switch_to.window(parent)
    print("Sprawdzam link do twittera")
    driver.find_element(By.CLASS_NAME, "twitter").click()
    time.sleep(1)
    child = driver.window_handles[1]
    driver.switch_to.window(child)
    driver.find_element(By.CLASS_NAME, "css-901oao").click()
    time.sleep(1)
    driver.save_screenshot("twitter.png")
    driver.close()
    driver.switch_to.window(parent)
    print("Sprawdzam link do youtube")
    driver.find_element(By.CLASS_NAME, "youtube").click()
    time.sleep(1)
    child = driver.window_handles[1]
    driver.switch_to.window(child)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    driver.find_element(By.XPATH,
                        "//*[@id='yDmH0d']/c-wiz/div/div/div/div[2]/div[1]/div[4]/form/div/div/button/span").click()
    time.sleep(1)
    driver.save_screenshot("youtube.png")
    driver.close()
    driver.switch_to.window(parent)


def test_pagination():
    for i in range(2, 81):
        driver.find_element(By.LINK_TEXT, f"{i}").click()
        time.sleep(0.25)
    driver.find_element(By.CLASS_NAME, "custom-logo").click()



print("Otwieram stronę")
driver.get(url='https://www.zsi.kielce.pl')
print("Strona otwarta")
print("Rozpoczynam testy")

print("Test input")
test_input()
print("Test zakończony")
print("-----------------------------------------------------------")

print("Test responsywności strony")
test_page_responsiveness()
print("Test zakończony")
print("-----------------------------------------------------------")

print("Test social linków")
test_social_links()
print("Test zakończony")
print("-----------------------------------------------------------")

print("Czy chcesz wykonać test paginacji strony - czas trwania około 30 sekund")
odp = input("[y/n]")
if odp == "y":
    test_pagination()
