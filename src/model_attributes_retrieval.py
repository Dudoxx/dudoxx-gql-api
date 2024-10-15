from graphql_client import OdooGraphQLClient

def retrieve_model_attributes(client, model_name):
    query = f"""
    {{
      {model_name} {{
        __typename
        fields {{
          name
          type {{
            name
          }}
        }}
      }}
    }}
    """
    result = client.execute_query(query)
    return result

if __name__ == "__main__":
    client = OdooGraphQLClient(
        url="http://localhost:8069",
        db="dudoxx_backend3",
        username="admin",
        password="admin"
    )
    # Example model name, replace with actual model names retrieved from introspection
    model_name = "res_partner"
    attributes_result = retrieve_model_attributes(client, model_name)
    print(attributes_result)
