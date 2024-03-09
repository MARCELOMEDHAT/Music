from AnonXMusic.core.bot import Anony
from AnonXMusic.core.dir import dirr
from pyromod import listen
from AnonXMusic.core.userbot import Userbot
from AnonXMusic.misc import dbb, heroku

from .logging import LOGGER


dirr()
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