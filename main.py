import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

external_stylesheets = [dbc.themes.BOOTSTRAP]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets, title="Dashboard for State wise Exports")
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw'
                 '/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')

df = df.reset_index()
df = df.drop('Unnamed: 0', axis=1)

fig = px.bar(
    df, x="state", y="total exports", color="corn", barmode="group",
    title="Corn exports by States"
)
# fig.update_layout(
#     plot_bgcolor=colors['background'],
#     paper_bgcolor=colors['background'],
#     font_color=colors['text']
# )

fig1 = px.scatter(df, x="state", y="dairy", size="total exports",
                  color="beef", title="Dairy exports by States")


# fig1.update_layout(
#     plot_bgcolor=colors['background'],
#     paper_bgcolor=colors['background'],
#     font_color=colors['text']
# )


def generate_table(dataframe, max_rows=10):
    return dbc.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Main", href="#")),

    ],
    brand="DashBoard",
    brand_href="#",
    color="primary",
    dark=True,
)

server = app.server

app.layout = html.Div(

    children=[navbar,
              dbc.Container([

                  dbc.Jumbotron(
                      style={
                          'background': colors['background']
                      },
                      children=[
                          html.H1(children="Welcome to Export Dashboard", className="display-3", style={
                              'textAlign': 'center',
                              'color': colors['text']
                          }),
                          html.Div(children='''
                                            Dashboard for Web applications 
                                        ''', style={
                              'textAlign': 'center',
                              'color': colors['text']
                          }),
                      ]
                  ),
                  html.H2(
                      children='''
                        Data of Exports from US states is shown as graph and table. 
                      ''',
                      style={
                          'textAlign': 'center'
                      }
                  ),
                  dbc.Row([
                      dbc.Col([
                          dcc.Graph(
                              id="fruit_graph",
                              figure=fig
                          ),
                      ]),
                      html.Br(),
                      dbc.Col([
                          dcc.Graph(
                              id="fruit_graph_1",
                              figure=fig1
                          ),
                      ])
                  ]),
                  html.Br(),
                  html.H1(children="Data Table", style={'textAlign': 'center'}),
                  generate_table(df)

              ])]
)
