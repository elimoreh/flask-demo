import flask

def test_users_route(app, client):
    res = client.get('/users')
    assert res.status_code == 200