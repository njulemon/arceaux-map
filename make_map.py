import webbrowser

from folium import folium, Marker, Icon
import pandas as pd


def main():
    #
    m = folium.Map(location=[50.800000, 4.416667], zoom_start=15)

    data = pd.read_csv('data.csv')
    data['latitude'] = data['lat_lng'].map(lambda x: str(x).split(';')[0])
    data['longitude'] = data['lat_lng'].map(lambda x: str(x).split(';')[1])

    for row in data.itertuples():
        lat = row.latitude
        lng = row.longitude
        status = row.status_commune
        n_arceaux = row.n_arceaux_form
        comment = row.comment_commune
        id = row.id

        if lng != -1:
            Marker(icon=Icon(color="blue"),
                   location=[lat, lng],
                   popup=f'<b>Id : {id} </b> [{status}]<br />'
                         f'<hr>'
                         f'Commentaire commune : {comment}<br />'
                         f'<hr>'
                         f'Nombre arceaux demandés : {n_arceaux}'
                   ).add_to(m)

    # Display the map
    m.save("index.html")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
