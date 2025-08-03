from typing import List, Protocol, Dict


class GraphRepo(Protocol):
    def add_company(self, company_id: int, properties: Dict):
        ...

    def relate(self, parent_id: int, child_id: int):
        ...

    def query_subsidiaries(self, company_id: int) -> List[int]:
        ...
