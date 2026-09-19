import pytest

from trains_shedule.trains import TrainSchedule


def test_get_all_trains():
    schedule = TrainSchedule()

    trains = schedule.get_all_trains()

    assert len(trains) == 12


def test_find_existing_train():
    schedule = TrainSchedule()

    train = schedule.find_train("001A")

    assert train is not None
    assert train["departure"] == "Бишкек"
    assert train["arrival"] == "Алматы"


def test_find_nonexistent_train():
    schedule = TrainSchedule()

    train = schedule.find_train("999X")

    assert train is None


def test_search_by_train_number():
    schedule = TrainSchedule()

    results = schedule.search("001A")

    assert len(results) == 1
    assert results[0]["number"] == "001A"


def test_search_by_city():
    schedule = TrainSchedule()

    results = schedule.search("Алматы")

    assert len(results) > 0


def test_search_is_case_insensitive():
    schedule = TrainSchedule()

    results = schedule.search("бишкек")

    assert len(results) > 0


def test_empty_search_returns_all_trains():
    schedule = TrainSchedule()

    results = schedule.search("")

    assert len(results) == 12


def test_filter_by_departure():
    schedule = TrainSchedule()

    results = schedule.filter_by_departure("Бишкек")

    assert len(results) > 0

    for train in results:
        assert train["departure"] == "Бишкек"


def test_filter_by_type():
    schedule = TrainSchedule()

    results = schedule.filter_by_type("Скорый")

    assert len(results) > 0

    for train in results:
        assert train["type"] == "Скорый"


def test_filter_all_types():
    schedule = TrainSchedule()

    results = schedule.filter_by_type("Все типы")

    assert len(results) == 12


def test_get_stations():
    schedule = TrainSchedule()

    stations = schedule.get_stations()

    assert "Бишкек" in stations
    assert "Алматы" in stations
    assert "Ош" in stations


def test_available_trains():
    schedule = TrainSchedule()

    results = schedule.get_available_trains()

    assert len(results) == 12

    for train in results:
        assert train["seats"] > 0


def test_train_has_required_fields():
    schedule = TrainSchedule()

    for train in schedule.get_all_trains():
        assert "number" in train
        assert "name" in train
        assert "departure" in train
        assert "arrival" in train
        assert "departure_time" in train
        assert "arrival_time" in train
        assert "duration" in train
        assert "type" in train
        assert "seats" in train


def test_train_number_is_unique():
    schedule = TrainSchedule()

    numbers = [
        train["number"]
        for train in schedule.get_all_trains()
    ]

    assert len(numbers) == len(set(numbers))