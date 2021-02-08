# email_thread

#### Реализована отправка писем через smtp сервер mail.ru

### Как развернуть на локальном устройстве

* склонировать этот репозиторий ```https://github.com/YuriyShashurin/email_thread.git```
* перейти в папку с ним ```cd email_thread```
* создать виртуальное окружение ```python -m venv venv```
* активировать его ```venv/bin/activate```
* установить зависимости - ```pip install -r requirements.txt```
* Запустить команду  ```python manage.py makemigrations```
* Установить емейл, с которого будет отправляться письма в файле settings.py в строке   ```EMAIL_HOST_USER = "Enter_Your_mail.ru_mail"```
* Установить пароль для этой почты в файле settings.py в строке   ```EMAIL_HOST_PASSWORD = 'Enter_Your_mail.ru_password'```
* Запустить команду  ```python manage.py migrate```
* Запустить приложение  ```python manage.py runserver```
* Ввести в адресной строке адрес  ```http://127.0.0.1:8000/```
 
 
 ##### Страницы на локальном устройстве:
* http://127.0.0.1:8000/ - Создание письма, установка таймера отправки
* http://127.0.0.1:8000/mails - Список последних 10 писем со статусом отправки


### Проект на Хероку
https://hidden-dusk-72655.herokuapp.com/

Почта, с которой будут отправляться письма, установлена по-умолчанию - test_sendmail@list.ru
* https://hidden-dusk-72655.herokuapp.com/ - Создание письма, установка таймера отправки
* https://hidden-dusk-72655.herokuapp.com/mails - Список последних 10 писем со статусом отправки
