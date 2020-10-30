import dash
import dash_table
import dash_html_components as html
import dash_core_components as dcc
import data
from data.git_data import get_issues
import plotly.graph_objects as go


tags = ["todo", "in progress", "discussion"]
external_style = ["https://eds-static.equinor.com/font/equinor-font.css"]


app = dash.Dash(__name__, external_stylesheets=external_style)


data_issues = get_issues("equinor/gathering-leto")


def get_data_dict(data_json_list):
    results = []
    for node in data_json_list:
        d = {"title": node.title, "id": node.id, "user": node.user.login}
        results.append(d)
    return results


def _create_logo():
    return html.Img(
        src="https://eds-static.equinor.com/logo/equinor-logo-primary.svg#red",
        id="logo",
        width=100,
        alt="Equinor",
    )


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
                id="users-dropdown",
                options=[{"label": item, "value": item} for item in data_listbox],
            ),
            html.Div(id="show-user"),
        ]
    )


def _create_navbar():
    return html.Div(
        children=[
            html.Nav(
                className="nav nav-pills",
                children=[
                    html.A(
                        "Leto issues",
                        className="nav-item nav-link active btn",
                        href="/",
                    )
                ],
            )
        ]
    )


def _create_bottombar():
    return html.Div(
        children=[
            html.Nav(
                className="bottombar",
                children=[
                    html.P(
                        "Team Leto - copyright 2020",
                    )
                ],
            )
        ]
    )


def _create_activity_plot(issue_data):
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            name="Closed",
            x=issue_data["date"],
            y=issue_data["closed"],
            stackgroup="the-one",
        )
    )
    fig.add_trace(
        go.Scatter(
            name="Open",
            x=issue_data["date"],
            y=issue_data["open"],
            stackgroup="the-one",
        )
    )

    return html.Div(
        [
            dcc.Graph(figure=fig),
        ]
    )


app.layout = html.Div(
    [
        _create_logo(),
        _create_navbar(),
        _create_tags_listbox_div(tags),
        _create_table_view_div(get_data_dict(data_issues)),
        _create_bottombar(),
        _create_activity_plot(
            data.git_data.fetch_issue_activity("equinor/gathering-leto")
        ),
    ]
)


@app.callback(
    dash.dependencies.Output("show-user", "children"),
    [dash.dependencies.Input("users-dropdown", "value")],
)
def update_output(value):
    return 'You have selected "{}"'.format(value)


if __name__ == "__main__":
    app.run_server(debug=True, port=8000, host="0.0.0.0")
