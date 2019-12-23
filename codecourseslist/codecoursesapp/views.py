import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from requests.compat import quote_plus  # nos ayuda con las url si hay espacios
from . import models

BASE_CRAIGSLIST_URL = 'https://alicante.craigslist.org/search/bbb?query='
# BASE_CRAIGSLIST_URL = 'https://losangeles.craigslist.org/search/bbb?query='


def home(request):
    return render(request, template_name='base.html')


def new_search(request):
    search = request.POST.get('search')
    # We save a search into ddbb
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGSLIST_URL + "{}".format(quote_plus(search))
    print(final_url)
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
        # post_title = post_rows.find_all('a', { 'class': 'result-title'})
        # post_url = post_rows.find_all('p', { 'class': 'result-info'})
        # post_price =
        final_results.append({
            'post_title': post_title,
            'post_url': post_url
        })

    print(final_results)
    data = {
        'search': search,
        'final_results': final_results
    }
    print(data)
    return render(request, 'codecoursesapp/new_search.html', data)
