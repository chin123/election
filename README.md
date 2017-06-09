# Election
# Requirements
1. Python 2.7.6.1 or above
2. Django 1.6.2 or above
  
# Running
1. Store all the names of the voters in a file names `allfiles.csv` in the root directory of the code with the following format:  
A heading in the first line (The first line is not read into the voters list)  
All the names of the voters in the following format:  
`S. No.,Name,House`  
If the house name is left blank, the name will be added to all the houses.  
2. Go to the root directory of the code and run `python manage.py runserver <ip address>:<port>`  

# Adding Names of Nominees  
1. Store the images of all the nominees in the root directory of the code.  
2. Navigate to <ip address>:<port>/settings in your web browser. 
3. In the image path, just type in the file name of the image.  

# Features
1. A voters list to manage attendance and to prevent double voting
2. All  the 4 houses, and prefect elections can run on the same server instance

# List of URLs
Function          | URL
------------------|----------------------------
Settings          |`/settings`
Voters List       |`/choose?house=<house name>`
Results           |`/results?house=<house name>`
Voting Page       |`/vote?house=<house name>`
Load from savefile|`/loadsave`

# License
GPL V3  
![GPL V3 Logo](gplv3.png)  

# Contributors  
Chinmaya M
Rahul B
Nikhil I
