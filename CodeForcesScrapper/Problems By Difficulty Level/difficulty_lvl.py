from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

min = input('Minimum Difficulty: ')
max = input('Maximum Difficulty: ')
print('Please Enter a reasonable no. of problems (below 45)')
number = input('Enter the number of problems: ')
x = int(number)
difficulty = min + '-' + max + number + 'Problems'

link = "https://codeforces.com/problemset?tags="+min + '-' + max

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(link)

# create master folder
path = os.getcwd()
path = os.path.join(path, difficulty)
if not os.path.exists(path):
    os.mkdir(path)
os.chdir(path)  # inside problems folder


# main process copied from contest scrapper code with minor modifications
# site structure remains same so there is not much issue
for j in range(x):
    problems_codes = driver.find_elements_by_tag_name("td")
    l = []
    text = []
    i = 0
    while i < len(problems_codes) - 2:
        l.append(problems_codes[i])
        text.append(problems_codes[i].text)
        i += 5
    list_ofProblems = l[:x]
    list_ofProblems[j].click()
    fp = os.path.join(path, text[j])
    if not os.path.exists(fp):
        os.mkdir(fp)

    img = os.path.join(fp, 'problem.png')
    driver.save_screenshot(img)

    input = driver.find_elements_by_class_name("input")
    for i in range(len(input)):
        inp = input[i].text[11:]
        name = "input" + str(i + 1) + '.txt'
        filename = os.path.join(fp, name)
        with open(filename, 'w') as f:
            f.write(inp)

    output = driver.find_elements_by_class_name("output")
    for i in range(len(output)):
        out = output[i].text[12:]
        name = "output" + str(i + 1) + '.txt'
        filename = os.path.join(fp, name)
        with open(filename, 'w') as f:
            f.write(out)

    driver.back()

driver.close()

