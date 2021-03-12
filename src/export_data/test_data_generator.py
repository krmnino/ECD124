import datetime
import random

def generate_data(start_date, fields, data_points):
    out = 'Date,'
    with open('./data/test_data.csv', 'w') as file:
        for i in fields.keys():
            out += i + ','
        out += '\n'
        for i in range(0, data_points):
            out += datetime.datetime.strftime(start_date, '%Y-%m-%d %H:%M:%S') + ','
            for j in fields.keys():
                out += str(random.randrange(fields[j][0], fields[j][1] + 1, 1)) + ','
            out += '\n'
            start_date  += datetime.timedelta(0, 5)
        file.write(out)
    file.close()      
    

fields = {
    'Battery_Voltage' : (200, 500),
    'Battery_Current' : (10, 70),
    'Battery_Max_Discharge_Power' : (0, 200),
    'Battery_Max_Regen_Power' : (0, 200),
    'Battery_State' : (0, 5),
    'Battery_Temperature' : (0, 200),
    'WEMS_Target_Power' : (0, 100),
    'WEMS_Power_Direction' : (0, 1),
}

date_str = '2021-01-05 08:00:00'
start_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
data_points = 300

generate_data(start_date, fields, data_points)