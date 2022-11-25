import hvac


class Vault():
    """
    Module responsible for reading from vault
    """

    def __init__(self):
        client = self._init_server()

    def _init_server(self):
        """
        Authenticates to server
        """
        client = hvac.Client(url='http://localhost:8200')
        print(f" Is client authenticated: {client.is_authenticated()}")

        return client

    def write_secret(self, secret_path, secret_key, secret_value):
        """writes a new secret to path

        Args:
            secret_key (str): vault secret key
            secret_value (str): vault secret value
            secret_path (str): path to vault
        """
        create_response = self.client.secrets.kv.v2.create_or_update_secret(
            path=secret_path, secret={secret_key: secret_value})

        print(create_response)
        return create_response

    def _read_path_secrets(self, path):
        """reads all secrets in a path

        Args:
            path (str): path in vault

        Returns:
            dict: all secrets in the path returned
        """
        read_response = self.client.secrets.kv.v2.read_secret_version(
            path=path)
        # secrets with all metadata
        print(read_response)

        """
        # example response
            {
        "request_id":"9c2fb05c-f78a-837a-a6d0-6b7a59b4d45d",
        "lease_id":"",
        "renewable":false,
        "lease_duration":0,
        "data":{
        "data":{
            "username":"ahmed"
            "password" : "password"
        },
        "metadata":{
            "created_time":"2022-11-22T07:34:58.187639Z",
            "custom_metadata":"None",
            "deletion_time":"",
            "destroyed":false,
            "version":1
        }
            },
            "wrap_info":"None",
            "warnings":"None",
            "auth":"None"
            }
        """
        secrets = read_response['data']['data']

        return secrets

        # read_secret(new/ahmed)

    def read_a_certain_secret(self, key):
        """
        reads a single secret from vault

        """
        try:
            return self._read_path_secrets()[key]
        except ValueError:
            print("Can't find value")
        except Exception as e:
            print(f"error ouccured ({e})")
