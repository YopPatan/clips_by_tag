import io
import json
import urllib2
json_media = json.load(urllib2.urlopen(""))

json_new = {}
json_all = []

for video in json_media['data']:
    title = video['title']
    description = video['description']
    
    if video['custom'].get('Minuto'):
        mam = video['custom']['Minuto']
    else:
        mam = 'S/I'

    if len(video['thumbnails']) > 0:
        thumbnail = video['thumbnails'][0]['url']
    else:
        thumbnail = ''

    if len(video['meta']) > 0:
        video_mp4 = video['meta'][0]['url']
    else:
        video_mp4 = ''

    if video['protocols'].get('hls'):
        video_hls = video['protocols']['hls']
    else:
        video_hls = ''

    video_element = {'title': title, 'description': description, 'mam': mam, 'thumbnail': thumbnail, 'video_hls': video_hls, 'video_mp4': video_mp4}
    json_all.append(video_element)

    for tag in video['tags']:
#        print tag

        if not json_new.get(tag):
            json_new[tag] = []

        json_new[tag].append(video_element)

with io.open('data/data_all.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(json_all, ensure_ascii=False))

for key, data in json_new.iteritems():
    with io.open('data/data_' + key + '.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False))

#print json_new


