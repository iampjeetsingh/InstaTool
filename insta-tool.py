from selenium import webdriver
from selenium.common import exceptions
from time import sleep

driver = webdriver.Chrome(executable_path="./chromedriver")
driver.get('https://instagram.com')
driver.maximize_window()
sleep(3)
while True:
    sleep(5)
    username = None
    try:
        username = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')
    except:
        print('Not Logged in yet')
    else:
        print("Logged In")
        break
sleep(5)

def click(xpath):
    c = 0
    while c < 15:
        sleep(1)
        try:
            element = driver.find_element_by_xpath(xpath)
            element.click()
        except exceptions.NoSuchElementException:
            print("Waiting for element...")
        else:
            return
        c += 1
    assert "Element not found"

followers = []
following = []
try:
    # Click Profile Icon
    click('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a')
    sleep(5)
    # Click Followers Icon
    click('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
    sleep(5)
    # Get Followers
    totalfollowers = int((driver.find_elements_by_class_name("g47SY")[1]).text)
    script = 'var scrollView = document.querySelector("body > div.RnEpo.Yx5HN > div > div.isgrP");scrollView.scrollBy(0,100000);'
    while len(driver.find_elements_by_class_name('FPmhX')) != totalfollowers:
        sleep(3)
        driver.execute_script(script)
    lis = driver.find_elements_by_class_name('FPmhX')
    for elem in lis:
        followers.append(elem.text)
    sleep(5)
    # Click Cross Button
    click('/html/body/div[4]/div/div[1]/div/div[2]/button')
    sleep(5)
    # Click Following Icon
    click('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a')
    sleep(3)
    # Get Following
    totalfollowing = int((driver.find_elements_by_class_name("g47SY")[2]).text)
    script = 'var scrollView = document.querySelector("body > div.RnEpo.Yx5HN > div > div.isgrP");scrollView.scrollBy(0,100000);'
    while len(driver.find_elements_by_class_name('FPmhX')) != totalfollowing:
        sleep(3)
        driver.execute_script(script)
    lis = driver.find_elements_by_class_name('FPmhX')
    for elem in lis:
        following.append(elem.text)
    # Click Cross Button
    click('/html/body/div[4]/div/div[1]/div/div[2]/button')
    sleep(5)
    # Click Settings Button
    click('//*[@id="react-root"]/section/main/div/header/section/div[1]/div/button')
    sleep(5)
    # Click Logout Button
    click('/html/body/div[4]/div/div/div/button[9]')
except exceptions.NoSuchElementException:
    print('Element not found')
else:
    sleep(5)
    driver.quit()
print()
print()
print("You have "+str(len(followers))+" Followers")
print("You have "+str(len(following))+" Following")
print()
moles = []
for person in following:
    if person not in followers:
        moles.append(person)
print("You have "+str(len(moles))+" moles")
for person in moles:
    print(person)
