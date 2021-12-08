# required libraries
from dash import *  # Used dash as it comprises of power of flask for running the server as well as power of plotly and react for data visualisation
import pandas as pd
import numpy as np
import plotly.express as px

# reading data
data = pd.read_csv("LoanPricing.csv")

# for pie chart
count = data['Marital_Status_Desc'].value_counts()
names = data['Marital_Status_Desc'].unique()

# to make dashboard look good thru CSS
external_stylesheets = [
    {
        "href": "https://fonts.googleapis.com/css2?"
                "family=Lato:wght@400;700&display=swap",
        "rel": "stylesheet",
    },
]

# initialising app
app = dash.Dash(__name__)
app.title = 'Data Visualisation: Dashboard'
# in this we are basically using html div & paragraph tags to create the layout of the app
app.layout = html.Div(
    children=[
        # html paragraph tag
        html.Pre(children="Data Science Lab Evaluation, 2021-22ODDSEM             by Bhavya Tyagi, 102097014, 3CSE2",
                 className="header-text"),
        html.P(children=" Submitted to:- Dr. Geeta Kasana, CSED, TIET,Patiala",
               className="header-text-right"),
        # html div tag
        # This div is for the header
        html.Div(
            children=[
                html.P(children="🚗💵", className="header-emoji"),
                html.H1(children="Vehicle Loan Analytics",
                        className="header-title",),
                html.P(
                    children="Analyze the behavior of Loan tenures and Vehicle Cost amongst different gender & age groups",
                    className="header-description",
                ),
            ],
            className="header",
        ),
        # this div is for the input
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Gender",
                                 className="menu-title"),
                        dcc.Dropdown(
                            id="gender-filter",
                            options=[
                                {"label": Gender_Desc, "value": Gender_Desc}
                                for Gender_Desc in (data.Gender_Desc.unique())
                            ],
                            value="Female",
                            clearable=False,
                            className="dropdown",
                        ),
                    ]
                ),
            ],
            className="menu",
        ),
        # this div is for the output i.e. the graphs
        html.Div(
            children=[

                html.Div(
                    children=dcc.Graph(
                        id="loan_term", config={"displayModeBar": False},
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="pie_chart", config={"displayModeBar": False},
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="scatter_chart", config={"displayModeBar": False},
                    ),
                    className="card",
                ),
                html.Div(
                    children=dcc.Graph(
                        id="loan_term_2", config={"displayModeBar": False},
                    ),
                    className="card",
                ),
            ],
            className="wrapper",
        ),
        # this div is for the conclusions
        html.Div(
            children=[
                html.Div(
                    children=[
                        html.Div(children="Some Conclusions through the above analysis...",
                                 className="conclusion-title"),
                        html.P(children="1. According to the data, Men are more likely to spend more on Cars than Women.",
                               className="conclusion-desc"),
                        html.P(children="2. According to the data, Women have longer Loan Terms than Men in early age.",
                               className="conclusion-desc"),
                    ]
                ),
            ],
            className="conclusion",
        ),
        # this paragraph is for the footer
        html.P(children="Made with 💖 by Bhavya Tyagi, 102097014, 3CSE2",
               className="footer"),
    ]
)

# creating callback on change of input by user


@app.callback(
    [Output("scatter_chart", "figure"), Output(
        "loan_term", "figure"), Output("loan_term_2", "figure"), Output("pie_chart", "figure")],
    [
        # Input taken thru above defined div and given special id gender-filter and handled
        Input("gender-filter", "value"),
    ],
)
# this is where our callback gets data upon change of input
# this method updates our charts at runtime
def update_charts(gender):
    # mask for input given by users
    mask = (
        (data.Gender_Desc == gender)
    )
    # getting filtered_data
    filtered_data = data.loc[mask, :]
    # building figures & layouts
    loan_term_figure = {
        "data": [
            {
                "x": filtered_data["Age"],
                "y": filtered_data["Loan_Term"],
                "type": "bar",
            },
        ],
        "layout": {"title": "Loan Term vs Age of a Person",
                   "x": 0.05,
                   "xanchor": "left",
                   "yaxis": {
                       "tickprefix": "$",
                   },
                   "colorway": ["#855C75"],
                   },

    }
    # building figures & layouts
    loan_term_2_figure = {
        "data": [
            {"x": filtered_data["ID"],
             "y": filtered_data["Current Valuation"],
                "type": "line", },
        ],
        "layout": {"title": "Current Valuation vs ID of a Person",
                   "x": 0.05,
                   "xanchor": "left",
                   "yaxis": {
                       "tickprefix": "$",
                   },
                   "colorway": ["#855C75"],
                   },
    }
    # building figures & layouts
    pie_chart_figure = px.pie(filtered_data, values=count,
                              names=names, title='Marital Status Distribution')
    scatter_chart_figure = px.scatter(filtered_data, x="Cost_Of_Vehicle", y="Age",
                                      title="Cost of Vehicle vs Age", color="Gender_Desc", color_discrete_sequence=px.colors.qualitative.Antique)
    # return figures
    return scatter_chart_figure, loan_term_figure, loan_term_2_figure, pie_chart_figure


# this is us running the server at defualt port 8000 trhu localhost
if __name__ == "__main__":
    app.run_server(debug=True)
