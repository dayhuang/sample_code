

def audio_dl(yid):
    # download yid youtube audio file, and store in
    # in local directory as 't%yid.mp3' file

    out_path = 'a' + yid + '.mp3'
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': out_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ret = ydl.download(['http://www.youtube.com/watch?v=' + yid])
    return out_path


def video_dl(yid):
    out_path = "v" + yid + ".mp4"
    ydl_opts = {
        'videoformat' : "mp4",
        'outtmpl': out_path,
        'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # one of avi, flv, mkv, mp4, ogg, webm
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ret = ydl.download(['http://www.youtube.com/watch?v=' + yid])
    return out_path



