from browsermobproxy import Server
from pprint import pprint
server = Server("/Users/minhtuevo/browsermob-proxy/bin/browsermob-proxy")
server.start()
proxy = server.create_proxy()
proxy.blacklist("http://www\.bing\.com/", 404)

from selenium import webdriver
profile  = webdriver.FirefoxProfile()
profile.set_proxy(proxy.selenium_proxy())
driver = webdriver.Firefox(firefox_profile=profile)

driver.get("http://www.bing.com")

proxy.stop()
driver.quit()
