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
| &rarr; /character/\<name> | Script of a character for the entire show |
| &rarr; /\<season>/ | Script of an entire season |
| &rarr; &rarr; /character/\<name> | Script of a character for a given season |
| &rarr; &rarr; /\<episode> | Script of an entire episode |
| &rarr; &rarr; &rarr; /\<name> | Script of a character for a given episode |
| **Show sentiment analysis (SA)** |
| &rarr; /sa/character/\<name> | SA of a character for the entire show |
| &rarr; &rarr; /mean/character/\<name> | Mean SA of a character for the entire show | 
| &rarr; &rarr; /meanstop/character/\<name> | Mean SA (filtering out stopwords) of a character for the entire show |
| &rarr; &rarr; /\<season> | SA of an entire season |
| &rarr; &rarr; &rarr; /\<episode> | SA of an entire episode |
| &rarr; &rarr; &rarr; &rarr; /\<name> | SA of a character for a given episode |
| &rarr; &rarr; &rarr; &rarr; /mean/character/\<name> | Mean SA of a character for a given episode |
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

