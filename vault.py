import hvac


def init_server():
    """
    Authenticates to server
    """
    client = hvac.Client(url='http://localhost:8200')
    print(f" Is client authenticated: {client.is_authenticated()}")

    return client


client = init_server()
