from nathanmusic.core.bot import Anony
from nathanmusic.core.dir import dirr
from nathanmusic.core.git import git
from nathanmusic.core.userbot import Userbot
from nathanmusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Anony()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
