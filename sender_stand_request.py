import configuration
import requests
import data

# Функция создания заказа
def post_order(body):
    return requests.post(f'{configuration.URL_SERVICE}{configuration.POST_ORDERS}', json=body, headers=data.headers)

# Функция получения заказа по его номеру
def get_order_by_track(track_id):
    request_path = f'{configuration.URL_SERVICE}{configuration.GET_ORDERS}'
    return requests.get(request_path,
                        params={'t': track_id},
                        headers=data.headers
                        )
