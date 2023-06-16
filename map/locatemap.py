import folium
import geocoder
import csv
import pandas as pd
from django.http import HttpResponse

def locate_map1(para, val):
    #create a folium map 
    f = folium.Figure(height=516, width=934)
    #setting the location of a map for 'India'
    m = folium.Map(location=[24.5362, 81.3037], zoom_start=7).add_to(f)

    #adding different layers in a map
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
    folium.raster_layers.TileLayer('CartoDB Positron').add_to(m)
    folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(m)
    folium.LayerControl().add_to(m)
    
    #reading the location csv file to grap the lat and lng of the locations for a map
    df8=pd.read_csv("static/RuntimeS/Runtime/Location's.csv")
    d1=df8.to_dict("records")
    for i in range(0,92):
        df7=pd.read_csv("static/RuntimeS/Runtime/{}/Location{}/Data.csv".format(para,str(i+1)))
        d=df7.to_dict("records")
        
        #create a popup for the markers showed in a map
        pp= folium.Html("<strong><h5>'" + "'Location {} : ".format(str(i+1)) + d1[i]['Name Of The River'] +" '" + 
            "'</h5></strong><hr><h5 style='text-decoration : underline;'>Current Water Parameter Value :- </h5><h5>" + para + " : " + 
            str(d[-1][para]) + "</h5><h5>Date : " + str(d[-1]['Date']) + "</h5><h5>Time : " + str(d[-1]['Time']) + 
            "</h5><a href='#'>To Vizualize graph go to Services Page</a>'", script=True)
        popup = folium.Popup(pp, max_width=2650)

        #adding a marker for specific location's with a popup
        folium.Marker([d1[i]['Latitude'], d1[i]['Longitude']], popup= popup,
            icon=folium.Icon(icon= "tint", color= "red")).add_to(m)
        #create a link to represent a map in index1.html page
        #folium.Marker([lat, lng], popup= country).add_to(m)
    m = m._repr_html_()
    cont = {'m' : m, 'nm' : para, 'nm2' : val}
    return cont

def locate_map2(para, val):
    #create a folium map 
    f = folium.Figure(height=516, width=934)
    #setting the location of a map for 'India'
    m = folium.Map(location=[24.5362, 81.3037], zoom_start=7).add_to(f)

    #adding different layers in a map
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
    folium.raster_layers.TileLayer('CartoDB Positron').add_to(m)
    folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(m)
    folium.LayerControl().add_to(m)
    
    #reading the location csv file to grap the lat and lng of the locations for a map
    df8=pd.read_csv("static/RuntimeS/Runtime2/Location's.csv")
    d1=df8.to_dict("records")
    for i in range(0,92):
        df7=pd.read_csv("static/RuntimeS/Runtime2/{}/Location{}/Data.csv".format(para,str(i+1)))
        d=df7.to_dict("records")
        
        #create a popup for the markers showed in a map
        pp= folium.Html("<strong><h5>'" + "'Location {} : ".format(str(i+1)) + d1[i]['Name Of The River'] +" '" + 
            "'</h5></strong><hr><h5 style='text-decoration : underline;'>Current Water Parameter Value :- </h5><h5>" + para + " : " + 
            str(d[-1][para]) + "</h5><h5>Date : " + str(d[-1]['Date']) + "</h5><h5>Time : " + str(d[-1]['Time']) + 
            "</h5><a href='#'>To Vizualize graph go to Services Page</a>'", script=True)
        popup = folium.Popup(pp, max_width=2650)

        #adding a marker for specific location's with a popup
        folium.Marker([d1[i]['Latitude'], d1[i]['Longitude']], popup= popup,
            icon=folium.Icon(icon= "tint", color= "red")).add_to(m)
        #create a link to represent a map in index1.html page
        #folium.Marker([lat, lng], popup= country).add_to(m)
    m = m._repr_html_()
    cont = {'m' : m, 'nm' : para, 'nm2' : val}
    return cont

