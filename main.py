from instabot import Bot
import os
import glob

MEDIA_FOLDER = 'media/'


USERNAME = 'your_username'
PASSWORD = 'your_password'

def upload_media():
    bot = Bot()
    bot.login(username=USERNAME, password=PASSWORD)

    media_files = glob.glob(os.path.join(MEDIA_FOLDER, '*'))
    for media in media_files:
        if media.endswith(('jpg', 'jpeg', 'png')):
            bot. upload_photo(media, caption="Your caption here")
        elif media.endswith(('mp4', 'mov')):
            bot.upload_video(media, caption="Your caption here")

    bot.logout()

if __name__ == '__main__':
    upload_media()
