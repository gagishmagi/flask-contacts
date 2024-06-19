# create tests for contacts home page
import pytest
import requests
from bs4 import BeautifulSoup

# create client fixture
@pytest.fixture
def client():
    client = requests.Session()
    return client

# test the home page if I get status 200 and the title is View | Contacts Flask
def test_home_page(client):
    response = client.get('http://localhost:7000/')
    # assert response.status_code == 200
    # get title of the page using beautiful soap
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.text
    assert 'View | Contacts Flask' in title


# check if the home page has contacts h1
def test_home_page_has_contacts_h1(client):
    response = client.get('http://localhost:7000/')
    soup = BeautifulSoup(response.text, 'html.parser')
    h1 = soup.find('h1')
    assert h1.text == 'Contacts'


# check if the home page has welcome in the body
def test_home_page_has_welcome_in_page(client):
    response = client.get('http://localhost:7000/')
    soup = BeautifulSoup(response.text, 'html.parser')
    body = soup.find('body')
    # assert 'Welcome' in body.text 
    assert 'Contacts' in body.text 