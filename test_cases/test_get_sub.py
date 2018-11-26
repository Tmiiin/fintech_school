def test_script(http_client):

    response = http_client.get_sub(siebel_id='d.kovaleva', request_id='1', system_code='2')

    assert response.status_code == 200
