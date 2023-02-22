# Viettel-Speaker-Noti-TTS-HASS
Bước 1:

+,đi tới thư mục "custom_components" và tạo thư Mục tên "youtube_music".
  tiếp theo tải 2 file "__init__.py" và "manifest.json" vào trong thư mục "youtube_music" vừa tạo.
  
+,Tạo tiếp thư mục "www" ngang hàng với file "configuration.yaml". 
  tiếp đến vào thư mục "www" vừa tạo, tạo tiếp một thư mục nữa có tên là: "youtube_music"

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




