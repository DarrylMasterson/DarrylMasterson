import sqlite3
conn = sqlite3.connect('DMARC.db')
cur = conn.cursor()

#create list to update table data
x = ['1and1.com', 'App River', 'AppTix', 'BAE Systems', 'Barracuda', 'Blue Tie', 'CA', 'Carrierzone', 'Cocentra', 'Cox Cable', 'Dream Host', 'DuoCircle', 'Exchange Defender', 'GFI Software', 'GoDaddy', 'Google', 'IPHmx.com', 'J2 Global', 'Mail Anyone', 'Mailroute', 'Microsoft Office', 'MX25.net', 'Network Solutions', 'Proofpoint', 'Rackspace', 'Reflexion', 'Securence', 'Server Data', 'Smarsh', 'Sophos', 'Spam Stops Here', 'Superpages', 'Symantec Connect', 'Trend Micro', 'X Mission', 'Yahoo Biz', 'Zoho']

#create the ESPS table
cur.execute('''CREATE TABLE [esps] (
    'espID' INTEGER,
    'esp' TEXT,
    PRIMARY KEY('espID')
)''')
conn.commit()

#load the ESPS table
for u in range(len(x)):
    cur.execute('''INSERT INTO [esps] (esp) VALUES (?)''', (x[u],))
    conn.commit()

conn.close()
