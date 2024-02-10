import sender_stand_request
import data

#Función para modificar el parámetro name
def get_kit_body(name):
    current_name = data.kit_name.copy()
    current_name["name"] = name
    return current_name

#-----------------------------------------------------------------
#Función de prueba positiva
def positive_assert(kit_body):
    #Nuevo nombre del kit
    kit_name = get_kit_body(kit_body)

    #Respuesta de la solicitud de crear un nuevo kit ya con el Token generado del nuevo usuario
    kit_response = sender_stand_request.post_new_client_kit(kit_name)

    #Comprueba si el código es 201
    assert kit_response.status_code == 201, "El status code del nuevo kit no es 201"
    #Comprueba que el campo authToken está en la respuesta y no está vacío
    assert kit_response.json()['user']['authToken'] != "", "El campo authToken está vacío"
#-----------------------------------------------------------------

def negative_assert_code_400(kit_body):
    #Versión actualizada del campo name del kit nuevo
    kit_name = get_kit_body(kit_body)

    #Response de la solicitud al crear un nuevo kit
    response = sender_stand_request.post_new_client_kit(kit_name)

    #Comprueba si el status_code es 400
    assert response.status_code == 400, "El error obtenido es diferente a 400"
#------------------------------------------------------------------

# Test_1: El número permitido de caracteres es 1
def test_create_kit_1_character_in_name_get_success_response():
    positive_assert("a")
#---------------------------------------------------------------------

#Test_2: El número permitido de caracteres es 511
def test_create_kit_511_character_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
#--------------------------------------------------------------------

# Test_3: El número de caracteres es menor que la cantidad permitida (0)
def test_create_kit_0_character_in_name_get_error_response():
    negative_assert_code_400("")
#--------------------------------------------------------------------

# Test_4: El número de caracteres es mayor que la cantidad permitida (512)
def test_create_kit_512_character_in_name_get_success_response():
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
#--------------------------------------------------------------------

# Test_5: Se permiten caracteres especiales
def test_create_kit_special_characters_get_success_response():
    positive_assert( "№%@")
#-------------------------------------------------------------------

# Test_6: Se permiten espacios
def test_create_kit_with_spaces_get_success_response():
    positive_assert("A Aaa")
#------------------------------------------------------------------

# Test_7: Se permiten números
def test_create_kit_with_numbers_get_success_response():
    positive_assert("123")
#-----------------------------------------------------------------
# Función de prueba negativa para Test_8
def negative_assert_no_name(kit_body):
    #Guardamos la response en una variable
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400, "El código obtenido es diferente a 400"
#---------------------------------------------------------------

# Test_8: El parámetro name no se pasa en la solicitud {}
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_name.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)
#--------------------------------------------------------------

# Test_9: Se ha pasado un tipo de parámetro diferente (int)
def test_create_kit_name_is_int_get_error_response():
    negative_assert_code_400(123)
