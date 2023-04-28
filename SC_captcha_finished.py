from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver.common.by import By
fox = webdriver.Chrome()
fox.get('https://stdn.iau.ir/Student/Pages/acmstd/loginPage.jsp')

# now that we have the preliminary stuff out of the way time to get that image :D
element = fox.find_element(By.ID,"captchaimg") # find part of the page you want image of
# element=browser.find_element(By.ID,"searchinput")
# location = element.location
# print(location)
# size = element.size
# print(size)
png = fox.get_screenshot_as_png() # saves screenshot of entire page
fox.quit()

im = Image.open(BytesIO(png)) # uses PIL library to open image in memory

left =650
top = 515
right = 870
bottom = 635


im = im.crop((left, top, right, bottom)) # defines crop points
im.save('D:\captchascreenshot.png') # saves new cropped image