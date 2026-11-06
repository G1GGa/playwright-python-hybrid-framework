import requests

BASE_URL = "https://reqres.in/api"

def test_get_users_list():
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert  response.status_code == 200

    data = response.json()
    assert "data" in data
    assert len(data['data']) > 0

def test_create_new_user():
    payload = {
        "name": "Giga",
        "job": "QA Automation Engineer"
    }
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201

    res_data = response.json()
    assert res_data["name"] == "Giga"
    assert res_data["job"] == "QA Automation Engineer"
    assert "id" in res_data