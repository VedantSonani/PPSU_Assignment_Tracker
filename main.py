import requests
from bs4 import BeautifulSoup

LOGIN_URL = "https://erp.ppsu.ac.in/Login.aspx"

headers = {
    "User-Agent": "Mozilla/5.0"
}
session = requests.Session()