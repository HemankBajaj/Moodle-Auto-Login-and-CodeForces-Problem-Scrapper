from selenium import webdriver
from selenium.webdriver.common.keys import Keys

kerberos_id = input("Please enter yur Kerberos ID ")
password = input("Please enter your Password ")

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://moodle.iitd.ac.in/login/index.php")

username = driver.find_element_by_id("username")
username.send_keys(kerberos_id)

password_final = driver.find_element_by_id("password")
password_final.send_keys(password)

text = driver.find_element_by_id("login").text
new = text[51:]
i = 0
k = 0
s = ""
while k == 0:
    if new[i] == "=":
        k += 1
    else:
        s += new[i]
    i += 1
final_ans = 0
if s[0] == 'a':
    ans = s[4:]
    t = ans.index('+')
    a = int(ans[:t])
    b = int(ans[t+1:])
    final_ans = str(a+b)
if s[0] == 's':
    ans = s[9:]
    t = ans.index('-')
    a = int(ans[:t])
    b = int(ans[t + 1:])
    final_ans = str(a - b)
if s[0] == 'e' and s[6] == 'f':
    ans = s[18:]
    t = ans.index(',')
    final_ans = ans[:t]
if s[0] == 'e' and s[6] == 's':
    ans = s[19:]
    t = ans.index(',')
    final_ans = ans[t+1:]

captcha = driver.find_element_by_id("valuepkg3")
captcha.send_keys(Keys.BACK_SPACE)
captcha.send_keys(final_ans)
captcha.send_keys(Keys.RETURN)