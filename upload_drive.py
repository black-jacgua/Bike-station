from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LoadCredentialsFile("credentials.json")

if gauth.credentials is None:
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    gauth.Refresh()
else:
    gauth.Authorize()

gauth.SaveCredentialsFile("credentials.json")
drive = GoogleDrive(gauth)

file_to_update = drive.CreateFile({'id': '1IHYSaJTBeGQC3Q7FLbiGTeUnIdX4G6rp'})

file_to_update.SetContentFile('./live/bike_frenquency_station.csv')
file_to_update.Upload()
