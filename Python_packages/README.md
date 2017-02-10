# Useful Python Packages

As you work through a problem, you will find invaluable community developed packages at your disposal. Below are just a few packages that I have found useful.

### DS_Util

[DS_Util](https://github.com/Ibotta/ds_util) is a repository the data science team will be developing with useful functions like redshift connectors and s3 interfaces in this repository. If you want to use it you will need to:

```
git clone https://github.com/Ibotta/ds_util

pip install <path to cloned repository, usually ~/ds_util/>
```

### Data Science

* [Pandas](http://pandas.pydata.org/)

  * Data Storage and manipulation workhorse. If you can do it in SQL you can do it in Pandas, and if you can't do it in SQL you can still do it in Pandas!

  * Built on top of [Numpy](http://www.numpy.org/), which is optimized array manipulation. Useful for working with arrays and performing aggregate operations.

* [Scikit-learn](http://scikit-learn.org/stable/)

  * Algorithms, advanced data manipulation, imputation, normalization, prediction, and all around data science.

* [Keras](https://keras.io/)

  * Deep Learning building blocks. Unbelievably easy to get started with all flavors of Neural Nets!

### Web Scraping

  * [Requests](http://docs.python-requests.org/en/master/)

    * HTTP requests, to bring the html to your computer.

  * [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)

    * If you need to parse HTML code when you web scrape, this is a great tool.

### Some Useful basics worth knowing

* os, sys, collections (DefaultDict)
