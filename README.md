**Ironhack Project-4**

---
# API of Thrones 
#### An analysis of the Game of Thrones character language through a self-built API
---
## 1- Main objective
## 2- Structure of the API
API endpoints:
| **Endpoint** | **Information** |
| --- | --- |
| / | API docs |
| /top | Characters ordered by nº of sentences |
| /random/\<name> | Random sentences of the specified character |
| **Show scripts** | 
| /script | Script of the entire show |
| ........ /character/\<name> | Script of a character for the entire show |
| ........ /\<season>/ | Script of an entire season |
| .................... /character/\<name> | Script of a character for a given season |
| .................... /\<episode> | Script of an entire episode of a season |
| ................................ /\<name> | Script of a character for a given episode of a season |
| **Show sentiment analysis (SA)** |
| ........ /sa/character/\<name> | SA of a character for the entire show |
| .................... /mean/character/\<name> | Mean SA of a character for the entire show | 
| .................... /meanstop/character/\<name> | Mean SA (filtering out stopwords) of a character for the entire show |
| .................... /\<season> | SA of an entire season |
| ................................ /\<episode> | SA of an entire episode of a season |
| ............................................ /\<name> | SA of a character for a given episode of a season |
| ............................................ /mean/character/\<name> | Mean SA of a character for a given episode of a season |
| /insertrow |


## 3- Queries
### 3.1- Get
### 3.2- Post
## 4- Sentiment analysis
**Main GoT characters based on number of sentences**

**Comparing the presence of stopwords in the SA**

**Sentiment score of the top 20 main characters**

**Evolution of main characters by season**

**Most negative episodes**

-
-

**Oberyn Martell vs The Mountain**

**Theon Greyjoy vs Ramsay Bolton**

