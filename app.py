import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
from data.git_data import get_issues
from data.mock_data import issues, tags

app = dash.Dash(__name__)


data_issues = get_issues("equinor/gathering-leto")


def get_data_dict(data_json_list):
    results = []
    for node in data_json_list:
        d = {"title": node.title, "id": node.id, "user": node.user.login}
        results.append(d)
    return results


def _create_table_view_div(data_dict):
    print(data_dict[0].keys())
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
                id="users-dropdown",
                options=[{"label": item, "value": item} for item in data_listbox],
            ),
            html.Div(id="show-user"),
        ]
    )


app.layout = html.Div(
    [
        _create_tags_listbox_div(tags),
        _create_table_view_div(get_data_dict(data_issues)),
    ]
)


@app.callback(
    dash.dependencies.Output("show-user", "children"),
    [dash.dependencies.Input("users-dropdown", "value")],
)
def update_output(value):
    return 'You have selected "{}"'.format(value)


if __name__ == "__main__":
    app.run_server(debug=True)