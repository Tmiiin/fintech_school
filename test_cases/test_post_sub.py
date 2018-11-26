def test_post_sub(http_client):

    response = http_client.post_sub('1', '2', 'TCS_SPBXM', 'TCS', 'equity', 100, 'd.kovaleva')

    assert response.status_code == 201
