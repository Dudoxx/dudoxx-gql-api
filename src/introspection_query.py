from graphql_client import OdooGraphQLClient

def perform_introspection(client):
    introspection_query = """
    {
      __schema {
        types {
          name
          fields {
            name
            type {
              name
            }
          }
        }
      }
    }
    """
    result = client.execute_query(introspection_query)
    return result

if __name__ == "__main__":
    client = OdooGraphQLClient(
        url="http://localhost:8069",
        db="dudoxx_backend3",
        username="admin",
        password="admin"
    )
    introspection_result = perform_introspection(client)
    print(introspection_result)
