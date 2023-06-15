# github_scrapper
This is a simple flask api for getting someone's GitHub profile details such as Name, No. of public repositories, No. of followers, No. of following, all repositories' name etc, made by scraping GitHub. Scraping is done using Beautifulsoup4 library.

## API Endpoint
### Production
#### To Get Basic Details
Send GET Request at this url and get basic GitHub profile details of somenone https://github-scrapper-by-subrata.onrender.com/basic/?user=<GITHUB_USERNAME>
#### To Get All Public Repositories Name
Send GET Request at this url and get basic GitHub profile details of somenone https://github-scrapper-by-subrata.onrender.com/repo/?user=<GITHUB_USERNAME>
### Development
#### To Get Basic Details
Send GET Request at this url and get basic GitHub profile details of somenone http://localhost:5000/basic/?user=<GITHUB_USERNAME>
#### To Get All Public Repositories Name
Send GET Request at this url and get basic GitHub profile details of somenone http://localhost:5000/repo/?user=<GITHUB_USERNAME>
