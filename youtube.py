import youtube_dl

""" 
    Para descargar
    
    with youtube_dl.YoutubeDL() as ydl:
        ydl.download(['https://www.youtube.com/watch?v=yY8UIQRNM7M'])
"""
opcionMusica = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def DescargarAudio(url):
    with youtube_dl.YoutubeDL(opcionMusica) as ydl:
        ydl.download([url])


def DescargarVideo(lista):
    for i in lista:
        with youtube_dl.YoutubeDL() as ydl:
            ydl.download([i])
