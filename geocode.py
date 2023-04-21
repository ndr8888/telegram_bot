def api_request(response):
    toponym = response["response"]["GeoObjectCollection"][
        "featureMember"][0]["GeoObject"]
    rect = toponym['boundedBy']['Envelope']
    delta = min([abs(float(rect['lowerCorner'].split()[0]) - float(rect['upperCorner'].split()[0])),
                 abs(float(rect['lowerCorner'].split()[1]) - float(
                     rect['upperCorner'].split()[1]))]) / 2
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    ll, spn = ",".join([toponym_longitude, toponym_lattitude]), ",".join([str(delta), str(delta)])
    static_api_request = f"http://static-maps.yandex.ru/1.x/?ll={ll}&spn={spn}&l=map&pt={','.join([toponym_longitude, toponym_lattitude]) + ',pm2rdl'}"
    return static_api_request
