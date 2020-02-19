# ya_translate
Очень простой скрипт для перевода слов с русского языка на английский.
Для запуска программы необходимо получить API ключ на yandex.ru.
Для этого заходим на страницу для разработчиков (заранее авторизовавшись в системе): 
- Нажимаем «Get a free API key». 
- Нас переводят на страницу где мы нажимаем на кнопку «Create new key» и получаем новый ключ.

##Пример использования:
`Для начала работы введите ваш API ключ.: "ЗДЕСЬ ВАШ КЛЮЧ"`
`Введите слово для перевода или введите "stop" для остановки и получения результата: луна`
`Введите слово для перевода или введите "stop" для остановки и получения результата: земля`
`Введите слово для перевода или введите "stop" для остановки и получения результата: stop`

###Результат работы:
`the moon`
`earth`

Скрипт не чувствителен к регистру.

#### Translate
Для программы создан простенький класс который хранит список введенных слов и делает перевод каждого слова.

##### ya_test_translate
Автоматический тест для проверки корректности работы класса "Translate" и работы программы.
Для запуска автотеста необходимо так же ввести ключ API.
