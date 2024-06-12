def render_list_restaurantes(resetaurantes):
    return [
        {
            "id":restaurante.id,
            "name":restaurante.name,
            "address":restaurante.address,
            "city":restaurante.city,
            "phone":restaurante.phone,
            "description":restaurante.description,
            "rating":restaurante.rating
        }
        for restaurante in resetaurantes
    ]

def render_detail_restaurante(restaurante):
    return {
        "id":restaurante.id,
        "name":restaurante.name,
        "address":restaurante.address,
        "city":restaurante.city,
        "phone":restaurante.phone,
        "description":restaurante.description,
        "rating":restaurante.rating
    }