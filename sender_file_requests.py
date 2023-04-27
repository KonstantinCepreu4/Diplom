import requests
import configuration
import data



# Создание заказа
def post_greate_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.GREATE_ORDERS,
                         json=body,
                         headers=data.headers)
# Вызов функции создания заказа
response = post_greate_order(data.order_body)

# Получаем номер заказа
def take_track():
    # Переменной присваивается вызов функции
    order_track = post_greate_order(data.order_body)
    # В переменную сохраняется тело ответа.
    response_json = order_track.json()
    # Сохраняем в переменную параметр "track"
    track = response_json["track"]
    # Возвращаем переменную.
    return track

# Функция отправляет запрос на получение заказа по номеру
def get_order_by_track():
    param_t = take_track()
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_TRACK,
                        params={"t":param_t})

response = get_order_by_track()
