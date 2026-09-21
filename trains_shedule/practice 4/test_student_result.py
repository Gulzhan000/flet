import pytest

from student_result import get_result


@pytest.mark.parametrize(
    "score, attendance, expected",
    [
        (90, 80, "Отлично"),
        (100, 100, "Отлично"),
        (95, 85, "Отлично"),
        (89, 80, "Хорошо"),
        (90, 79, "Хорошо"),
        (70, 70, "Хорошо"),
        (89, 70, "Хорошо"),
        (69, 70, "Зачёт"),
        (70, 69, "Зачёт"),
        (50, 60, "Зачёт"),
        (69, 60, "Зачёт"),
        (49, 60, "Незачёт"),
        (50, 59, "Незачёт"),
        (0, 0, "Незачёт"),
        (49, 59, "Незачёт")
    ]
)
def test_get_result(score, attendance, expected):
    assert get_result(score, attendance) == expected


@pytest.mark.parametrize(
    "score",
    [-1, -10, 101, 150]
)
def test_invalid_score(score):
    assert get_result(score, 80) == "Некорректный балл"


@pytest.mark.parametrize(
    "attendance",
    [-1, -10, 101, 150]
)
def test_invalid_attendance(attendance):
    assert get_result(80, attendance) == "Некорректная посещаемость"


@pytest.mark.parametrize(
    "score",
    ["90", "70", "50", None, [], {}]
)
def test_invalid_score_type(score):
    with pytest.raises(TypeError, match="Баллы должны быть числом"):
        get_result(score, 80)


@pytest.mark.parametrize(
    "attendance",
    ["80", "70", "60", None, [], {}]
)
def test_invalid_attendance_type(attendance):
    with pytest.raises(
        TypeError,
        match="Посещаемость должна быть числом"
    ):
        get_result(80, attendance)


@pytest.mark.parametrize(
    "score, attendance, expected",
    [
        (0, 0, "Незачёт"),
        (49, 59, "Незачёт"),
        (50, 60, "Зачёт"),
        (69, 69, "Зачёт"),
        (70, 70, "Хорошо"),
        (89, 79, "Хорошо"),
        (90, 80, "Отлично"),
        (100, 100, "Отлично")
    ]
)
def test_boundary_values(score, attendance, expected):
    assert get_result(score, attendance) == expected