from django.apps import AppConfig


class WebForumConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'web_forum'


# @app.route("/graphcall")
# def graphcall():
#     token = _get_token_from_cache(app_config.SCOPE)
#     if not token:
#         return redirect(url_for("login"))
#     graph_data = requests.get(  # Use token to call downstream service.
#         app_config.ENDPOINT,
#         headers={'Authorization': 'Bearer ' + token['access_token']},
#         ).json()
#     return render_template('display.html', result=graph_data)