from django.urls import path

from core.views import home, about, contact, ContactView, p404_page, export, send_mail

app_name = "core"
urlpatterns = [
    path("", home, name="home_page"),
    path("about/", about, name="about_page"),
    # path("contact/", contact, name="contact"),
    path("contact/", ContactView.as_view(), name="contact"),

    path("404/", p404_page, name="404_page"),


    path("export/", export, name="export"),
    path("sendmail/", send_mail, name="send_mail"),

]