import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
from data.git_data import get_issues
from data.mock_data import issues, tags

app = dash.Dash(__name__)


def _create_table_view_div(data_dict):
    return html.Div(
        [
            dash_table.DataTable(
                id="table",
                columns=[{"name": key, "id": key} for key in data_dict[0].keys()],
                data=data_dict,
            )
        ]
    )


def _create_tags_listbox_div(data_listbox):
    return html.Div(
        [
            dcc.Dropdown(
                id="demo-dropdown",
                options=[{"label": item, "value": item} for item in data_listbox],
                # value="NYC",
            ),
            html.Div(id="dd-output-container"),
        ]
    )


app.layout = html.Div(
    [
        _create_tags_listbox_div(tags),
        _create_table_view_div(issues),
    ]
)
if __name__ == "__main__":
    issues = get_issues("equinor/gathering-leto")
    for issue in issues:
        print(issue.title)
    app.run_server(debug=True)