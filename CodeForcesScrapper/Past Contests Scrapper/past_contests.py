from selenium import webdriver
import os

number_str = input("Please tell the Number of past contests: ")
number_int = int(number_str)

PATH = "chromedriver.exe"
driver = webdriver.Chrome(PATH)
link = "https://codeforces.com/contests"
driver.get(link)

path = os.getcwd()

for a in range(number_int):
    contest = driver.find_elements_by_link_text("Enter »")[:number_int]
    contest[a].click()
    number = 'Most Recent Contest ' + str(a + 1)
    path1 = os.path.join(path, number)
    if not os.path.exists(path1):
        os.mkdir(path1)
    os.chdir(path1)
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
        fp = os.path.join(path1, text[j])
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
    driver.back()

driver.close()