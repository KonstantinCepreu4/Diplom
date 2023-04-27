import sender_file_requests


# Функция для позитивных проверок
def positive_assert():
    # В переменную сохраняется результат запроса
    order_response = sender_file_requests.get_order_by_track()
    # Проверка, что код ответа 200
    assert order_response.status_code == 200
# Тест кода ответа на запрос получения заказа по его номеру.
def test_get_order_response():
    positive_assert()