def test_delete_sub(http_client):

    response = http_client.delete_sub('d.kovaleva', '1', '2', '2')

    assert response.status_code == 200
