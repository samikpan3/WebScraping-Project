#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing all the required dataset to run all task.
import requests
import pandas as pd         
from bs4 import BeautifulSoup


# ## Parse HTML webpage
# 

# In[2]:


imdbmovie = "https://www.imdb.com/search/title/?title_type=tv_series&num_votes=,100000&sort=runtime,asc"
page = requests.get(imdbmovie)

soup = BeautifulSoup(page.content, "html.parser")


# In[3]:


lister = soup.find(id = "main")
movies = lister.find_all("div", class_ = "lister-item mode-advanced")


# In[4]:


titles = []
years_name = []
ratings = []
series_runtime_name = []
genre_name = []
star_name = []
plot_name = []


# In[5]:


star_strip = lambda x: x.replace('\n', '').replace('Star:', '').replace('Stars:', '').strip()
plot_strip = lambda x: x.replace('Add a Plot', '').strip()
year_strip =lambda x: x.replace('(', '').replace('–', '').replace(")", '').strip()
 


# In[6]:


for movie in movies:
    #print(movies.prettify())
    title = movie.h3.a.text
    premier_year = movie.h3.find('span', class_ ="lister-item-year text-muted unbold" )
    if (premier_year is not None):
        year = year_strip(premier_year.get_text())
    else: 
        year = 'NA'
        
    ratingclass = movie.find("div", class_ ="inline-block ratings-imdb-rating")
    if (ratingclass is not None):
        rating = ratingclass.strong.get_text()
    else: 
        rating = 'NA'
        
    series_runtime = movie.find("span", class_ = "runtime")
    if (series_runtime is not None):
        series_runtimetotal =series_runtime.get_text()
    else: 
        series_runtimetotal = "NA"
    
    genre = movie.find('span', class_ = "genre")
    if (genre is not None):
        genre_text = genre.get_text().strip('\n')
    else: 
        genre_text = "NA"
    stars = movie.find("p",class_ ="")
                                            
    if (stars is not None):
        stars_final = star_strip(stars.get_text())
    else: 
        stars_final = 'NA'
    
    plotclass = movie.find_all("p", class_ = "text-muted") [1]                                   
    if (plotclass is not None):
        plot = plot_strip(plotclass.get_text())
    else: 
        plot = "NA" 
    
    titles.append(title)
    years_name.append(year)
    ratings.append(rating)
    series_runtime_name.append(series_runtimetotal)
    genre_name.append(genre_text)
    star_name.append(stars_final)
    plot_name.append(plot)

        


# In[8]:


movie_first = pd.DataFrame({
    "Title" : titles,
    "Premiere Year": years_name,
    "Rating": ratings,
    "Time": series_runtime,
    "Genre": genre_name,
    "Star": star_name,
    "Plot": plot_name
 }) 

movie_first.head(10)


# In[ ]:





# In[19]:


movie_first.to_csv("movies_first.csv")


# ## Task 2 

# In[11]:


titles_2010 = []
years_name_2010 = []
ratings_2010 = []
series_runtime_2010 = []
genre_name_2010 = []
star_name_2010 = []
plot_name_2010= []
for movie in movies:
    #print(movies.prettify())
    title = movie.h3.a.text
    premier_year = movie.h3.find('span', class_ ="lister-item-year text-muted unbold" )
    if (premier_year is not None):
        year = year_strip(premier_year.get_text())
        year = int(year)
    else: 
        year = 'NA'
        
    ratingclass = movie.find("div", class_ ="inline-block ratings-imdb-rating")
    if (ratingclass is not None):
        rating = ratingclass.strong.get_text()
    else: 
        rating = 'NA'
        
    series_runtime = movie.p.find("span", class_ = "runtime")
    if (series_runtime is not None):
        series_runtimetotal =series_runtime.get_text()
    else: 
        series_runtimetotal = "NA"
    
    genre = movie.find('span', class_ = "genre")
    if (genre is not None):
        genre_text = genre.get_text().strip('\n')
    else: 
        genre_text = "NA"
    
    stars = movie.find("p",class_ ="")
                                            
    if (stars is not None):
        stars_final = star_strip(stars.get_text())
    else: 
        stars_final = 'NA'
    
    plotclass = movie.find_all("p", class_ = "text-muted")[1]
                                            
    if plotclass is not None:
        plot = plot_strip(plotclass.get_text())
    else: 
        plot = "NA"
        
    if (year > 2009):
    
        titles_2010.append(title)
        years_name_2010.append(year)
        ratings_2010.append(rating)
        series_runtime_2010.append(series_runtimetotal)
        genre_name_2010.append(genre_text)
        star_name_2010.append(stars_final)
        plot_name_2010.append(plot)


