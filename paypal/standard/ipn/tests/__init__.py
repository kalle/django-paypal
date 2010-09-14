from django.conf import settings

if not getattr(settings, "PAYPAL_SKIP_TESTS", False):
    from test_ipn import *
