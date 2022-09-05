
# Ecojoy

Transforming planting into an experience


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


##
Made with ❤ by Anvansh ([@RyanWalker277](https://github.com/RyanWalker277))
