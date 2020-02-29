import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus  # nos ayuda con las url si hay espacios
from . import models

# BASE_CRAIGSLIST_URL = 'https://alicante.craigslist.org/search/bbb?query='
BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/bbb?query='
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'


def home(request):
    return render(request, template_name='base.html')


def new_search(request):
    search = request.POST.get('search')
    # We save a search into ddbb
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL + "{}".format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    # Here we get the information
    post_rows = soup.find_all('li', {'class': 'result-row'})

    final_results = []
    if len(post_rows) > 0:
        for post in post_rows:
            post_title = post.find(class_='result-title').text
            post_url = post.find('a').get('href')
            if post.find(class_='result-price'):
                post_price = post.find(class_='result-price').text
            else:
                post_price = 'N/A'

            if post.find('a') and post.find('a').get('data-ids'):
                ids = post.find('a').get('data-ids')
                if len(ids) >= 1:
                    id_image = ids.split(',')[0][2:]
                    post_image_url = BASE_IMAGE_URL.format(id_image)
            else:
                post_image_url = 'https://craigslist.org/images/peace.jpg'
            final_results.append({
                'post_title': post_title,
                'post_url': post_url,
                'post_price': post_price,
                'post_image_url': post_image_url
            })
    data = {
        'search': search, # What user has typed
        'final_results': final_results
    }
    return render(request, 'codecoursesapp/new_search.html', data)
