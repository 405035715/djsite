# coding = utf-8

from django.shortcuts import render, HttpResponse
import json
import urllib.request
import urllib.parse
# from .models import JdMonitor
# import datetime
import time

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


def jdimage_login():
    """
    监测APP是否登录成功
    连续3次测试登录不成功，判断为异常
    登录不成功原因：1、账户不正确 2、服务器响应异常 返回：{'login': False, 'token': ''}
    登录成功，返回：{'login': True, 'token': '')}
    """
    url = 'http://121.40.19.7/api/doctor/login'
    values = {'username': '18072996469',
              'password': '123456'
              }
    data = urllib.parse.urlencode(values)  # 编码工作
    data = data.encode('utf-8')
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'  # 模拟浏览器
    headers = {'User-Agent': user_agent}
    req = urllib.request.Request(url, data, headers)  # 发送请求同时传data表单
    i = 0
    while i < 3:  # 如果失败会尝试3次
        try:
            with urllib.request.urlopen(req) as response:  # 接受反馈的信息
                the_page = response.read().decode('utf-8')  # 读取反馈的内容
                result_json = json.loads(the_page)  # 解析json格式的str
                # print(the_page)
                if result_json['flag']:
                    return {'login': True, 'token': result_json.get('user', {}).get('token', '')}  # 登录成功返回token
                else:
                    time.sleep(1)  # 失败后，1秒后再测试
        except urllib.request.URLError as e:
            time.sleep(1)  # 失败后，1秒后再测试
            print(e)
        finally:
            i += 1
    return {'login': False, 'token': ''}  # 登录失败返回False


def jdimage_hospitals(token_str):
    """
    获取医院列表
    """
    url = 'http://121.40.19.7/api/real/info?token=%s' % token_str
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            the_page = response.read().decode('utf-8')  # 读取反馈的内容
            result_json = json.loads(the_page)  # 解析json格式的str
            monitor_hospitals = []
            for hospital in result_json['info']['linkHospitals']:
                monitor_hospitals.append(hospital)
                print(hospital)
            return monitor_hospitals  # [{'name': '影像云诊断中心', 'pacs_hid': 'jdimage', 'id': 14},...]
    except urllib.request.URLError as e:
        print(e)
    return [{'name': '', 'pacs_hid': '', 'id': 0}]


def hospitals_from_jdimage(request):
    """
    获取jdimage中的医院
    :param request:
    :return:
    """
    hospitals_set = jdimage_hospitals(jdimage_login()['token'])
    context = {
        'hospitals_set': hospitals_set
    }
    return render(request, 'jdmonitor/jdimage_hospitals.html', context)

