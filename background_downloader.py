import urllib, json, urlparse, os

urllib.urlretrieve ("https://clients3.google.com/cast/chromecast/home/v/c9541b08", "download.html")

parseme = open("download.html")

art_json = ""

for line in parseme:
    sposition = line.find("JSON.parse(")
    if sposition > 0:
        eposition = line.find("));</script>")
        if eposition > 0:
            art_json = line[sposition + 12 : eposition - 1]
            break

art_array = json.loads(art_json.decode('string_escape'))

for x in range(0, len(art_array[1])):
    filename = urlparse.urlsplit(art_array[1][x][1]).path.split("/")[-1]
    if not os.path.isfile(filename):
        print "Downloading " + filename
        urllib.urlretrieve(art_array[1][x][1], filename)