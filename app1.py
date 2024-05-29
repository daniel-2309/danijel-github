import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy


volcano_df = pd.read_csv('data/volcano_ds_pop.csv')

# Load the geoJSON file
with open('data/countries.geojson', 'r') as file:
    volcano_geojson = json.load(file)

# Add title and header
st.title("Exercise: Introduction to Streamline")
st.header("World Volcanoes History")

st.markdown(
    "**Volcanoes**, the spectacular and powerful manifestations of Earth's dynamic interior, are scattered across the globe. "
    "These geological formations are vents in the Earth's crust through which molten rock, debris, and gases from the planet's interior are expelled. "
    "They are primarily found along tectonic plate boundaries and can be categorized as active, dormant, or extinct based on their eruption history.\n\n"
    "**Active Volcanic Regions:**\n"
    "**1. The Pacific Ring of Fire:** This is the most seismically active region in the world, stretching around the Pacific Ocean. "
    "Countries like Japan, Indonesia, and the United States (particularly Alaska and Hawaii) have numerous active volcanoes.\n"
    "**2. The Mediterranean Belt:** Known for its historical eruptions, this area affects nations like Italy (Mount Vesuvius and Mount Etna) and Greece.\n"
    "**3. The East African Rift:** This region includes multiple volcanoes in Ethiopia and the famously active Mount Nyiragongo in the Democratic Republic of Congo.\n\n"
    "**Important Information About Volcanoes:**\n"
    "- **Eruption Types:** Volcanoes exhibit various eruption styles, from explosive ash eruptions, as seen with Mount Saint Helens in 1980, "
    "to effusive lava flows, typical of Hawaii's Kilauea.\n"
    "- **Volcanic Hazards:** These include lava flows, ash clouds, pyroclastic flows, and volcanic gases that can pose significant risks to life and property.\n"
    "- **Monitoring and Prediction:** Through seismic activity, gas emissions, ground deformation, and thermal and satellite imagery, "
    "scientists can often predict eruptions and mitigate their impact.\n\n"
    "Volcanoes play crucial roles in shaping Earth's landscape, affecting its atmosphere, and fostering rich ecosystems. "
    "They also pose significant hazards, necessitating ongoing research and monitoring to protect communities living in their shadows.",
    unsafe_allow_html=False
)





fig = px.scatter_mapbox(volcano_df,
                        lat='Latitude',
                        lon='Longitude',
                        color='Type',
                        hover_name='Volcano Name',
                        hover_data=['Type', 'Country', 'Region', 'Status'],
                        zoom=1.5,
                        title="<b>'Volcanoes of the World'</b>",
                        color_discrete_sequence=px.colors.qualitative.Plotly)

fig.update_layout(
                    title={"font_size":20,
                         "xanchor":"center", "x":0.38,
                        "yanchor":"bottom", "y":0.95},
                    title_font=dict(size=24, color='Black', family='Arial, sans-serif'),
                    height=1100,
                    width=1300,
                    autosize=True,
                    hovermode='closest',
                    mapbox=dict(
                        style='open-street-map'
                    ),
                    legend_title_text='Volcano Type'
)

## fig.show()

st.plotly_chart(fig)