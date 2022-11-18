import qrcode

url = "https://google.com"  # Задаём ссылку, куда будет вести QR-код
filename = "site.png"  # Имя нового файла, куда сохранить QR-код
img = qrcode.make(url)  # Создаем QR-код с помощью библиотеки
img.save(filename)  # Сохраняем картинку кода
