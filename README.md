# tweet-automation

## Steps

1. Install python from https://www.python.org/ftp/python/3.10.4/python-3.10.4-amd64.exe
2. Install virtualenv
  ```bash
  pip install virtualenv
  ```
3. Create and enter virtualenv
  ```bash
  virtualenv venv
  .\venv\Scripts\activate
  ```
4. Install requirements
  ```bash
  pip install -r requirements.txt
  ```
5. Add required media in media/ and required content in content.json in format:
  ```json
  [
    {
      "msg": "This is my first tweet",
      "media": "imageVideoNameInMedia.png"
    },
      "msg":"नमस्ते दुनिया",
      "media":""
  ]
  ```
6. Run the main file
  ```bash
  python tweepy-v2-upload.py
  ```
