from selenium import webdriver

class SeleniumTest(object):

    def __init__(self, driver):
        self.driver = driver


    def test(self):
        self.google_test()

    def google_test(self):
        self.driver.get("https://www.google.com")
        self.driver.find_element_by_xpath("//input[@name='q']").clear()
        self.driver.find_element_by_xpath("//input[@name='q']").send_keys("cats")
        self.driver.find_element_by_xpath("//input[@name='btnK']").click()

def main():
    driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    t = SeleniumTest(driver)
    t.test()

if __name__ == "__main__":
    main()