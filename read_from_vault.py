from vault import client


def read_path_secrets(path):
    """reads all secrets in a path

    Args:
        path (str): path in vault

    Returns:
        dict: all secrets in the path returned
    """
    read_response = client.secrets.kv.v2.read_secret_version(path=path)
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
         "created_time":"2021-12-02T07:34:58.187639Z",
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

def read_a_certain_secret(key):
    """
    reads a single secret from vault

    """
    return read_path_secrets()[key]
