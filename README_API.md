Under construction.

**API endpoints:**

- / - API docs \*under construction*
- /top - Characters ordered by nº of sentences in the show.
- /random/\<name> - Random sentences of the specified character.
<br>

- **Retrieve scripts:** 
    - /script - Script of the entire show.
    - /script/character/\<name> - Script of a given character for the entire show, divided in seasons and episodes.
    - /script/\<season>/ - Script of an entire season.
    - /script/\<season>/character/\<name> - Script of a character for a given season divided in episodes.
    - /script/\<season>/\<episode> - Script of a character for a given episode.
    - /script/\<season>/\<episode>/\<name> - Script of a character for a given episode of a season.
<br>

- **Retrieve sentiment analysis (SA):** 
    - /script/sa/character/\<name> - SA of a character for the entire show.
    - /script/sa/\<season> - SA of an entire season.
    - /script/sa/\<season>/mean/character/\<name> - Mean SA of a character for the entire show.
    - /script/sa/\<season>/meanstop/character/\<name> - Mean SA of a character for the entire show filtering out stop words.
    - /script/sa/\<season>/\<episode> - SA of an entire episode of a season.
    - /script/sa/\<season>/\<episode>/\<name> - SA of a character for a given episode of a season.
    - /script/sa/\<season>/\<episode>/mean/character/\<name> - Mean SA of a character for a given episode of a season.
    - /insertrow - Inserts a new row into the script dataset.