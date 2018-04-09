import re

def open_file():
    with open('finland_html.html', encoding="utf-8") as f:
        text = f.read()
    return text


def searching(text):
    res_1 = re.sub('Финляндия','Малайзия', text)
    res_2 = re.sub('Финляндии','Малайзии', res_1)
    res_3 = re.sub('Финляндию','Малайзию', res_2)
    res_4 = re.sub('Финляндией','Малайзией', res_3)
    res_5 = re.sub('ФИНЛЯНДИИ','МАЛАЙЗИИ', res_4)
    res_6 = re.sub('Финля́ндия', 'Мала́йзия', res_5)
    return res_6

def writing(res_6):
    with open('Malaysia.html', "w", encoding="utf-8") as f:
        f.write(res_6)


def main():
    file = open_file()
    search = searching(file)
    write = writing(search)


if __name__=='__main__':
    main()
