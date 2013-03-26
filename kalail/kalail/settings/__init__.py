import os

# Import corresponding environment settings.
try:
    app_env = os.environ["KALAIL_ENV"]
    if app_env == "production":
        # Import production settings
        from .production import *
    elif app_env == "development":
        # Import development settings
        from .development import *
except KeyError, e:
    # import local settings
    from .local import *