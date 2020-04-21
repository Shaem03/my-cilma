import json
import requests


class MyCilmaTv:

    def tvResult(self):
        title_list = self.split(" ")
        series_name = []
        genres = []
        tv_id = ""
        language = "NA"
        overview = "NA"
        for val in range(0, len(title_list)):
            series_name.append(title_list[val])
            if val != len(title_list) - 1:
                series_name.append("%")
        seperator = ''
        search_show = seperator.join(series_name)
        series_data = "https://api.themoviedb.org/3/search/tv?api_key=3aca899f8fe1c1ede4ec01d1acd5f0f4&query=%s" % \
                      search_show
        tv_result = requests.get(url=series_data)
        tv_content = json.loads(tv_result.content.decode('utf-8'))
        for val in tv_content['results']:
            overview = val['overview']
            tv_id = val['id']
            language = val['original_language']
            pass

        if tv_id:
            get_tv_url = "https://api.themoviedb.org/3/tv/%s?api_key=3aca899f8fe1c1ede4ec01d1acd5f0f4" % tv_id
            get_tv_data = requests.get(url=get_tv_url)
            tv_content = json.loads(get_tv_data.content.decode('utf-8'))
            for vals in tv_content['genres']:
                genres.append(vals['name'])
            pass

        tv_data = {
            "genres": genres,
            "language": language,
            "overview": overview
        }
        return tv_data
