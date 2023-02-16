from datetime import timedelta, datetime
from pprint import pprint

import requests

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from common.menu import MenuSetting
from common.DB.jdbc import db_select, db_create
import json
import math

menuListDB = MenuSetting()

with open("setting.json", encoding="UTF-8") as f:
    SETTING = json.loads(f.read())
Customer = SETTING['PROJECT']['CUSTOMER']
WorldUse = SETTING['PROJECT']['MAP']['World']
KoreaUse = SETTING['PROJECT']['MAP']['Korea']
AreaUse = SETTING['PROJECT']['MAP']['Area']['use']
AreaType = SETTING['PROJECT']['MAP']['Area']['type']
Login_Method = SETTING['PROJECT']['LOGIN']

def index(request):
    returnData = {'menuList': menuListDB}
    return render(request, 'web/index.html', returnData)

def dashboard(request):
    res_data = {}
    if not 'sessionid' in request.session:
        res_data['error'] = '먼저 로그인을 해주세요.'
        return render(request, 'common/login.html', res_data)
    else:
        dashboardType = 'dataFabric/webQuery_DF.html'
        returnData = {'menuList': menuListDB, 'Login_Method': Login_Method}
        return render(request, dashboardType, returnData)

############################ X-factor-DF ############################################
def dataFabric_webQuery(request):
    returnData = {'menuList': menuListDB, 'Customer': Customer}
    return render(request, 'dataFabric/webQuery_DF.html', returnData)

def dataFabric_monitoring(request):
    returnData = {'menuList': menuListDB, 'Customer': Customer,}
    return render(request, 'dataFabric/monitoring_DF.html', returnData)

def dataFabric_Navigator(request):
    returnData = {'menuList': menuListDB, 'Customer': Customer,}
    return render(request, 'dataFabric/Navigator_DF.html', returnData)

#################################### api ############################################
@csrf_exempt
def dataFabric_api(request) :
    data = str(request.POST['data'])
    if data.lower().startswith('select') :
        result = db_select(data)
        
        if result['status'] == 200 :
            column = result['data'].columns.values.tolist()
            data = result['data'].values.tolist()
            returnData = {
                'status' : result['status'],
                'column' : column,
                'data' : data
            }
        elif result['status'] == 400 :
            returnData = result
    elif data.lower().startswith('create') :
        result = db_create(data)
        
        if result['status'] == 200 :
            returnData = {
                'status' : result['status'],
                'data' : result['data']
            }
        elif result['status'] == 400 :
            returnData = result
    return JsonResponse(returnData)
    
    