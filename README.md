# Viettel-Speaker-Noti-TTS-HASS
Bước 1:

+,đi tới thư mục "custom_components" và tạo thư Mục tên "youtube_music".
  tiếp theo tải 2 file "__init__.py" và "manifest.json" vào trong thư mục "youtube_music" vừa tạo.
  
+,Tạo tiếp thư mục "www" ngang hàng với file "configuration.yaml". 
  tiếp đến vào thư mục "www" vừa tạo, tạo tiếp một thư mục nữa có tên là: "youtube_music"

#tạo xong check config rồi khởi động lại Home Assistant


#Cấu Hình trong file configuration.yaml theo bên dưới đây:

      youtube_music:


#cấu hình input text để nhập văn bản thành giọng nói 

      input_text:
        viettell_tts_text:
          name: "Nhập Nội Dung"
 
#Cấu hình trong file script.yaml

    youtube_music_cast:
      sequence:  
      - service: youtube_music.cast
        data_template:
          entity_id: media_player.googlehomemini    
          message: '{{ states(''input_text.viettell_tts_text'') }}'
 
#Cấu hình Xong check config rồi khởi động lại home assistant




