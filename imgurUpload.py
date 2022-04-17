from os import path
from imgur_python import Imgur
from cred import imgurclientid, imgurclientsecret

def upload_image(img_path):
    try:
        file = path.realpath('./media/'+img_path)
        title = 'Untitled'
        description = 'Image description'
        album = None
        disable_audio = 0

        imgur_client = Imgur({'client_id': imgurclientid, 'access_token':imgurclientsecret})
        # imgur_client = Imgur()
        response = imgur_client.image_upload(file, title, description, album, disable_audio)
        url = "https://imgur.com/"+response['response']['data']["id"]
        return url
    except Exception as e:
        print(e)
        return "https://imgur.com/gallery/rQ4ofyB"


upload_image("catvideo.mp4")