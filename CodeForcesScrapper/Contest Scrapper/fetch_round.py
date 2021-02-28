from selenium import webdriver
import os

num = input("Enter Contest Number: ")
link = "https://codeforces.com/contest/" + num

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(link)

path = os.getcwd()
path = os.path.join(path,num)
if not os.path.exists(path):
    os.mkdir(path)
os.chdir(path)           # inside contest folder

submissions = driver.find_elements_by_class_name("act")
x = len(submissions)

for j in range(x):
    problems_codes = driver.find_elements_by_tag_name("td")
    l = []
    text = []
    i = 0
    while i < len(problems_codes) - 2:
        l.append(problems_codes[i + 1])
        text.append(problems_codes[i + 1].text)
        i += 4
    list_ofProblems = l[:x]
    list_ofProblems[j].click()
    fp = os.path.join(path, text[j])
    if not os.path.exists(fp):
        os.mkdir(fp)

    img = os.path.join(fp,'problem.png')
    driver.save_screenshot(img)

    input = driver.find_elements_by_class_name("input")
    for i in range(len(input)):
        inp = input[i].text[11:]
        name = "input" + str(i + 1) + '.txt'
        filename = os.path.join(fp, name)
        with open(filename , 'w') as f:
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

