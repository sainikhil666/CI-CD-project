
import unittest
import requests
import json

URL = "https://w83wuqwch8.execute-api.us-east-1.amazonaws.com/welcome/"

class Testing(unittest.TestCase):
    def test_string(self):
        remote = requests.get(URL)
        remote = remote.text
        with open("data.json", "r", encoding="utf-8") as f:
            local = f.read()
        local = json.loads(local)
        self.assertEqual(remote, local["message"])

if __name__ == '__main__':
    unittest.main()
