def get_date(request, param):
    date_param = request.query_params.get(param)
    date_param = date_param.split("-")
    date_param_year, date_param_month, date_param_day = int(date_param[0]), int(date_param[1]), int(date_param[2])
    return date_param_day, date_param_month, date_param_year
