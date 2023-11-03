"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .authentication import Authentication
from .config import Config
from .drinks import Drinks
from .ingredients import Ingredients
from .orders import Orders
from .sdkconfiguration import SDKConfiguration, ServerEnvironment
from speakeasybar import utils
from speakeasybar.models import shared
from typing import Dict

class Speakeasybar:
    r"""The Speakeasy Bar: A bar that serves drinks.
    A secret underground bar that serves drinks to those in the know.
    https://docs.speakeasy.bar - The Speakeasy Bar Documentation.
    """
    authentication: Authentication
    r"""The authentication endpoints."""
    config: Config
    drinks: Drinks
    r"""The drinks endpoints."""
    ingredients: Ingredients
    r"""The ingredients endpoints."""
    orders: Orders
    r"""The orders endpoints."""

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 security: shared.Security = None,
                 environment: ServerEnvironment = None,
                 organization: str = None,
                 server: str = None,
                 server_url: str = None,
                 url_params: Dict[str, str] = None,
                 client: requests_http.Session = None,
                 retry_config: utils.RetryConfig = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.
        
        :param security: The security details required for authentication
        :type security: shared.Security
        :param environment: Allows setting the environment variable for url substitution
        :type environment: sdk.ServerEnvironment
        :param organization: Allows setting the organization variable for url substitution
        :type organization: str
        :param server: The server by name to use for all operations
        :type server: str
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: utils.RetryConfig
        """
        if client is None:
            client = requests_http.Session()
        
        
        security_client = utils.configure_security_client(client, security)
        
        
        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
        server_defaults = {
            'prod': {
            },
            'staging': {
            },
            'customer': {
                'environment': environment or 'prod',
                'organization': organization or 'api',
            },
        }

        self.sdk_configuration = SDKConfiguration(client, security_client, server_url, server, server_defaults, retry_config=retry_config)
       
        self._init_sdks()
    
    def _init_sdks(self):
        self.authentication = Authentication(self.sdk_configuration)
        self.config = Config(self.sdk_configuration)
        self.drinks = Drinks(self.sdk_configuration)
        self.ingredients = Ingredients(self.sdk_configuration)
        self.orders = Orders(self.sdk_configuration)
    