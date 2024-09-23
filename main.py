from fastapi import FastAPI, UploadFile, File
import pysftp


app = FastAPI()

@app.post("/upload")
async def upload_csv(file: UploadFile = File(...)):
    if file.filename.endswith('.csv'):
        #read csv data
        contents = await file.read()
        #save csv in sftp azure
        # Dirección o IP del servidor SFTP.
        host = "devanalytics.sftpchallenge@devanalytics.blob.core.windows.net"
        # Usuario y contraseña.
        username = "sftpchallenge"
        password = "Uerqqtuq6t+wRkqTKMY7/zx38C"

        # Realizar la conexión.
        with pysftp.Connection(host, username=username, password=password) as sftp:
            with sftp.cd("/datalake/sftp_challenge/"):
                sftp.put(contents)
        return file.filename

    else:
        return {'error: Only csv files are allowed'}
