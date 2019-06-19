from .views import FacebookLogin

re_path(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login')
