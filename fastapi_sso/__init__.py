"""FastAPI plugin to enable SSO to most common providers.

(such as Facebook login, Google login and login via Microsoft Office 365 account)
"""

from .sso.base import OpenID, SSOBase, SSOLoginError
from .sso.bitbucket import BitbucketSSO
from .sso.discord import DiscordSSO
from .sso.facebook import FacebookSSO
from .sso.fitbit import FitbitSSO
from .sso.generic import create_provider
from .sso.github import GithubSSO
from .sso.gitlab import GitlabSSO
from .sso.google import GoogleSSO
from .sso.kakao import KakaoSSO
from .sso.line import LineSSO
from .sso.linkedin import LinkedInSSO
from .sso.microsoft import MicrosoftSSO
from .sso.naver import NaverSSO
from .sso.notion import NotionSSO
from .sso.spotify import SpotifySSO
from .sso.twitter import TwitterSSO

__all__ = [
    "BitbucketSSO",
    "DiscordSSO",
    "FacebookSSO",
    "FitbitSSO",
    "GithubSSO",
    "GitlabSSO",
    "GoogleSSO",
    "KakaoSSO",
    "LineSSO",
    "LinkedInSSO",
    "MicrosoftSSO",
    "NaverSSO",
    "NotionSSO",
    "OpenID",
    "SSOBase",
    "SSOLoginError",
    "SpotifySSO",
    "TwitterSSO",
    "create_provider",
]
