def remove_url_anchor(url):
   return url.split('#')[0]

if __name__ == '__main__':
    url1 = "www.codewars.com#about"
    url2 = "www.codewars.com/katas/?page=1#about"
    url3 = "www.codewars.com/katas/"

    val1 = remove_url_anchor(url1)
    val2 = remove_url_anchor(url2)
    val3 = remove_url_anchor(url3)