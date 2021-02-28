from selenium import webdriver
import os

number_str = input("Please tell the Number of past contests: ")
number_int = int(number_str)

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)

link = "https://codeforces.com/contests"
driver.get(link)

