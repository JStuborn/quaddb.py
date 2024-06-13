# api_wrapper.py

import requests
from typing import List, Dict, Any, Optional
from uuid import uuid4
from .errors import InvalidParameterError, NotFoundError, ServerError
from .utils import handle_response

class QuadDBClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_documents(self, db: str, page: int = 1, size: int = 5) -> Dict[str, Any]:
        url = f"{self.base_url}/api/v1/docs/{db}"
        params = {'page': page, 'size': size}
        response = requests.get(url, params=params)
        return handle_response(response)

    def create_documents(self, db: str, documents: List[Dict[str, Any]]) -> Dict[str, Any]:
        url = f"{self.base_url}/api/v1/docs/{db}"
        for document in documents:
            if 'id' not in document or not document['id']:
                document['id'] = str(uuid4())
        response = requests.post(url, json=documents)
        return handle_response(response)

    def search_documents(self, db: str, field: str, value: str) -> Dict[str, Any]:
        url = f"{self.base_url}/api/v1/docs/{db}/search"
        params = {'field': field, 'value': value}
        response = requests.get(url, params=params)
        return handle_response(response)

    def get_document(self, db: str, key: str) -> Dict[str, Any]:
        url = f"{self.base_url}/api/v1/docs/{db}/{key}"
        response = requests.get(url)
        return handle_response(response)

    def update_document(self, db: str, key: str, data: Dict[str, Any]) -> Dict[str, Any]:
        url = f"{self.base_url}/api/v1/docs/{db}/{key}"
        response = requests.put(url, json=data)
        return handle_response(response)

    def delete_document(self, db: str, key: str) -> Dict[str, Any]:
        url = f"{self.base_url}/api/v1/docs/{db}/{key}"
        response = requests.delete(url)
        return handle_response(response)

    def get_updates(self) -> Dict[str, Any]:
        url = f"{self.base_url}/api/v1/docs/updates"
        response = requests.get(url)
        return handle_response(response)

    def get_collections(self) -> Dict[str, int]:
        url = f"{self.base_url}/api/v1/docs/collections"
        response = requests.get(url)
        return handle_response(response)
