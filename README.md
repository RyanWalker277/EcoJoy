# Ecojoy

Ecojoy is a portal to connect local vendors with global online market for plants.A local vendor can list his products on the website's "shop" section.It also has an AR app which can identify plants and list it's details.

[![GitHub issues](https://img.shields.io/github/issues/RyanWalker277/EcoJoy)](https://github.com/RyanWalker277/EcoJoy/issues)
[![GitHub forks](https://img.shields.io/github/forks/RyanWalker277/EcoJoy)](https://github.com/RyanWalker277/EcoJoy/network)
[![GitHub stars](https://img.shields.io/github/stars/RyanWalker277/EcoJoy)](https://github.com/RyanWalker277/EcoJoy/stargazers)
[![GitHub license](https://img.shields.io/github/license/RyanWalker277/EcoJoy)](https://github.com/RyanWalker277/EcoJoy/blob/main/LICENSE)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) ![contributions welcome](https://img.shields.io/static/v1.svg?label=Contributions&message=Welcome&color=0059b3&style=flat-square) ![GitHub contributors](https://img.shields.io/github/contributors-anon/RyanWalker277/EcoJoy) 
<br>

## Demo

The demo of the project can be found at 
https://rakathon2022.pythonanywhere.com/


## Setup Instructions

Clone the repo in your local system

```bash
  git clone https://github.com/RyanWalker277/Rakathon-Backend.git
```
Install virtualenv

```bash
  py -m pip install --user virtualenv
```
Create a new Virtualenvironment

```bash
  py -m venv env
```
Activate the Virtualenvironment with

```bash
  .\env\Scripts\activate
```
Change directory to the folder

```bash
  cd folder-where-you-cloned-the-repo
```
Install all the requirements with

```bash
  pip3 install -r requirements.txt
```
Apply all the migrations with 

```bash
  python3 manage.py migrate
```
Run the developement server with 

```bash
  python3 manage.py runserver
```
You'll see output like this
```bash
  Performing system checks...

System check identified no issues (0 silenced).
July 04, 2022 - 15:50:53
Django version 4.0, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Creating Superuser

Clone the repo in your local system

```bash
python3 manage.py createsuperuser
```
You will see a screen like this

```bash
Username (leave blank to use 'default'):
```
Enter a username and press enter , you will see a screen like this

```bash
Email address:
```
Enter an email and press enter , then you will see a screen like this

```bash
Password:
```
Enter a password , then you will see a screen like this

```bash
Password (again):
```
Re-enter the password and you are done! You will see a screen like this

```bash
Superuser created successfully
```

## Tech Stack

**Client:** HTML , CSS , Javascript

**Server:** Django , Python

**User Authentication:** Django-allauth

**Ar:** Unity , Vyuyforia Engine

## Features

- Convinient E-Commerce store for plants 
- Plant identification through AI
- AR app for recognition of plants and augumenting the details of the plant in realtime

## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

<!-- readme: contributors -start -->
<table>
<tr>
    <td align="center">
        <a href="https://github.com/RyanWalker277">
            <img src="https://avatars.githubusercontent.com/u/32684077?v=4" width="100;" alt="RyanWalker277"/>
            <br />
            <sub><b>Anvansh</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/manaswii">
            <img src="https://avatars.githubusercontent.com/u/85053597?v=4" width="100;" alt="manaswii"/>
            <br />
            <sub><b>Manaswi Sharma</b></sub>
        </a>
    </td>
    <td align="center">
        <a href="https://github.com/Yash-Var">
            <img src="https://avatars.githubusercontent.com/u/95767787?v=4" width="100;" alt="Yash-Var"/>
            <br />
            <sub><b>Yash Varshney</b></sub>
        </a>
    </td></tr>
</table>
<!-- readme: contributors -end -->

## Support++

This project needs your shiny star ⭐.   
Don't forget to leave a star ⭐️

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)  [![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)


##
Made with ❤ by Anvansh ([@RyanWalker277](https://github.com/RyanWalker277))
