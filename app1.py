import plotly.graph_objects as go
import plotly.express as px
import plotly.io as pio
#pio.renderers.default = 'colab'   # try changing this in case your plots aren't shown
import pandas as pd
import json

internet_access_perc = pd.read_csv('./data/share-of-individuals-using-the-internet.csv')


countries = []
most_recent_year = []

for grp, df in df.groupby("Code"):
    countries.append(grp)
    most_recent_year.append(df["Year"].max())
    
recent_years_df = pd.DataFrame({"Code": countries, "most_recent_year": most_recent_year})

recent_perc = pd.merge(recent_years_df, internet_access_perc)
recent_perc = recent_perc[recent_perc["Year"]==recent_perc["most_recent_year"]]


# Create the map, add hovertips, title, labels, styling, etc.

fig = px.choropleth(
    recent_perc,
    locations="Code", 
    color="Individuals using the Internet (% of population)",

    width=950,
    height=450,
    labels={"Individuals using the Internet (% of population)":"% of Population",
           "most_recent_year":"Year"},
    hover_name="Entity",
    hover_data={"Code": False,
                "most_recent_year":True,
                "Individuals using the Internet (% of population)":':.2f'},
    title="<b>Percentage of Population Using the Internet</b>",
    color_continuous_scale="Viridis",
    
)

fig.update_traces(marker={"opacity":0.7})

fig.update_layout(margin={"r":20,"t":35,"l":0,"b":0},
                  font_family="Rockwell",
                  hoverlabel={"bgcolor":"white", 
                              "font_size":12,
                             "font_family":"Rockwell"},
                  title={"font_size":20,
                        "xanchor":"left", "x":0,
                        "yanchor":"top"},
                  geo={"resolution":50,
                      "showlakes":True, "lakecolor":"lightblue", 
                       "showocean":True, "oceancolor":"aliceblue"
                      }
                 )

fig.show()


