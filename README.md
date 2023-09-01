# Youtube-Cast-MP3-Hass
Nếu thiếu thư viện:
dùng lệnh: "find / -name youtube.py" để tìm kiếm xem có thư viện youtube_dl hay không, nếu không có thì tải thư mục thưu viện youtube_dl trên git này lên theo đường dẫn vừa dùng lệnh trên để tìm
ví dụ đường dẫn thư mục trên docker: (Mỗi thiết bị sẽ có đường dẫn khác nhau)
/var/lib/docker/overlay2/81b5134b03a172a61f0f269b70be1d65be6531e90b0dc61bf915a8230e5559ec/merged/usr/local/lib/python3.11/site-packages
bê nguyên thư mục youtube_dl coppy vào trong thư mục site-packages trên docker



Bước 1:

+,đi tới thư mục "custom_components" và tạo thư Mục tên "youtube_music".
  tiếp theo tải 2 file "__init__.py" và "manifest.json" vào trong thư mục "youtube_music" vừa tạo.
  

#tạo xong check config rồi khởi động lại Home Assistant


#Cấu Hình trong file configuration.yaml theo bên dưới đây:

      youtube_music:


#cấu hình input text để nhập Link youtube

      input_text:
        youtube_music_casttt:
          name: "Nhập Link/Url Youtube"
 
#Cấu hình trong file script.yaml

    youtube_music_cast:
      sequence:  
      - service: youtube_music.cast
        data_template:
          entity_id: media_player.googlehomemini    
          message: '{{ states(''input_text.youtube_music_casttt'') }}'
 
#Cấu hình Xong check config rồi khởi động lại home assistant


#Cấu Hình loveLace:

    type: custom:vertical-stack-in-card
    cards:
      - type: entities
        entities:
          - entity: input_text.youtube_music_casttt
            icon: mdi:text-box-edit
            name: 'Nhập Link mp3 Youtube:'
          - entity: media_player.googlehomemini
            artwork: cover
            type: custom:mini-media-player
            icon: mdi:google-assistant
            name: Google Home Mini
            source: icon
            info: short
            hide:
              icon_state: false
              power_state: false
              runtime: false
              source: false
              volume: false
            shortcuts:
              columns: 1
              buttons:
                - icon: mdi:youtube
                  type: script
                  id: script.youtube_music_cast
                  name: Youtube
  
