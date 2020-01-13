# codecourseslist-app

I created a clone of [craiglist](https://alicante.craigslist.org/) just for learning **Django**.

## Demo
[codecourseslist-app](https://codecourseslist-app.herokuapp.com/)

## Local setup

Download the project with:

`git clone `

then create an enviroment and install the requirements:

`pip install -r requirements.txt`

finally to run the app locally:

`cd codecourseslist`
`souce ../env/bin/activate` 

`python manage.py runserver`

and access to the url:

http://127.0.0.1:8000/



Commands for creating the project:
`conda create --name codecourseslist-app python=3`

`django-admin startproject codecourseslist-app`

To add style and stuff I have added these lines to the file base.html:

```html
<link
  rel="stylesheet"
  type="text/css"
  media="screen"
  href='{% static "css/style.css" %}'
/>
<!-- Compiled and minified CSS -->
<link
  rel="stylesheet"
  href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css"
/>
<link
  href="https://fonts.googleapis.com/css?family=Montserrat|Roboto&display=swap"
  rel="stylesheet"
/>
<link
  href="https://fonts.googleapis.com/icon?family=Material+Icons"
  rel="stylesheet"
/>
```
