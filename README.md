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
| **Show scripts**| 
| /script | Script of the entire show |
| ..... /character/\<name> | Script of a character for the entire show |
| ..... /\<season>/ | Script of an entire season |
| ............... /character/\<name> | Script of a character for a given season |
| ............... /\<episode> | Script of an entire episode |
| .......................... /\<name> | Script of a character for a given episode |
| ..... /sa/character/\<name> | Script |
| ............... /mean/\<name> |
| **Show sentiment analysis**
| /script/sa/\<season> |
| ......... /character/\<name> |
| ......... /mean/character/\<name> |
| ......... /meanstop/character/\<name> |
| ......... /\<episode>/mean/character/\<name> |
| ......... /\<episode> |
| .................. /\<name> |
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