# In[ ]:





# In[12]:


movie_2010 = pd.DataFrame({
    "Title" : titles_2010,
    "Premiere Year": years_name_2010,
    "Rating": ratings_2010,
    "Time": series_runtime_2010,
    "Genre": genre_name_2010,
    "Star": star_name_2010,
    "Plot": plot_name_2010
 }) 

movie_2010.head()
#movies_2010.to_csv(index = False)


# In[18]:


movie_2010.to_csv("movies_2010.csv")


# ## Task 3 

# In[ ]:





# In[15]:




for i in range(10):
    start_page = (i*50)+1
    imdbmovie = 'https://www.imdb.com/search/title/?title_type=tv_series&num_votes=,100000&sort=runtime,asc&start='+ str(start_page) +'&ref_=adv_nxt'
    page = requests.get(imdbmovie)
    soup = BeautifulSoup(page.content, "html.parser")

    
    lister = soup.find(id = "main")
    movies = lister.find_all("div", class_ = "lister-item-content")
    
    titles_task3 = []
    years_name_task3 = []
    ratings_task3 = []
    series_runtime_task3 = []
    genre_name_task3 = []
    star_name_task3 = []
    plot_name_task3 = []
    
    star_strip = lambda x: x.replace('\n', '').replace('Star:', '').replace('Stars:', '').strip()
    plot_strip = lambda x: x.replace('Add a Plot', '').strip()
    year_strip =lambda x: x.replace('(', '').replace('–', '').replace(")", '').strip()
    for movie in movies:
    #print(movies.prettify())
        title = movie.h3.a.text
        premier_year = movie.h3.find('span', class_ ="lister-item-year text-muted unbold" )
        if (premier_year is not None):
            year = year_strip(premier_year.get_text())
        else: 
            year = 'NA'
        
        ratingclass = movie.find("div", class_ ="inline-block ratings-imdb-rating")
        if (ratingclass is not None):
            rating = ratingclass.strong.get_text()
        else: 
            rating = 'NA'
        
        series_runtime = movie.p.find("span", class_ = "runtime")
        if (series_runtime is not None):
            series_runtimetotal =series_runtime.get_text()
        else: 
            series_runtimetotal = "NA"
        genre = movie.find('span', class_ = "genre")
    #     print(genre)

        if (genre is not None):
            genre_text = genre.get_text().strip('\n')
        else: 
             genre_text = "NA"
        stars = movie.find("p",class_ ="")
        if (stars is not None):
            stars_final = star_strip(stars.get_text())
        else: 
            stars_final = 'NA'
        plotclass = movie.find_all("p", class_ = "text-muted")[1]
        if plotclass is not None:
            plot = plot_strip(plotclass.get_text())
        else: 
            plot = "NA"
    
        titles_task3.append(title)
        years_name_task3.append(year)
        ratings_task3.append(rating)
        series_runtime_task3.append(series_runtimetotal)
        genre_name_task3.append(genre_text)
        star_name_task3.append(stars_final)
        plot_name_task3.append(plot)


# In[16]:


movie_all = pd.DataFrame({
"Title" : titles_task3,
"Premiere Year": years_name_task3,
"Rating": ratings_task3,
"Time": series_runtime_task3,
"Genre": genre_name_task3,
"Star": star_name_task3,
"Plot": plot_name_task3
})

movie_all.head()
#movies_2010.to_csv(index = False)


# In[20]:


movie_all.to_csv("movies_all.csv")