def locate_map3(para, val):
    #create a folium map 
    f = folium.Figure(height=516, width=934)
    #setting the location of a map for 'India'
    m = folium.Map(location=[24.5362, 81.3037], zoom_start=7).add_to(f)

    #adding different layers in a map
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
    folium.raster_layers.TileLayer('CartoDB Positron').add_to(m)
    folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(m)
    folium.LayerControl().add_to(m)

    #reading the location csv file to grap the lat and lng of the locations for a map
    df8=pd.read_csv("static/RuntimeS/Runtime3/Location's.csv")
    d1=df8.to_dict("records")
    for i in range(0,92):
        df7=pd.read_csv("static/RuntimeS/Runtime3/{}/Location{}/Data.csv".format(para,str(i+1)))
        d=df7.to_dict("records")
        
        #create a popup for the markers showed in a map
        pp= folium.Html("<strong><h5>'" + "'Location {} : ".format(str(i+1)) + d1[i]['Name Of The River'] +" '" + 
            "'</h5></strong><hr><h5 style='text-decoration : underline;'>Current Water Parameter Value :- </h5><h5>" + para + " : " + 
            str(d[-1][para]) + "</h5><h5>Date : " + str(d[-1]['Date']) + "</h5><h5>Time : " + str(d[-1]['Time']) + 
            "</h5><a href='#'>To Vizualize graph go to Services Page</a>'", script=True)
        popup = folium.Popup(pp, max_width=2650)

        #adding a marker for specific location's with a popup
        folium.Marker([d1[i]['Latitude'], d1[i]['Longitude']], popup= popup,
            icon=folium.Icon(icon= "tint", color= "red")).add_to(m)
        #create a link to represent a map in index1.html page
        #folium.Marker([lat, lng], popup= country).add_to(m)
    m = m._repr_html_()
    cont = {'m' : m, 'nm' : para, 'nm2' : val}
    return cont

def locate_map4(para, val):
    #create a folium map 
    f = folium.Figure(height=516, width=934)
    #setting the location of a map for 'India'
    m = folium.Map(location=[24.5362, 81.3037], zoom_start=6).add_to(f)

    #adding different layers in a map
    folium.raster_layers.TileLayer('Stamen Terrain').add_to(m)
    folium.raster_layers.TileLayer('Stamen Toner').add_to(m)
    folium.raster_layers.TileLayer('Stamen Watercolor').add_to(m)
    folium.raster_layers.TileLayer('CartoDB Positron').add_to(m)
    folium.raster_layers.TileLayer('CartoDB Dark_Matter').add_to(m)
    folium.LayerControl().add_to(m)

    npara = para.replace("/","_")     
    #reading the location csv file to grap the lat and lng of the locations for a map
    df8=pd.read_csv("static/RuntimeS1/Location's.csv")
    d1=df8.to_dict("records")
    for i in range(0,34):
        try:
            df7=pd.read_csv("static/RuntimeS1/{}/Location{}/Data.csv".format(npara,str(i+1)))
            d=df7.to_dict("records")
                    
            #create a popup for the markers showed in a map
            pp= folium.Html("<strong><h5>'"+ "'Location {} : ".format(str(i+1)) + d1[i]['Location'] +" '" + 
                "'</h5></strong><hr><h5 style='text-decoration : underline;'>Current Water Parameter Value :- </h5><h5>" + para + " : " + 
                str(d[-1][para]) + "</h5><h5>Date : " + str(d[-1]['Date']) + "</h5><h5>Time : " + str(d[-1]['Time']) + 
                "</h5><a href='#'>To Vizualize graph go to Services Page</a>", script=True)
            popup = folium.Popup(pp, max_width=2650)

            #adding a marker for specific location's with a popup
            folium.Marker([d1[i]['Latitude'], d1[i]['Longitude']], popup= popup,
                icon=folium.Icon(icon = "tint", color= "red")).add_to(m)
        except:
            pass
    m = m._repr_html_()
    cont = {'m' : m, 'nm' : para, 'nm2' : val}
    return cont