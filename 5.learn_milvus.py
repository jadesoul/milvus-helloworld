from pymilvus import (
    connections,
    utility,
    FieldSchema, CollectionSchema, DataType,
    Collection,
)


fmt = "\n=== {:30} ===\n"
search_latency_fmt = "search latency = {:.4f}s"

print(fmt.format("start connecting to Milvus"))
connections.connect("default", host="localhost", port="19530")

from pymilvus import Collection
collection = Collection("hello_milvus")      # Get an existing collection.

if not collection.has_partition("novel"):
    collection.create_partition("novel")
    print('created collection')
else:
    print('already has the collection')



print(collection.partitions)

# collection.drop_partition("novel")

if collection.has_index():
    collection.drop_index()
    print('dropped index')
else:
    print('has no index')


connections.disconnect('default')


# More info
# https://github.com/milvus-io/milvus
# https://github.com/milvus-io/bootcamp/blob/master/solutions/text_search_engine/text_search_engine.ipynb
# https://github.com/zilliztech/attu/blob/main/doc/zh-CN/attu_collection.md
# https://github.com/zilliztech/attu