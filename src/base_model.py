import json
import os

from typing import Dict, Optional, Union, Any
from requests import Request, Session, PreparedRequest, Response

class BaseEndpointModel:

    def __init__(self):
        self.base_url: str = "https://rickandmortyapi.com/api/"
        self.endpoint: str = ""
        self.session: Session = Session()

    def build_request(
        self,
        method: Optional[str] = "GET",
        payload: Optional[Dict[str, Union[str, float, list, dict]]] = None,
        id: Union[int, str, None] = None,
        search: Optional[str] = None,
    ) -> PreparedRequest:

        request_base_url: str = f"{self.base_url}{self.endpoint}"
        url = f"{request_base_url}/{id}" if id is not None else request_base_url

        if search is not None:
            search = search if search[0] != "?" else search[1:]
            url = f"{url}?{search}"

        print(f"url: {url}")
        return self.session.prepare_request(
            Request(method=method, url=url, data=json.dumps(payload))
        )

    def get(
        self,
        id: Optional[Union[int, str]] = None,
        search: Optional[str] = None
    ):
        req: PreparedRequest = self.build_request(
            id=id, search=search
        )
        self.last_get = self.session.send(req)
        return self