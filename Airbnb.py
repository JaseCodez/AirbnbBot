from random import randint
import Tenant
from typing import Text
import csv
from bs4 import BeautifulSoup


class AirbnbManager:
    def __init__(self, tenant_file: Text):
        self._tenant_list = []
        with open(tenant_file) as f:
            file = csv.reader(f)
            for line in file:
                self._tenant_list.append(Tenant())

        self.tenant_file = tenant_file

    def write_to_csv(self) -> str:
        pass

    def get_tenant_list(self):
        return self._tenant_list[:]

    def get_tenant_password(self):
        pass



