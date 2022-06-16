from .base import *

DATABASES = {
    'default': {
        'ENGINE': env("ENGINE"),
        'NAME': env("NAME"),
        'USER': env("USER"),
        'HOST': env("HOST"),
        'PORT': env("PORT"),
        'PASSWORD': env("PASSWORD"),
    }
}
