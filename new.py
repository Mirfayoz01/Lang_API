from requests import get

url = 'https://langapi-sjvl.onrender.com/docs/'

response = get(url)

text = """
1: eng_uz
2: uz_eng
3. exit
"""

while True:
    print(text)
    choice = int(input('Enter your choice: '))
    if choice == 1:
        text = input('Enter text in UZBEK: ')
        en = f'https://langapi-sjvl.onrender.com/uz_en/{text}'
        response_en = get(en)
        print(response_en.json()['EN'])
    elif choice == 2:
        text = input('Enter text in ENG: ')
        uz = f'https://langapi-sjvl.onrender.com/en_uz/{text}'
        response_uz = get(uz)
        print(response_uz.json()['UZ'])

    elif choice == 3:
        break
    else:
        print('Invalid choice')
