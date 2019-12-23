# codecourseslist-app

I am creating a clone of [craiglist](https://alicante.craigslist.org/) just for learning

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
