from selenium import webdriver
from quiz_nybi import quiz_1_api, quiz_2_api

PATH = "C:\\Program Files (x86)\\chromedriver.exe"
main_driver = webdriver.Chrome(PATH)
main_driver.set_window_size(1000, 1000)


def quiz_1(driver):
    driver.get("https://www.nybi.org/subnet-1.php")
    answer_form = driver.find_element_by_id('answer')

    network_id = answer_form.find_element_by_tag_name('strong').text
    subnet_required = answer_form.find_element_by_class_name('mb-3').find_element_by_tag_name('strong').text

    result = quiz_1_api(network_id, subnet_required)

    driver.find_element_by_name('s1').send_keys(result[0])
    driver.find_element_by_name('n1').send_keys(result[1])
    driver.find_element_by_name('m1').send_keys(result[2])

    driver.find_element_by_name('bt1').click()


def quiz_2(driver):
    driver.get("https://www.nybi.org/subnet-2.php")

    full_ip = driver.find_element_by_xpath('//*[@id="answer"]/div[1]/strong').text

    result = quiz_2_api(full_ip)

    driver.find_element_by_name('n2').send_keys(result[0])
    driver.find_element_by_name('b2').send_keys(result[1])
    driver.find_element_by_name('s2').send_keys(result[2])

    driver.find_element_by_name('bt1').click()


for _ in range(2):
    quiz_1(main_driver)
    quiz_2(main_driver)

main_driver.quit()
