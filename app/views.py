# builtins
import secrets
import requests
import socket
import re

# dependencies
from flask import Blueprint, render_template, flash, request
from bs4 import BeautifulSoup

# local files
from .mail import send_mail

views = Blueprint('views', __name__)
views.secret_key = secrets.token_urlsafe(16)

PORT = 8080
HOST = socket.gethostname()
FETCH_LOCAL_URL = f'http://{socket.gethostbyname(HOST)}:{PORT}/'

def parse_search_page(text: str):
    soup = BeautifulSoup(text, 'html.parser')
    all_sections = str(soup.find_all(name='h3'))
    return soup.get_text(), re.findall(r'"([^"]*)"', all_sections)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        body = request.form['message']
        if email != "" and name != "" and subject != "":
            if send_mail(name, email, subject, body) and send_mail(name, email, subject, body, send_to_admin=True):
                flash('Votre message a bien été envoyé !', category='success')
            else:
                flash('Une erreur est survenue !', category='error')
        else:
            flash('Veuillez remplir tous les champs !', category='error')
    return render_template('contact.html')

@views.route('/moyenne/')
def contrainte():
    return render_template('moyenne.html')

@views.route('/nos-projets/')
def presentation():
    return render_template('projets.html')

@views.route('/search-results/', methods=['GET', 'POST'])
def search_results():
    link = '/#'
    page = 'Présentation'
    search_results = set()
    if request.method == 'POST':
        search = request.form['search']
        if search == '':
            return render_template('search.html')
        content_page_response = requests.get(FETCH_LOCAL_URL)
        content_page_text, sections = parse_search_page(content_page_response.text)
        content_page_text = content_page_text.split()
        for word in content_page_text:
            if search.lower() in word:
                search_results.add(word)
        for search_result in search_results:
            flash(f"[...] {content_page_text[content_page_text.index(search_result) - 1]} {search_result} {content_page_text[content_page_text.index(search_result) + 1]} [...]")
    return render_template('search.html', link=link+sections[0], page=page)
