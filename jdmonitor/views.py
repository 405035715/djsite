from django.shortcuts import render, HttpResponse
import json
from .models import JdMonitor
import datetime

APP_CODE = 1.0  # 版本号


def response_help(appcode, databuffer, result=None):
    """
    统一返回结果：json格式
    :param appcode: 版本号
    :param databuffer: 请求状态
    :param result: 请求结果
    :return:
    """
    json_dic = {"appcode": appcode, "databuffer": databuffer}
    if result:
        json_dic["result"] = result
    json_str = json.dumps(json_dic, False)
    return json_str


def get_monitor_data(request):
    """
    获取监控数据
    :param request:
    :return:
    """
    result_set = []
    jd_monitor_data = JdMonitor.objects.all()
    for data in jd_monitor_data:
        result_set.append({'hospital_name': data.hospital_name, 'last_update_datetime': data.last_update_datetime.strftime('%Y-%m-%d %H:%M:%S')})
    return HttpResponse(response_help(APP_CODE, 'success', result_set))


def update_monitor_data(request):
    """
    插入监控数据
    :param request:
    :return:
    """
    req = getattr(request, request.method)
    param_hospital_name = req.get('hospital_name')
    param_last_update_datetime = datetime.datetime.strptime(req.get('last_update_datetime'), '%Y-%m-%d-%H:%M:%S')
    jd_monitor = JdMonitor(hospital_name=param_hospital_name,
                           last_update_datetime=param_last_update_datetime)
    jd_monitor.save()
    return HttpResponse(response_help(APP_CODE, 'success'))