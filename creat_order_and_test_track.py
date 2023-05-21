import sender_stand_request
import data

# Функция проверки заказа по его треку
def test_cheking_order_by_track():
    get_order = sender_stand_request.post_order(data.order_body)
    #проверка создание заказа
    assert get_order.status_code == 201

    create_order_response_json = get_order.json()
    track = create_order_response_json['track']
    #проверка наличие трека
    assert track >= 0

    get_track_response = sender_stand_request.get_order_by_track(track)
    #проверка наличие заказа по треку
    assert get_track_response.status_code == 200
