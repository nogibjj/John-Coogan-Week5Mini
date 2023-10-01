[![Test,Lint,Format](https://github.com/johncoogan53/sqlite-lab_John-Coogan/actions/workflows/cicd.yml/badge.svg)](https://github.com/johncoogan53/sqlite-lab_John-Coogan/actions/workflows/cicd.yml)

## SQLite ETL Command Line Tool
### Overview
![Alt text](<Project Architecture.png>)'

This project uses SQLite to extract, transfer, load, and dynamically query a database through a command line interface tool via python fire. The data includes rankings of video games by name, producer, platform, year, user scores, and critic scores. This command line tool allows for quick SQL queries while employing SQLite's ability to host local databases. Because of SQLite's ability to handle very large data, this project is scalable to much larger datasets. 

### Reflection

During this project, I found issues with the standard extract syntax handling url's which were not raw csv files. This can be an issue with common data science websites like Kaggle. I circumvented this issue by uploading the csv to github and using the github user content as the url. This will allow this code to be reproducible for anyone attempting to run it without the csv file as it pull directly from this github repository.

This project provided initial exposure to SQL and querying. It became readily apparent that while SQL queries are very powerful, they also require specificity and a deliberate approach. This is highlighted by the below command line log of some example queries:
![Alt text](Query_OutputsV2.png)

What we see here is that SQL allows us to very quickly gain complex insights into a database. Here we have asked for all the video games produced by Valve ranked by User Score. What I quickly found is that Valve is represented in the dataset under many variations of that company name. The complete list returned by the first query seemed to be incomplete based off my domain knowledge and so I wanted to see what was missing. The second query shows all the different titles for Valve in the publisher column. Following that up with a refined query utilizing wild cards gave me a more comprehensive list of their titles. 

The fourth query shows that multiple database values can be queried at once. This is a very powerful feature of SQL and allows for quick and easy comparisons.

The power of this tool is quite clear, however, the cost tradeoff is the mastery of yet another syntax like SQL. That said, this is essentially necessary for 'Big Data' and can be seemlessly integrated with python processing and visualization tools.

During this assignment, I was assisted by github copilot. I would rate this AI tool higher than codewhisper as it has a chat function and provides recommendations in real time. It also seems to be amore user friendly service which feels more accurate than codewhisper. 

Changes I would make to this project are to add more python processing of database outputs. I think this will be the future direction for this project to become more familiar with python and SQL integration.



