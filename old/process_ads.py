# -*- coding: utf-8 -*-
import ads
from jinja2 import Environment, FileSystemLoader
env = Environment(loader=FileSystemLoader(''))

ads.config.token = '7scWI1Z2A8kPAukKoYUPKyzlQqn3eSY1m4r0QCTo'

all_query = 'author:"duncan, k" year:2013-2020 database:astronomy property:refereed'

first_author = 'author:"^duncan, k" year:2013-2020 database:astronomy property:refereed'


allp = list(ads.SearchQuery(q=all_query, sort="date"))
first = list(ads.SearchQuery(q=first_author, sort="citation_count"))

template = env.get_template('publications_template.html')
out = template.render(all=allp)

with open("publications.html", "wb") as f:
    f.write(out)