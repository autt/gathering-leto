import dash
import dash_table
from data.mock_data import issues

app = dash.Dash(__name__)

app.layout = dash_table.DataTable(
    id="table",
    columns=[{"name": key, "id": key} for key in issues[0].keys()],
    data=issues,
)

if __name__ == "__main__":
    app.run_server(debug=True)