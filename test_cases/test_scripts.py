def test_script(http_client):

    response = http_client.get_instruments(request_id='1', system_code='2')

    assert response.status_code == 200


def test_post_sub(http_client):
    response = http_client.post_sub('1', '2', 'TCS_SPBXM', 'TCS', 'equity', 14, 'd.kovaleva')

    assert response.status_code == 201


def test_script(http_client):

    response = http_client.get_sub(siebel_id='d.kovaleva', request_id='1', system_code='2')

    assert response.status_code == 200


def test_delete_sub(http_client):

    response = http_client.delete_sub('d.kovaleva', '1', '2', '2')

    assert response.status_code == 200



