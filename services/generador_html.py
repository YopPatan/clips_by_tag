import io
import json
import urllib2
import sys

try:
    json_conf = json.load(urllib2.urlopen('http://localhost/clips_by_tag/services/config/config_html_alemania_camerun.json'))
except Exception as inst:
    print "error al leer archivo de config"
    sys.exit()

for data in json_conf["data"]:
    with open ("../html/principal.html", "r") as myfile:
        file_html = myfile.read()

    if data["tag"]=='all':
        fullhtml = json_conf["html"]

        with open ("../html/solobody.html", "r") as myfile:
            file_solohtml = myfile.read()

        file_solohtml = file_solohtml.replace('INFO_CSSVERSION', json_conf["css_version"])
        file_solohtml = file_solohtml.replace('INFO_HTML', json_conf["html"])
        file_solohtml = file_solohtml.replace('INFO_LUGAR', json_conf["lugar"])
        file_solohtml = file_solohtml.replace('INFO_MEDIAID', json_conf["media_id"])

        file_solohtml = file_solohtml.replace('INFO_TITULO', data["titulo"])
        file_solohtml = file_solohtml.replace('INFO_DESCRIPCION', data["descripcion"])
        file_solohtml = file_solohtml.replace('INFO_IMAGEN', data["imagen"])
        file_solohtml = file_solohtml.replace('INFO_TAG', data["tag"])
        file_solohtml = file_solohtml.replace('INFO_FULLHTML', 'solobody_' + json_conf["html"])

        with io.open('data_html/solobody_' + json_conf["html"] + '.html', 'w', encoding='utf-8') as f:
            f.write(file_solohtml)
            f.close()
            print 'http://estaticos.tvn.cl/skins/copa_confederaciones/solobody_' + json_conf["html"] + '.html'

    else:
        fullhtml = json_conf["html"] + '_' + data["tag"]

    file_html = file_html.replace('INFO_CSSVERSION', json_conf["css_version"])
    file_html = file_html.replace('INFO_HTML', json_conf["html"])
    file_html = file_html.replace('INFO_LUGAR', json_conf["lugar"])
    file_html = file_html.replace('INFO_MEDIAID', json_conf["media_id"])

    file_html = file_html.replace('INFO_TITULO', data["titulo"])
    file_html = file_html.replace('INFO_DESCRIPCION', data["descripcion"])
    file_html = file_html.replace('INFO_IMAGEN', data["imagen"])
    file_html = file_html.replace('INFO_TAG', data["tag"])
    file_html = file_html.replace('INFO_FULLHTML', fullhtml)

    with io.open('data_html/' + fullhtml + '.html', 'w', encoding='utf-8') as f:
        f.write(file_html)
        f.close()
        print 'http://estaticos.tvn.cl/skins/copa_confederaciones/' + fullhtml + '.html'