from pyramid.view import view_config


@view_config(route_name="home", renderer="json")
def my_view(request):
    return {"message": "hello world"}
