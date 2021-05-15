# Web-Scraper

# About
For this project I created a web scraper using Python and BeautifulSoup                 

This web scraper will parse my Portfolio Website: ytang913.github.io

When the website is parsed a csv file projects.csv will be created

# Documentation

I created a request variable with my website's URL to request the page allowing me to scrape the webpage
                        
Then I created a variable to read the request variable and then closed it
                     
A html parser was created to parse through the div class "post-wrapper"
                        
I created csv file called projects.csv to store the parsed data

Headers are created to differentiate the data: Title and Description

A for loop is used to iterate through the html parser. Within the for loop there is a title and a description variable.
                        
The title and description variable are created scrape the "post-title" class and "post-intro" class
respectively using the iterator in the for loop, item.
                        
Then the data from the title and description is written on the csv file I created.
                        