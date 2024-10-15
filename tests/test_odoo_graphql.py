import unittest
from graphql_client import OdooGraphQLClient

class TestOdooGraphQL(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = OdooGraphQLClient(
            url="http://localhost:8069",
            db="dudoxx_backend3",
            username="admin",
            password="admin"
        )

    def test_connection(self):
        try:
            self.client.authenticate()
            self.assertTrue(True)
        except Exception as e:
            self.fail(f"Connection test failed: {e}")

    def test_model_retrieval(self):
        introspection_query = """
        {
          __schema {
            types {
              name
            }
          }
        }
        """
        result = self.client.execute_query(introspection_query)
        self.assertIn('data', result)
        self.assertIn('__schema', result['data'])

    def test_attribute_retrieval(self):
        model_name = "res_partner"  # Example model name
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
        result = self.client.execute_query(query)
        self.assertIn('data', result)
        self.assertIn(model_name, result['data'])

if __name__ == '__main__':
    unittest.main()
