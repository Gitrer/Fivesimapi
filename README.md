# fivesimapi
Упрощенное взаимодействие с API веб-сайта 5sim.biz

# Использование
Апи ключ находится тут - https://5sim.biz/settings/security <br>
Ответы во всех методах приходят в json формате


```python
Импортируем библиотеку
from fivesimapi import *

Объявляем основной класс
api = fivesim(api='апи ключ с личного кабинета')

# Выводит статистику пользователя
print(api.get_profile())

# Выводит историю заказов
print(api.order_history(category='telegram'))

# Выводит историю платежей
print(api.payment_history())

# Выводит список установленых максимальных цен
print(api.max_prices())

# Установить или обновить лимит максимальной цены
print(api.set_limit(product_name='telegram', price='123'))

# Удалить лимит максимальной цены
print(api.delete_limit(product_name='telegram'))

# Вывести список товаров
print(api.product_request(country='indonesia', operator='any'))

# Вывести список цен
print(api.request_for_prices())

# Вывести список цен по конкретной стране
print(api.prices_by_country(country='indonesia'))

# Вывести список цен по конкретному товару
print(api.prices_by_country(product='telegram'))

# Вывести список цен по конкретному товару и по конкретной стране
print(api.prices_by_country_and_product(country='indonesia' ,product='telegram'))

# Заказ номера
print(api.get_number(country='indonesia', operator='any', product='telegram'))

# Аренда номера
print(api.rent_phone(country='indonesia', operator='any', product='telegram'))

# Повторный заказ номера
print(api.rebuy_phone(number='7123456789', product='telegram'))

# Получить смс
print(api.get_sms(id='123456'))

# Завершить заказ
print(api.complete_order(id='123456'))
```

# Разработчик
Разработчик - Gitrer

Telegram - @devilgrammm
