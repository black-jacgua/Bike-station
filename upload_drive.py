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

file_to_update = drive.CreateFile({'id': 'ID_DU_FICHIER_SUR_DRIVE'})
file_to_update.SetContentFile('path/local/du/fichier.txt')
file_to_update.Upload()
