from trips.repository.base import DataSource


class TripsManagement:

    def __init__(self, repo: DataSource):
        self.repo = repo

    def count_trips(self) -> int:
        return self.repo.count()

    def count_trips_by_city(self, city: str) -> int:
        return self.repo.count_by_field("city", city)

    def create_trip(self, trip: dict) -> bool:
        ok = self.repo.create(trip)
        if ok:
            return ok
        raise TripsManagementError("Miscellaneous Error")

    def update_trip(self, trip: dict):
        # TODO: Pending
        pass


class TripsManagementError(Exception):
    pass
