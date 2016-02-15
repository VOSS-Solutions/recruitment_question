#Recruitment challenge

# uncnomment below and figured out what must be imported
#import

#bottom 2 stringss are encoded, find out how
search = "KCg/Olx4MkYpfCg/OmNhcmVlcnMpfCg/Oltjd3Zvc2lvbmx0bXUtXSl8KD86XC4pKQ=="
#below string has been formatted for PEP8
text = "dmltIG9wZW5zb3VyY2Ugc29mdHdhcmUgc2VjdXJlIC0gc29mdC1waG9uZSBvcGVyYXRpb25z\
        IGxpbnV4IHVuaWZpZWQgcHl0aG9uIGlwLXRlbGVwaG9ueSBvYmplY3RzIG5naW54IGpzb24gM\
        TI3LjAuMC4xIGNoYWxsZW5nZXMgb3Bwb3J0dW5pdGllcyBtdWx0aS1kaXNjaXBsaW5hcnkgLyB\
        jYXJlZXJz"

url = ''

#fix the below variables by decoding 2^5
decode_search = search
decode_text = text

r = re.compile(decode_search)

find = decode_text.split(" ")

for instance in find:
    result = re.search(r,instance)
    try:
        #print result.groups()[0]
        url += result.groups()[0]
    except Exception:
        print "False, decode must have failed"

print "Search:\n{}".format(decode_search)
print "Text:\n{}".format(decode_text)

hash = hashlib.md5()
hash.update(url)


result = "\nIf you have fixed this correctly then email:\nchristo.goosen@{}\
 the hash {} or visit  \
www.{} \n".format(re.sub(r'\x2f\x63\x61\x72\x65\x65\x72\x73', '',url),hash.hexdigest(),url)
print result