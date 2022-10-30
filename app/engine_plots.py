def plot(
    axis,
    title: str,
    x_data: list,
    y_datas: dict[str, list],
    axis_params: dict
) -> None:
    axis.set_title(title)
    axis.set(**axis_params)

    for name, y_data in y_datas.items():
        axis.plot(x_data, y_data, label=name)

    axis.legend()
