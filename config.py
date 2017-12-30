from tinydb import TinyDB, Query
import datetime
current_user = {
    'is_authenticated': False
}

iran_delta = datetime.timedelta(hours=3, minutes=30)

users = TinyDB('static/db/users.json')
csvs = TinyDB('static/db/csvs.json')
