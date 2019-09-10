from abc import ABCMeta


class DataSource(metaclass=ABCMeta):

    def count(self) -> int:
        raise NotImplementedError

    def count_by_field(self, field: str, value: str) -> int:
        raise NotImplementedError

    def create(self, obj: dict) -> bool:
        raise NotImplementedError

    def update(self, obj: dict) -> bool:
        raise NotImplementedError
