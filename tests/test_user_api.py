import pytest
import requests

# 从配置文件加载的环境配置信息
from utils.config import load_config

@pytest.fixture(scope="module")
def base_url():
    config = load_config()
    return config["base_url"]

def test_get_user(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1



@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_user(base_url, user_id):
    response = requests.get(f"{base_url}/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["id"] == user_id