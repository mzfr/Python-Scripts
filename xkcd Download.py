from bs4 import BeautifulSoup
import requests

fail_counter = 0
image_count = 1
while fail_counter == 0:
    page = requests.get("http://xkcd.com/" + str(image_count))
    soup = BeautifulSoup(page.content, 'html.parser')

    div = soup.find_all('div', {'id': 'comic'})

    img = div[0].find('img')
    src = img.__getitem__("src")[2:]

    response = requests.get("http://" + src)

    # For Downloading the image
    if response.status_code == 200:
        with open("images/" + str(image_count) + ".jpg", 'wb') as image:
            image.write(response.content)
            print ("image saved")
            image_count += 1
    else:
        print ("failed")
        fail_counter += 1
