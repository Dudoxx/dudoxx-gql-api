import requests

class OdooGraphQLClient:
    def __init__(self, url, db, username, password):
        self.url = url
        self.db = db
        self.username = username
        self.password = password
        self.session = requests.Session()
        self.authenticate()

    def authenticate(self):
        login_url = f"{self.url}/web/session/authenticate"
        headers = {'Content-Type': 'application/json'}
        payload = {
            "jsonrpc": "2.0",
            "params": {
                "db": self.db,
                "login": self.username,
                "password": self.password
            }
        }
        response = self.session.post(login_url, json=payload, headers=headers)
        response.raise_for_status()
        result = response.json().get('result')
        if not result or not result.get('uid'):
            raise Exception("Authentication failed")
        self.session_id = result['session_id']

    def execute_query(self, query):
        graphql_url = f"{self.url}/graphql"
        headers = {
            'Content-Type': 'application/json',
            'X-Openerp-Session-Id': self.session_id
        }
        response = self.session.post(graphql_url, json={'query': query}, headers=headers)
        response.raise_for_status()
        return response.json()

# Example usage
if __name__ == "__main__":
    client = OdooGraphQLClient(
        url="http://localhost:8069",
        db="dudoxx_backend3",
        username="admin",
        password="admin"
    )
    query = """
    {
      __schema {
        types {
          name
        }
      }
    }
    """
    result = client.execute_query(query)
    print(result)
