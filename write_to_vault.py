from vault import client


def write_secret(secret_path, secret_key, secret_value):
    """writes a new secret to path

    Args:
        secret_key (str): vault secret key
        secret_value (str): vault secret value
        secret_path (str): path to vault
    """
    create_response = client.secrets.kv.v2.create_or_update_secret(
        path=secret_path, secret={secret_key: secret_value})

    print(create_response)
    return create_response


# write_secret(new/ahmed, username ,ahmed)
# write_secret(new/ahmed, password ,password)
