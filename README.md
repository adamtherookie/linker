<div align="center">
  <img src="./website/static/website/logo.png">
  <h2>Free and Open Source Link Sharing</h2>
  <a href="https://www.linkshar.in">Website</a> | <a href="https://discord.gg/g6ZSJdt8">Discord</a>
</div>

## What is linksharin'?
Linksharin' is a link sharer (surprise!). It gives you a unique link which you can then post on your social media profiles which then contains all the other links you would like your audience to see: personal websites, stores, content.... It also has a feature where you can generate custom private startpages with all your quicklinks and more!

## Running locally
If you want to host an instance of Linksharin' on your own server, or test it locally, you can clone the git repo

`git clone https://github.com/adamtherookie/linksharin`.

Then you must set up the sqlite3 database: `python manage.py makemigrations && python manage.py migrate`.

After that you can run the server: `python manage.py runserver`

Requires sqlite3, python and the Django, Beautiful Soup, and markdown modules.

## Contributing
Any contributions fixing issues or adding new features are greatly appreciated. A good place to start would to look at the goals below.

## Features + Goals
- [x] 100% FOSS
- [x] Custom CSS
- [ ] Drag and Drop mechanism for adding links
- [ ] Separate startpage CSS from page CSS
- [ ] Enable users to publish their custom themes (a theme marketplace or something of that sort)
- [ ] Detailed analytics with time-to-click, geographic distribution, referring sites, etc
- [ ] Portfolio generator
