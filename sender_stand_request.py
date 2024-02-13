import configuration
import requests
import data

#Función para crear un nuevo usuario
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, #URL completa con la ruta a la creación de cuenta
                         json=body,
                         headers=data.headers)

#Función para obtener el authToken del nuevo usuario
#--- CAMBIOS DEL FEEDBACK A MEJORAR ---
def create_kit_token():
    response = data.user_body.copy()
    response = post_new_user(data.user_body)
    data_response = response.json()
    return data_response["authToken"]

#Función para crear un nuevo kit
def post_new_client_kit(kit_body):
    token = create_kit_token()
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}"
    }
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=headers) #Header que contiene: Content-Type y Authorization