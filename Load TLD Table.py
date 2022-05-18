import sqlite3
conn = sqlite3.connect('DMARC.db')
cur = conn.cursor()

#create list to update table data
x = ['aero', 'agency', 'ai', 'bank', 'biz', 'bz', 'ca', 'church', 'cloud', 'co', 'com', 'coop', 'financial', 'health', 'info', 'io', 'it', 'md', 'me', 'net', 'org', 'partners', 'solutions', 'space', 'tv', 'us', 'ws']

for u in range(len(x)):
    cur.execute('''INSERT INTO [top level domains] (tld) VALUES (?)''', (x[u],))
    conn.commit()

conn.close()
