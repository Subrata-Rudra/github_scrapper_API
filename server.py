from bs4 import BeautifulSoup
import requests
from flask import *
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET'])  # creating an endpoint for GET request
def home_page():
    data_set = {'Page': 'HomePage of GitHub Scrapper',
                'Message': 'Successfully loaded the HomePage'}
    json_dump = json.dumps(data_set)
    return json_dump


@app.route('/basic/', methods=['GET'])
def request_data():
    username = str(request.args.get('user'))
    base_url = "https://github.com/"
    final_url = base_url + username
    html_text = requests.get(final_url).text
    soup = BeautifulSoup(html_text, 'lxml')
    gitUsername = soup.find('span', class_ = "p-nickname vcard-username d-block").text
    guser = gitUsername[3:]
    name = soup.find(
        'span', class_="p-name vcard-fullname d-block overflow-hidden").text
    name0 = name[3:]
    bio = soup.find(
        'div', class_="p-note user-profile-bio mb-3 js-user-profile-bio f4").text
    connections = soup.find_all('span', class_="text-bold color-fg-default")
    followers = connections[0].text
    following = connections[1].text
    publicRepositories = soup.find('span', class_="Counter").text
    lastYearContribution = soup.find('h2', class_="f4 text-normal mb-2").text
    lastYearContribution0 = lastYearContribution[3:]
    data_set = {'GitHubUsername': guser, 'Name': name0, 'GitHubBio': bio, 'Followers': int(followers), 'Following': int(
        following), 'PublicRepositories': int(publicRepositories), 'LastYearContribution': lastYearContribution0}
    json_dump = json.dumps(data_set)
    return json_dump


@app.route('/repo/', methods=['GET'])
def repo_data():
    username = str(request.args.get('user'))
    base_url = "https://github.com/"
    final_url = base_url + username
    html_text = requests.get(final_url).text
    soup = BeautifulSoup(html_text, 'lxml')
    publicRepositories = soup.find('span', class_="Counter").text

    repoUrlFront = "https://github.com/" + username + "?page="
    repoUrlBack = "&tab=repositories"

    cnt = 1
    repoCnt = 0
    ind = 0
    repos_list = []

    while repoCnt < int(publicRepositories):
        repoUrlMiddle = str(cnt)
        repoUrl = repoUrlFront + repoUrlMiddle + repoUrlBack
        repoText = requests.get(repoUrl).text
        repoSoup = BeautifulSoup(repoText, 'lxml')
        repos = repoSoup.find_all('h3', class_="wb-break-all")
        for repo in repos:
            rep0 = repo.text
            rep1 = rep0[10:]
            required_length = len(rep1) - 8
            rep2 = rep1[:required_length]
            repos_list.insert(ind, rep2)
            repoCnt = repoCnt + 1
            ind = ind + 1
        cnt = cnt + 1  # increasing the cnt by 1 so that the repoUrlMiddle will change and will redirect to the next page

    repo_json = json.dumps(repos_list)

    data_set = {'PublicRepositories': repo_json}

    json_dump = json.dumps(data_set)
    return json_dump


if __name__ == '__main__':
    app.run()
