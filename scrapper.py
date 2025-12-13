import requests
from requests import Response
import requests
import asyncio
import aiohttp
import selenium
import os
from enum import StrEnum
from abc import ABC
from typing import Any

class RequestType(StrEnum):
    GET = "get"
    POST = "post"
    PUT = "put"
    DELETE = "delete"

class ContentType(StrEnum):
    HTML = "html"
    JSON = "json"
    XML = "xml"

class Scrapper(ABC):
    __base_url = ""
    def __init__(self, use_proxy: str = False,  use_selenium: bool = False, proxy_list = []):
        self.use_proxy = use_proxy
        self.use_selenium = use_selenium
        self.proxy_list = proxy_list

    def get_data(self, url, request_type: RequestType = RequestType.GET, **kwargs) -> str | dict | Any:
        if request_type == RequestType.GET:
            response = self.__get_request(url, kwargs)
            return response
        elif request_type == RequestType.POST:
            pass
        elif request_type == RequestType.PUT:
            pass

    async def async_get_data(self, url, request_type: RequestType = RequestType.GET, **kwargs) -> str | dict | Any:
        if request_type == RequestType.GET:
            response = await self.__async_get_request(url, **kwargs)
            return response
        elif request_type == RequestType.POST:
            pass
        elif request_type == RequestType.PUT:   
            pass

    def get_data_subpage(self, path, request_type: RequestType = RequestType.GET, **kwargs  ) -> str | dict | Any:
        url = f"{self.__base_url}/{path}" # 
        return self.get_data(url, request_type, **kwargs)
    
    def __get_request(self, url, **kwargs) -> Response:
        response = requests.get(url, kwargs)
        response.raise_for_status()
        return response
    
    async def __async_get_request(self, url, **kwargs) -> aiohttp.ClientResponse:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, **kwargs) as response:
                response.raise_for_status()
                return await response
    
    
    def get_request_text(self, url, **kwargs):
        response = self.__get_request(url, **kwargs)
        return response.text
    
    def get_request_json(self, url, **kwargs):
        response = self.__get_request(url, **kwargs)
        return response.json()

    def __post_request(self, url, data, **kwargs):
        response = requests.post(url, data, **kwargs)
        response.raise_for_status()
        return response   
    
    def post_request(self, url, data, **kwargs):
        response = self.__post_request(url, data, **kwargs)
        return response
    
    def post_request_json(self, url, data, **kwargs):
        response = self.__post_request(url, data, **kwargs)
        return response.json()
    
    def __put_request(self, url, data, **kwargs):
        response = requests.put(url, data, **kwargs)
        response.raise_for_status()
        return response
    
    def put_request(self, url, data, **kwargs):
        response = self.__put_request(url, data, **kwargs)
        return response.json()
    
    def __delete_request(self, url, **kwargs):
        response = requests.delete(url, **kwargs)
        response.raise_for_status()
        return response
    
    def delete_request(self, url, **kwargs):
        response = self.__delete_request(url, **kwargs)
        return response

        