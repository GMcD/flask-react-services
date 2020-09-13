import json

def test_testing_config(service):
    assert service.config['TESTING']
    assert '_test' in service.config['SQLALCHEMY_DATABASE_URI']

def test_time_endpoint(service):
    client = service.test_client()
    resp = client.get('/time')
    assert resp.status_code == 200
    data = json.loads(resp.data.decode())
    assert 'time' in data
