import urllib2
import json

req = urllib2.Request("http://192.168.56.151/api/layers/?limit=3&offset=0&order_by=-date")
opener = urllib2.build_opener()
f = opener.open(req)
json_data = json.loads(f.read())
layer_count = len(json_data['objects'])
layer_list = list()
print "{}".format(layer_count)
for layer in json_data['objects']:
    featured_layer = dict()
    featured_layer['title'] = layer['title']
    featured_layer['date'] = layer['date'][:10]
    featured_layer['owner'] = layer['owner__username']
    featured_layer['thumbnail_url'] = layer['thumbnail_url']
    featured_layer['detail_url'] = layer['detail_url']
    layer_list.append(featured_layer)

layer_dict = dict()
layer_dict['layers'] = layer_list
print json.dumps(layer_dict)
