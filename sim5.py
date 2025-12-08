from scrapper import *


class SIM5(Scrapper):
    __base_url = "https://5sim.net/v1/" 
    __headers = {'Accept': 'application/json'}
    def __init__(self, token: str = None, use_proxy = False, use_selenium = False, proxy_list=...):
        super().__init__(use_proxy, use_selenium, proxy_list)
        self.user_url = f"{self.__base_url}user/"
        self.guest_url = f"{self.__base_url}guest/"
        self.vendor_url = f"{self.__base_url}vendor/"
        self.token = token
    
    def __choose_token(self, token: str) -> str:
        if token:
            return token
        if self.token:
            return self.token
        raise Exception("Token not set")

    def __create_user_url(self, path: str) -> str:
        return f"{self.user_url}{path}"
    
    def __create_guest_url(self, path: str) -> str:
        return f"{self.guest_url}{path}"
    
    def __create_vendor_url(self, path: str) -> str:
        return f"{self.vendor_url}{path}"
    
    def user_get_balance(self, token = None):
        token = self.__choose_token(token)
        headers = self.__headers
        headers['Authorization'] = f"Bearer {token}"
        url = self.__create_user_url("profile")
        response = self.get_request_json(url, headers = headers)
        return response['balance']
    
    def user_get_order_history(self, token = None, category: str = "hosting", limit: int = 5, offset: int = 0, order="id", reverse: bool = True):
        token = self.__choose_token(token)
        headers = self.__headers
        headers['Authorization'] = f"Bearer {token}"
        params = (
            ('category', category),
            ('limit', limit),
            ('offset', offset),
            ('order', order),
            ('reverse', reverse),
        )
        url = self.__create_user_url(f"orders")
        response = self.get_request_json(url, headers = headers, params = params)
        return response

    def user_get_payments_history(self, token = None, limit: int = 5, offset: int = 0, order="id", reverse: bool = True):
        token = self.__choose_token(token)
        headers = self.__headers
        headers['Authorization'] = f"Bearer {token}"
        params = (
            ('limit', limit),
            ('offset', offset),
            ('order', order),
            ('reverse', reverse),
        )
        url = self.__create_user_url(f"payments")
        response = self.get_request_json(url, headers = headers, params = params)
        return response
    
    def get_prices_limit_list(self, token= None):
        token = self.__choose_token(token)
        headers = self.__headers
        headers['Authorization'] = f"Bearer {token}"
        url = self.__create_user_url("max-prices")
        response = self.get_request_json(url, headers = headers)
        return response
    
    def post_price_limit_create_update(self, token=None, product_name: str = "facebook", price: int = 10):
        token = self.__choose_token(token)
        headers = self.__headers
        headers['Authorization'] = f"Bearer {token}"
        data = {
            "product_name": product_name,
            "price": price
        }
        url = self.__create_user_url("max-prices")
        response = self.post_request(url, data=data, headers = headers)
        return response