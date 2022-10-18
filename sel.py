from selenium import webdriver
from selenium.webdriver.common.by import By

from quiz_nybi import quiz_1_api, quiz_2_api

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
main_driver = webdriver.Chrome(PATH)
main_driver.set_window_size(1000, 1000)


def quiz_1(driver):
    driver.get("https://www.nybi.org/subnet-1.php")
    answer_form = driver.find_element(by=By.ID, value='answer')

    network_id = answer_form.find_element(by=By.TAG_NAME, value='strong').text
    subnet_required = answer_form.find_element(by=By.CLASS_NAME, value='mb-3')\
        .find_element(by=By.TAG_NAME, value='strong').text

    result = quiz_1_api(network_id, subnet_required)

    driver.find_element(by=By.NAME, value='s1').send_keys(result[0])
    driver.find_element(by=By.NAME, value='n1').send_keys(result[1])
    driver.find_element(by=By.NAME, value='m1').send_keys(result[2])

    driver.find_element(by=By.NAME, value='bt1').click()


def quiz_2(driver):
    driver.get("https://www.nybi.org/subnet-2.php")

    full_ip = driver.find_element(by=By.XPATH, value='//*[@id="answer"]/div[1]/strong').text

    result = quiz_2_api(full_ip)

    driver.find_element(by=By.NAME, value='n2').send_keys(result[0])
    driver.find_element(by=By.NAME, value='b2').send_keys(result[1])
    driver.find_element(by=By.NAME, value='s2').send_keys(result[2])

    driver.find_element(by=By.NAME, value='bt1').click()


for _ in range(2):
    quiz_1(main_driver)
    quiz_2(main_driver)

main_driver.quit()
