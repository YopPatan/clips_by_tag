import io
import json
import urllib2
import sys

media_ids = []
tags_permitidos = []


try:
    json_conf = json.load(urllib2.urlopen('http://estaticos.tvn.cl/skins/copa_confederaciones/js/config.json'))
except Exception as inst:
    print "error al leer archivo de config"
    sys.exit()

if (json_conf.get("media_id")):
    media_ids = json_conf["media_id"]
else:
    sys.exit()

if (json_conf.get("tags_enabled")):
    tags_permitidos = json_conf["tags_enabled"]

for media_id in media_ids:
    json_new = {}
    json_all = []
    try:
        json_media = json.load(urllib2.urlopen('https://api.streammanager.co/api/media?token=f5c4d4c019297f434f10c7a7bd87fe30&category_id=' + media_id))
    except Exception as inst:
        print "error al leer archivo con videos"
        sys.exit()

    for video in json_media['data']:
        try:

            id = video['_id']
            title = video['title']
            description = video['description']

            if video.get('slug'):
                slug = video['slug']
            else:
                slug = ''

            if video.get('custom'):
                if video['custom'].get('Minuto'):
                    mam = video['custom']['Minuto']
                else:
                    mam = ''
            else:
                mam = ''

            if video.get('thumbnails'):
            	if len(video['thumbnails']) > 0:
                	thumbnail = video['thumbnails'][0]['url']
                	for img in video['thumbnails']:
                		if (img['is_default']) and (img['size'] == '480'):
                			thumbnail = img['url']
            	else:
                	thumbnail = ''
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

            video_element = {
                'id': id,
                'slug': slug,
                'title': title,
                'description': description,
                'mam': mam,
                'thumbnail': thumbnail,
                'video_hls': video_hls,
                'video_mp4': video_mp4
            }

            json_all.append(video_element)

            if video.get("tags"):

                for tag in video['tags']:

                    if not json_new.get(tag):
                        json_new[tag] = []

                    json_new[tag].append(video_element)
        except Exception as inst:
            print inst

    with io.open('data/data_' + media_id + '_all.json', 'w', encoding='utf-8') as f:
        f.write(unicode(json.dumps(json_all, ensure_ascii=False)))

    for key, data in json_new.iteritems():
        if key in tags_permitidos:
            with io.open('data/data_' + media_id + '_' + key + '.json', 'w', encoding='utf-8') as f:
                f.write(json.dumps(data, ensure_ascii=False))

#print json_new


