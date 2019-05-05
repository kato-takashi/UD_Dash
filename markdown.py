import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
dcc.Markdown('''
# 見出し1
## 見出し2
- 箇条書き
- 箇条書き
- 箇条書き
''')
])
if __name__ == '__main__':
    app.run_server(debug=True)
