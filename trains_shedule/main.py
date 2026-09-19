import flet as ft
from trains_shedule.trains import TrainSchedule


def main(page: ft.Page):
    page.title = "Train Schedule"
    page.padding = 0
    page.bgcolor = "#F4F6F8"
    page.window.width = 1200
    page.window.height = 780

    schedule = TrainSchedule()

    search_field = ft.TextField(
        label="Поиск",
        hint_text="Номер, направление или станция",
        expand=True
    )

    departure_dropdown = ft.Dropdown(
        label="Станция отправления",
        width=220,
        options=[
            ft.DropdownOption("Все станции"),
            ft.DropdownOption("Бишкек"),
            ft.DropdownOption("Алматы"),
            ft.DropdownOption("Ташкент"),
            ft.DropdownOption("Каракол"),
            ft.DropdownOption("Ош"),
            ft.DropdownOption("Тараз"),
            ft.DropdownOption("Шымкент")
        ],
        value="Все станции"
    )

    type_dropdown = ft.Dropdown(
        label="Тип поезда",
        width=200,
        options=[
            ft.DropdownOption("Все типы"),
            ft.DropdownOption("Скорый"),
            ft.DropdownOption("Пассажирский")
        ],
        value="Все типы"
    )

    trains_list = ft.Column(
        spacing=10,
        expand=True,
        scroll=ft.ScrollMode.AUTO
    )

    selected_train = ft.Text(
        "Выберите поезд",
        size=22,
        weight=ft.FontWeight.BOLD,
        color="#172033"
    )

    selected_info = ft.Text(
        "Информация о выбранном поезде появится здесь.",
        size=15,
        color="#64748B"
    )

    status_message = ft.Text(
        "",
        size=14
    )

    total_text = ft.Text(
        "12 поездов",
        size=14,
        color="#64748B"
    )

    def show_train(train):
        selected_train.value = (
            "Поезд " + train["number"]
        )

        selected_info.value = (
            "Направление: "
            + train["name"]
            + "\n\n"
            + "Отправление: "
            + train["departure"]
            + " — "
            + train["departure_time"]
            + "\n"
            + "Прибытие: "
            + train["arrival"]
            + " — "
            + train["arrival_time"]
            + "\n"
            + "Продолжительность: "
            + train["duration"]
            + "\n"
            + "Тип: "
            + train["type"]
            + "\n"
            + "Свободных мест: "
            + str(train["seats"])
        )

        page.update()

    def create_train_card(train):
        if train["seats"] <= 20:
            seats_text = "Осталось мало мест"
            seats_color = "#DC2626"
        else:
            seats_text = (
                "Свободных мест: "
                + str(train["seats"])
            )
            seats_color = "#059669"

        return ft.Container(
            bgcolor="#FFFFFF",
            padding=16,
            border_radius=12,
            content=ft.Row(
                [
                    ft.Container(
                        width=70,
                        height=70,
                        bgcolor="#E8EEF9",
                        border_radius=10,
                        content=ft.Column(
                            [
                                ft.Text(
                                    train["number"],
                                    size=16,
                                    weight=ft.FontWeight.BOLD,
                                    color="#2563EB"
                                ),
                                ft.Text(
                                    train["type"],
                                    size=11,
                                    color="#64748B"
                                )
                            ],
                            spacing=3
                        )
                    ),

                    ft.Container(width=15),

                    ft.Column(
                        [
                            ft.Text(
                                train["name"],
                                size=18,
                                weight=ft.FontWeight.BOLD,
                                color="#172033"
                            ),

                            ft.Text(
                                train["departure"]
                                + "  "
                                + train["departure_time"]
                                + "     →     "
                                + train["arrival"]
                                + "  "
                                + train["arrival_time"],
                                size=14,
                                color="#475569"
                            ),

                            ft.Text(
                                "В пути: "
                                + train["duration"],
                                size=13,
                                color="#64748B"
                            ),

                            ft.Text(
                                seats_text,
                                size=13,
                                color=seats_color
                            )
                        ],
                        spacing=5,
                        expand=True
                    ),

                    ft.Button(
                        "Подробнее",
                        on_click=lambda e, t=train: show_train(t)
                    )
                ],
                vertical_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

    def display_trains(trains):
        trains_list.controls.clear()

        if not trains:
            trains_list.controls.append(
                ft.Container(
                    padding=30,
                    content=ft.Text(
                        "По вашему запросу поезда не найдены.",
                        size=16,
                        color="#64748B"
                    )
                )
            )
        else:
            for train in trains:
                trains_list.controls.append(
                    create_train_card(train)
                )

        total_text.value = (
            str(len(trains))
            + " поездов найдено"
        )

        page.update()

    def search_trains(e):
        query = search_field.value

        results = schedule.search(query)

        departure = departure_dropdown.value

        if departure != "Все станции":
            results = [
                train
                for train in results
                if train["departure"] == departure
            ]

        train_type = type_dropdown.value

        if train_type != "Все типы":
            results = [
                train
                for train in results
                if train["type"] == train_type
            ]

        display_trains(results)

        status_message.value = ""

    def reset_filters(e):
        search_field.value = ""
        departure_dropdown.value = "Все станции"
        type_dropdown.value = "Все типы"

        display_trains(
            schedule.get_all_trains()
        )

        selected_train.value = "Выберите поезд"

        selected_info.value = (
            "Информация о выбранном поезде "
            "появится здесь."
        )

        status_message.value = ""

    def show_available(e):
        display_trains(
            schedule.get_available_trains()
        )

        status_message.value = (
            "Показаны поезда со свободными местами."
        )

        status_message.color = "#059669"

    header = ft.Container(
        bgcolor="#172033",
        padding=22,
        content=ft.Row(
            [
                ft.Column(
                    [
                        ft.Text(
                            "TRAIN SCHEDULE",
                            size=28,
                            weight=ft.FontWeight.BOLD,
                            color="#FFFFFF"
                        ),

                        ft.Text(
                            "Расписание поездов",
                            size=14,
                            color="#CBD5E1"
                        )
                    ],
                    spacing=3
                ),

                ft.Container(
                    expand=True
                ),

                ft.Text(
                    "Система поиска поездов",
                    size=14,
                    color="#CBD5E1"
                )
            ]
        )
    )

    filters = ft.Container(
        bgcolor="#FFFFFF",
        padding=18,
        border_radius=12,
        content=ft.Column(
            [
                ft.Text(
                    "Поиск и фильтры",
                    size=19,
                    weight=ft.FontWeight.BOLD,
                    color="#172033"
                ),

                ft.Row(
                    [
                        search_field,

                        departure_dropdown,

                        type_dropdown
                    ]
                ),

                ft.Row(
                    [
                        ft.Button(
                            "Найти",
                            on_click=search_trains
                        ),

                        ft.Button(
                            "Сбросить",
                            on_click=reset_filters
                        ),

                        ft.Button(
                            "Только доступные",
                            on_click=show_available
                        )
                    ]
                )
            ],
            spacing=10
        )
    )

    trains_section = ft.Container(
        bgcolor="#FFFFFF",
        padding=18,
        border_radius=12,
        expand=True,
        content=ft.Column(
            [
                ft.Row(
                    [
                        ft.Text(
                            "Расписание",
                            size=20,
                            weight=ft.FontWeight.BOLD,
                            color="#172033"
                        ),

                        ft.Container(
                            expand=True
                        ),

                        total_text
                    ]
                ),

                ft.Divider(),

                trains_list
            ],
            expand=True
        )
    )

    details_section = ft.Container(
        bgcolor="#FFFFFF",
        padding=20,
        width=350,
        border_radius=12,
        content=ft.Column(
            [
                ft.Text(
                    "Информация о поезде",
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    color="#172033"
                ),

                ft.Divider(),

                selected_train,

                ft.Container(
                    height=10
                ),

                selected_info,

                ft.Container(
                    expand=True
                ),

                ft.Text(
                    "Статус системы",
                    size=13,
                    color="#64748B"
                ),

                status_message
            ],
            spacing=8
        )
    )

    page.add(
        header,

        ft.Container(
            padding=20,
            expand=True,
            content=ft.Column(
                [
                    filters,

                    ft.Row(
                        [
                            trains_section,
                            details_section
                        ],
                        vertical_alignment=ft.CrossAxisAlignment.START,
                        expand=True
                    )
                ],
                expand=True
            )
        )
    )

    display_trains(
        schedule.get_all_trains()
    )


if __name__ == "__main__":
    ft.run(main)