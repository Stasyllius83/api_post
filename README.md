Реализовано веб-приложение с API-интерфейсом и админ-панелью , в котором пользователи могут писать посты и комментировать их.
Структура проекта три модели пользователь, пост, комментарий. Для модели пользователя реализован валидатор для пароля (должен быть не менее 8 символов, должен включать цифры) и валидатор для почты (разрешены домены: mail.ru, yandex.ru). Для модели поста реализованы валидатор на проверку того, что автор поста достиг возраста 18 лет и что автор в заголовок не вписал запрещенные слова: ерунда, глупость, чепуха. В админ панель в объекте поста добавлена ссылка на автора и есть фильтр по дате создания поста. Права доступа заложены в проект.
