Blog on Django
=================================================

Описание
=================================================
Данный блог обладает возможностями:
 - Создание постов (для всех пользоваетелей)
- Просмотр всех постов (для всех пользователей)
- Комментирование постов (для всех авторизованных пользователей (обязательно указание своего E-mail адреса))
- Редактирование и удаление постов (Только для авторизованных пользователей и для созданных ими постов)
- Регистрация нового пользователя
- Осуществление входа и выхода из любого аккаунта
- Текстовый поиск по названиям постов (можно искать как по словам и целым заголовкам так и по частям слов)

Таким образом, данный блог позволяет каждому пользователю анонимно добавлять посты, которые будут доступны к просмотру абсолютно всем пользователям. Любой пользователь может комментировать любой(в том числе и свой пост). Комменты, также как и посты, не привязаны к пользователю. Функция редактирования поста и его удаления доступна лишь владельцу(автору данного поста). При удалении поста удаляется вся страница поста вместе со всеми комментариями. Суперьпользователь, как и обычный пользователь не имеет право изменять и удалять не свои посты. Каждый пост имеет заголовок текст, а также, при отображении на главной странице, отображается дата и время добавления данного поста.


Кратко о конструкции проекта:
====================================================
- Все html шаблоны - my-first-blog\blog\templates\blog
 Тесты - my-first-blog\blog\tests.py
- CSS фаил - my-first-blog\blog\static\css\css.py
- Библиотеки установленные в виртуальном окружении - my-first-blog\myvenv\Lib\site-packages


Пользователи:
====================================================
![Image alt](https://github.com/VsevolodS23/my-first-blog/blob/master/Users.png)

Имеется 4 пользователя. Пользователь с ником vsevolod является суперпользователем (создан через коммандную строку), остальные пользователи являются обычными пользователями (были созданы через форму регистрации в блоге). Для всех пользователей используется 1 пароль - pythonpython

Оформление
=================================================

При создании блога использовались различные html шаблоны и css фаил. Все шаблоны выдержаны в едином стиле, оновные шаблоны построены на основе файла base.html 

![Image alt](https://github.com/VsevolodS23/my-first-blog/blob/master/Main_page.png)
