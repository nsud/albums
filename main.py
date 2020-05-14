from bottle import route
from bottle import run
from bottle import request
from bottle import HTTPError

from album import connect, find_art, find_alb, Album, insert


@route("/albums/<artist>")
def albums(artist):
    albums_list = find_art(artist)

    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        count = len(albums_list)
        result = f"Найдено альбомов: {count}\nСписок альбомов: \n {artist}\n"
        result += "\n".join(album_names)
    return result


@route("/albums", method="POST")
def add_album():
    try:
        year = int(request.forms.get("year"))
    except:
        return HTTPError(409, "Год введен неверно")
    data = Album(
        artist = request.forms.get("artist"),
        genre = request.forms.get("genre"),
        album = request.forms.get("album"),
        year = year
    )

    mes = find_alb(request.forms.get("album"))
    if mes == "OK":
        new_mes = insert(data)
        return new_mes
    else:
        result = HTTPError(409, mes)
        return result


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)