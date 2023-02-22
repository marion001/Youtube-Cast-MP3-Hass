#encoding: utf-8
#Code by: Vũ Tuyển
#Mail: tuyenbau1997@gmail.com
from __future__ import unicode_literals 
import youtube_dl
import re
DOMAIN = 'youtube_music'
CFG_ENTITY_ID = 'entity_id'
CFG_MESSAGE = 'message'
def setup(hass, config):
    def xuly_dulieu(call):
        #Khai Báo Biến
        entity_idid = call.data.get(CFG_ENTITY_ID)
        message = call.data.get(CFG_MESSAGE)
        #Lọc Lấy ID của link
        match = re.search(r'(?<=v=)[\w-]+', message)
        if match:
            video_id = "https://www.youtube.com/watch?v="+match.group(0)
            #print(video_id)
        else:
            video_id = message
        #Lấy dữ liệu link mp3
        ydl_opts = {
            'format': 'bestaudio',
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_id, download=False)
            show_link = info['formats'][0]['url']
        #Hass Send Data
        Data_Hass = {'entity_id': entity_idid, 'media_content_id': show_link, 'media_content_type': 'audio/mp3'}
        hass.services.call('media_player', 'play_media', Data_Hass)
    hass.services.register(DOMAIN, 'cast', xuly_dulieu)
    return True
