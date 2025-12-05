# def function_name (parameters):
#     code
#     logic
#     return python_data_type


message = "hi"


def sign_up(username, firstname, lastname, password):
    message = "Username should bot be less than 6 characters"

    if len(username) < 6:
        return message

    message = "Registration Successful"

    return message


print(message)

# calling the function
results = print(sign_up("alxawdwd", "Jesse", "Appiah", "ajstar"))


print(results)
