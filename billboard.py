# Get the artist on Billboard 100 and the number of weeks
def artist_weeks(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS artistWeeks (artist TEXT PRIMARY KEY, num_weeks INTEGER)")
    count = 0
    # cur.execute("SELECT num_weeks FROM artistWeeks") #CHECK THE SELECT STATEMENT
    
    url = '
https://www.billboard.com/charts/artist-100
'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    d = {}
    data = soup.find('div', class_ = 'chart-details')
    rows = data.find_all('div', class_  = "chart-list-item")

    for row in rows:
         artist_row = row.find_all('span', class_ = "chart-list-item__title-text")
         stats_row = row.find_all('div', class_ = "chart-list-item__ministats-cell")

         for ar in artist_row: #top 100 artists
             if count == 25:
                break
             else:
                artist= ar.text.strip()
                temp = stats_row[2].text
                num_weeks = temp.split()[0] #number of weeks on the billboard
                # cur.execute("INSERT OR IGNORE INTO artistWeeks (artist, num_weeks) VALUES (?, ?)", (artist, num_weeks))
                if cur.execute("SELECT artist AND num_weeks FROM artistWeeks WHERE artist = ? AND num_weeks = ?", (artist, num_weeks,)).fetchone() == None:
                    cur.execute("INSERT INTO artistWeeks (artist, num_weeks) VALUES (?,?)", (artist, num_weeks))
                    count += 1
            #  d[artist] = num_weeks #
    # return d
    conn.commit()
