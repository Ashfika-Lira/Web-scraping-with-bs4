import requests
from bs4 import BeautifulSoup

with open('home.html', 'r') as f:
    content = f.read()
    # print(content)

    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())

    # tags = soup.find('h5')
    course_tags = soup.find_all('h5')
    # print(tags)

    # for course in course_tags:
        # print(course.text)

    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        # print(course)
        # print(course.h5)
        course_name = course.h5.text
        # course_price = course.a.text
        course_price = course.a.text.split()[-1]

        # print(course_name)
        # print(course_price)
        print(f"{course_name} costs {course_price}")



