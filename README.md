# instagram-query
Designed using Juypter Notebook in order to filter and query different users based on the schools they are currently enrolled into. Allows for the user to insert a .csv file that contains name, biography, username, and followers count data resepctively. 

## Usage
Replace and insert your own .csv file. Take note that python does recongize backwards slash. 
```python
file = "replace_with_csv_file_path"
```

The program will use specific queries in order to export an output.xlsx file that contains all of the query information. Edit any of the following queries to match personal usages. 

```python

# list of queries for high schools 
hs_query = 'qa|nchs|ice|ahs|south division 21’|whitney 2020|ccat|carver|ascs|bdhs|kchs|cuyahoga falls|oak hill|high school|highschool|mshs|ajhs|battle mountain|avhs|eleanor roosevelt high'

# lists of queries for colleges 
college_query = 'university|jhu|college|john hopkins|stanford|mit|cmu|university of maryland|goucher|Frostburg|gt|purdue|florida state|jmu|Dsu|morgan state|upenn|penn state|hopkins|ic|isu|ksu|lmu|mcla|2021🎓|niu|occ|rwu|full sail|tamu|uchicago|U of C|virginia tech|xavier|yale|rit|george mason|temple|florida tech|cal poly|C’O 19|berkeley'

# list of queries for years
year_query = 'c"\\"o2021|\'21|‘21|co21|c"\\"o21|c"\\"o2020|\'20|co20|‘20|c"\\"o20|c"\\"o2019|‘19|\'19|co19|c"\\"o19|c"\\"o2018|‘18|\'18|co18|c"\\"o18|c"\\"o2017|\'17|‘17|co17|c"\\"o17'
```

Change the directory of the output file by editing the [directory] to be the absolute path of where you want the file to be exported. 

```python
directory = 'instagram query'
file = 'output.xlsx'

if not os.path.exists(directory): 
    os.makedirs(directory)
path = os.path.join(directory, file)
```
