from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from accounts.views import ContactFormListCreate
from thedatabet.views import BettingTipsList

from .api import api_router

urlpatterns = [
    path('api/v2/', api_router.urls),
    path("django-admin/", admin.site.urls, name="djangoadmin"),
    path("admin/", include(wagtailadmin_urls), name="wagtailadmin"),
    path("documents/", include(wagtaildocs_urls), name="documents"),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('contact_form/', ContactFormListCreate.as_view()),

    path('betting_tips/', BettingTipsList.as_view()),

    path('thedataeditor/', include('thedataeditor.urls')),
    path('accounts/', include('accounts.urls')),
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
