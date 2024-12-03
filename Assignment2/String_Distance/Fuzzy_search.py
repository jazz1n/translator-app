from datetime import datetime
from elasticsearch import Elasticsearch

client = Elasticsearch("https://4009971ded05486ba7ec30b5af64978f.us-central1.gcp.cloud.es.io:443", api_key="SGJscDI1RUIzS01BMEl2YzNkYkI6OTItZWpqR3pTRnUzb1lEY2g5S25WQQ==")

doc = {
    "author": "kimchy",
    "text": "Elasticsearch: cool. bonsai cool.",
    "timestamp": datetime.now(),
}

doc2 = {
    "author": "Bernard",
    "text": "Rahnama BootCamp is Cool.",
    "timestamp": datetime.now(),
}

resp = client.index(index="test-index", id=1, document=doc)
print(resp["result"])
resp = client.index(index="test-index", id=2, document=doc2)
print(resp["result"])

resp = client.get(index="test-index", id=1)
print(resp["_source"])
resp = client.get(index="test-index", id=2)
print(resp["_source"])

client.indices.refresh(index="test-index")


#Normal Search
resp = client.search(index="test-index", query={"match_all": {}})
print("Got {} hits:".format(resp["hits"]["total"]["value"]))
for hit in resp["hits"]["hits"]:
    print("{timestamp} {author} {text}".format(**hit["_source"]))


# Fuzzy Search
query = {
    "query": {
        "fuzzy": {
            "text": {
                "value": "cool",
                "fuzziness": "AUTO",          # فازی بودن خودکار
                "prefix_length": 1,           # تعداد کاراکترهایی که باید بدون تغییر در نظر گرفته شوند
                "max_expansions": 50,         # حداکثر تعداد کلماتی که می‌توانند گسترش یابند
                "transpositions": True,       # در نظر گرفتن جابجایی‌های دو کاراکتر
                "boost": 1.0,                 # نمره‌دهی جستجو
                "rewrite": "constant_score"   # استراتژی بازنویسی
            }
        }
    }
}


resp = client.search(index="test-index", body=query)
print("Got {} hits:".format(resp["hits"]["total"]["value"]))
for hit in resp["hits"]["hits"]:
    print("{timestamp} {author} {text}".format(**hit["_source"]))
