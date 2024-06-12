def render_list_reservas(reservas):
    return [
        {
            "id":reserva.id,
            "user_id":reserva.user_id,
            "restaurante_id":reserva.restaurante_id,
            "num_guests":reserva.num_guests,
            "special_requests":reserva.special_requests,
            "status":reserva.status
        }
        for reserva in reservas
    ]

def render_detail_reserva(reserva):
    return {
        "id":reserva.id,
        "user_id":reserva.user_id,
        "restaurante_id":reserva.restaurante_id,
        "num_guests":reserva.num_guests,
        "special_requests":reserva.special_requests,
        "status":reserva.status
    }