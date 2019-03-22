from flask import Flask
from flask import render_template
import requests
import os

app = Flask(__name__)

@app.route('/')
def index():
    user_email = ''
    user_repos = []
    lang_stats = {}

    token = os.environ['TOKEN']
    url = "https://api.github.com/user/emails"
    headers = { 'Authorization': 'token '+ token, 'X-Oauth-Scope': 'user:email' }
    response = requests.get(url,headers=headers)
    data = response.json()

    for item in data:
        if item['primary']:
            user_email = item['email']

    url = "https://api.github.com/users/0xBEDEAD/repos"
    response = requests.get(url)
    data = response.json()
    lang_urls = []

    for entry in data:
        user_repos.append(entry['name'])
        lang_urls.append(entry['languages_url'])

    for url in lang_urls:
        response = requests.get(url)
        data = response.json()
        for language in data:
            if language in lang_stats:
                lang_stats[language] += data[language]
            else:
                lang_stats[language] = data[language]

    return render_template('index.html', user_email=user_email, user_repos=user_repos, lang_stats=lang_stats)
