def test_get_all_planets_with_no_records(client):
    # Act
    response = client.get("/planets")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []


def test_get_one_planet(client, two_saved_planets):
    # Act
    response = client.get("/planets/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name": "Jupiter",
        "description": "cool planet"
    }


def test_no_data_returns_error(client):
    response = client.get("/planets/5")
    assert response.status_code == 404


def test_client_can_post(client, planet_data):
    response = client.post ("/planets", json=planet_data)
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == jsonify(f"Planet {planet_data.name} successfully created", 200)