from flask import url_for

def test_main_page_view(client):
    response = client.get(url_for('home_bp.home'))
    assert response.status_code == 200
    assert b'Welcome' in response.data

def test_about_view(client):
    response = client.get(url_for('home_bp.about'))
    assert response.status_code == 200
    assert b'I am Blyznyuk Nazar' in response.data

def test_skills_view(client):
    response = client.get(url_for('home_bp.skills'))
    assert response.status_code == 200
    assert b'C++' in response.data
    assert b'I have experience' in response.data

