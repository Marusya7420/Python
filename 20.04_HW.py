import json

with open("orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)

# 1. Какой номер самого дорогого заказа за июль
max_price = 0
max_order = ''
# цикл по заказам
for order_num, orders_data in orders.items():
    # получаем стоимость заказа
    price = orders_data['price']
    # если стоимость больше максимальной - запоминаем номер и стоимость заказа
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'1. Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')

# 2. Какой номер заказа с самым большим количеством товаров
max_quantity = 0
for order_num, orders_data in orders.items():
    # получить количество товаров
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        m_order = order_num
        max_quantity = quantity
print(f'2. Номер заказа с самым большим количестовм товаров: {m_order}, количество товаров: {max_quantity}')

# 3. В какой день в июле было сделано больше всего заказов
def find_big_day(orders):
    big_day_orders = {}
    for order_num, orders_data in orders.items():
        data = orders_data['date']
        if data in orders_data:
            big_day_orders[data] += 1
        else:
            big_day_orders[data] = 1

    big_day = max(big_day_orders, key = big_day_orders.get)
    return big_day
big_day = find_big_day(orders)
print(f"3. В этот день {big_day} было сделано больше всего заказов")

# 4. Какой пользователь сделал самое большое количество заказов за июль
add_order ={}
for order_num, orders_data in orders.items():
    users_id = orders_data['user_id']
    add_order[order_num] = users_id
# print(add_order) # проверяем наличие созданного словаря
def count_list_id(list_users_id):
    count_users_id = {}
    for item in list_users_id:
        count_users_id[item] = count_users_id.get(item, 0) + 1
    return count_users_id
list_users_id = list(add_order.values())
count_list_id(list_users_id)
# print(count_list_id(list_users_id)) # проверяем работу функции, есть ли словарь с посчитанными вхождениями
max_users_id = count_list_id(list_users_id)
max_user_result = max(max_users_id, key = max_users_id.get)
print(f'4. Пользователь с id_номером {max_user_result} сделал самое большое количество заказов')

# 5. У какого пользователя самая большая суммарная стоимость заказов за июль
big_sum_price = {}
for order_num, orders_data in orders.items():
    cost = orders_data['quantity'] * orders_data['price']
    users_id = orders_data['user_id']
    big_sum_price[users_id] = cost
# print(big_sum_price)
# Ищем пользователя с максимальной суммарной стоимостью
if users_id in big_sum_price:
    big_sum_price[users_id] = 0
    big_sum_price[users_id] += cost
max_user = max(big_sum_price, key = big_sum_price.get)
print(f'5. Пользователь с id_номером {max_user} имеет самую большую суммарную стоимость заказа')

# 6. Какая средняя стоимость заказа была в июле
order_num_price = {}
for order_num, orders_data in orders.items():
    price = orders_data['price']
    order_num_price[order_num] = price
# print(order_num_price)
s_price = sum(order_num_price.values())
# print(s_price)
count_order_num = len(orders)
# print(count_order_num)
average_amount = s_price / count_order_num
print(f'6. Средняя стоимость заказа в июле была: {average_amount}')

# 7. Какая средняя стоимость товаров в июле
quantity_price = {}
for order_num, orders_data in orders.items():
    price = orders_data['price']
    quantity = orders_data['quantity']
    quantity_price[quantity] = price
# print(quantity_price) # проверяем наличие словаря quantity_price
count_quantity = sum(quantity_price.keys())
count_price = sum(quantity_price.values())
average_price = count_price / count_quantity
print(f'7. Средняя стоимость товара в июле: {average_price:.3f}')


