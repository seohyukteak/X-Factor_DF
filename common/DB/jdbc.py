import teradataml
from sqlalchemy import *
from teradataml import *
from pprint import pprint
import pandas as pd

def db_select(qry):    
    try :
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")    
            
        result = td_context.execute(qry)   
        
        data = result.fetchall()    
        
        data = pd.DataFrame(data)    
        
        data = data.fillna('NULL')
        print(data.columns)
        print("===============================")
        print("Success")
        print("===============================")
        data = {'status' : 200, 'data' : data, 'type' : 'select'}
    
    except Exception as e :
        if 'Failed to connect to Teradata Vantage' in str(e) :
            data = {'status' : 404, 'data' : 'Failed to connect to Teradata Vantage', 'type' : 'select'}
        
        else :
            if '[Error' in str(e) :
                err_index = str(e).find('[Error')
                err_index = str(e).index(']', err_index)
                error = str(e)[0 : err_index]
                error_list = str(e).strip(error).split('at ')
                for i in range(len(error_list)) :
                    if i == 0 :
                        error_list[i] = 'S' + error_list[i]
                        continue
                    error_list[i] = 'at ' + error_list[i]
                error_list.insert(0, error + ']')
            data = {'status' : 400, 'data' : error_list, 'type' : 'select'}
        
    return  data

def db_create(qry):  
    try :
        td_context = create_context(host="1.223.168.93:44240", username="dbc", password="dbc", logmech="TD2")    

        result = td_context.execute(qry)    
        data = result.fetchall()
        
        print("===============================")
        print("Success")
        print("===============================")
        data = {'status' : 200, 'data' : qry.splitlines(), 'type' : 'create'}
    except Exception as e :
        if 'Failed to connect to Teradata Vantage' in str(e) :
            data = {'status' : 404, 'data' : 'Failed to connect to Teradata Vantage'}
        else :
            if '[Error' in str(e) :
                err_index = str(e).find('[Error')
                err_index = str(e).index(']', err_index)
                error = str(e)[0 : err_index]
                error_list = str(e).strip(error).split('at ')
                for i in range(len(error_list)) :
                    if i == 0 :
                        error_list[i] = 'S' + error_list[i]
                        continue
                    error_list[i] = 'at ' + error_list[i]
                error_list.insert(0, error + ']')
            data = {'status' : 400, 'data' : error_list, 'type' : 'create'}
    return data
