from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def get_screenshots(device):
    
    width = int(device['w']/device['h'] * 760)
    height = 760
    mobile_emulation = { "deviceMetrics": { "width": width, "height": height}}
    
    options = Options()
    options.add_argument('headless')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    
    with webdriver.Chrome(options = options) as browser:
        browser.get("https://covid-19.ontario.ca/school-screening/")
        time.sleep(0.4)
            
        click_button(browser, "Start school screening")
        
        click_button(browser, "Yes")
        click_button(browser, "No")
        
        click_button(browser, "Continue")
        
        for i in range(3):
            click_button(browser, "No")
            

        browser.find_element_by_tag_name('body').screenshot(f"screenshots/{device['name']}.png")


def click_button(browser, text, btType="button"):
    element = browser.find_element(By.XPATH, f"//*[ text() = '{text}' and @type='{btType}' ]")
    browser.execute_script('arguments[0].click();', element)
    time.sleep(0.4)
    
def fill_form(browser, id, inpt):
    element = browser.find_element(By.XPATH, f"//*[ @name='{id}' ]")
    element.send_keys(inpt)
    time.sleep(0.4)

def gen_click(browser, id):
    element = browser.find_element(By.XPATH, f"//*[@id='{id}']")
    browser.execute_script('arguments[0].click();', element)
    print("clicked")
    time.sleep(0.4)