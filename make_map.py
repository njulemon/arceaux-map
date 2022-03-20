import webbrowser

from folium import folium, Marker, Icon
import pandas as pd


def main():
    #
    m = folium.Map(location=[50.800000, 4.416667], zoom_start=15)

    data = pd.read_csv('survey.csv')
    data['latitude'] = data['LatLng'].map(lambda x: str(x).split(';')[0])
    data['longitude'] = data['LatLng'].map(lambda x: str(x).split(';')[1])

    data['latitude_g'] = data['gracq_lat_lng'].map(
        lambda x: str(x).split(';')[0] if len(str(x).split(';')) == 2 else -1)
    data['longitude_g'] = data['gracq_lat_lng'].map(
        lambda x: str(x).split(';')[1] if len(str(x).split(';')) == 2 else -1)

    data['text'] = 'Remarque : ' + data['remark'] + '\n' + 'Nombre arceaux : ' + data['n_arceaux'].map(lambda x : str(x))
    data['id'] = data['id']

    for row in data.itertuples():
        lat = row.latitude
        lng = row.longitude
        text = row.text
        id = row.id
        done = row.done
        lat_G = row.latitude_g
        lng_G = row.longitude_g

        # if 'V' in done:
        #     Marker(icon=Icon(color="green"), location=[lat, lng], popup=f'<b>id {id}</b>').add_to(m)
        # else:
        #     Marker(icon=Icon(color="red"), location=[lat, lng], popup=f'<b>id {id}</b>{text}').add_to(m)

        if lng_G != -1:
            Marker(icon=Icon(color="blue"), location=[lat_G, lng_G], popup=f'<b>id {id}</b>').add_to(m)


    # Display the map
    m.save("map.html")
    webbrowser.open("map.html")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
