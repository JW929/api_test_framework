def assert_status_code(response, expected_status):
    assert response.status_code == expected_status, f"Expected status code {expected_status}, but got {response.status_code}"

def assert_json_field(response, field_name, expected_value):
    json_body = response.json()
    assert json_body[field_name] == expected_value, f"Expected {field_name} to be {expected_value}, but got {json_body[field_name]}"