Бот для бесед Vk

'!чек' - проверка, что человек добавил в друзья всех с диалога. Вводится в диалог.
'!пост' - проверка по группам, что люди сделали посты.
'!кик' - удалить юзера с группы.
'!хелп' - не нуждается в представлении.
'!автопост' - включить\выключить выполнение команды !пост раз в час.

'!правила' - показать правила, которые админ назначил в группе. 
'!обновить' - назначить правила для группы.
'!макет' - задать макет для списка.
'!категория' - назначить категории для списка.
'!добавить' - добавить человека в список.
'!список' - вывести список.
'!убрать' - удалить человека из списка.

'!группы' - вывести группы, в которых будет производиться поиск по ключу.
'!+группа' - добавить группу в список. 
 '!-группа' - удалить группу из списка.
'!ключ' - задать ключ.

'!время' - задать время обнуления списка юзеров.
            
            
  Данные для конфига:
login: логин ВК (лучше задать через телефон, чтобы не было проблем с авторизацией)
password: пароль
token_for_bot: токен от группы сообщества. Должен иметь право на чтение сообщений
token_for_app: токен от приложения (используется для некоторых методов). Создать тут: https://vk.com/apps?act=manage. 
bot_id: id сообщества бота. 

TODO:
- Передать хранение данных с хранилища на базу данных (SQLite хотя бы)
- Добавить хранение всех бесед в базе
- Фиксы команд (при любом результате должен был ответ)
- Включить\Выключить показ правил и списка для новых пользователей.
- Добавить поддержку ссылок типа vk.com/durov
- Добавить отображение времени до чистки
- Сделать сохранение статистики для юзеров в базе данных.
- Добавить команду "!исключение" для юзеров.
- Сделать автокик в заданное время для людей, у которых 0 постов. 
- Сделать автоперемещение людей из одной категории в другую.
- Добавить функцию "!передатьпосты"
- Добавить функцию хранения никнейма
