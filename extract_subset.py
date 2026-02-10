"""
makes a dictionary that is a subset of another dictionary
"""

data = {
    'ip_1' :  1 ,
    'ip_2' :  50,
    'ip_3' :  100 ,
    'ip_4' :  200, 
    'ip_5' :  300,
    'ip_6' :  400,
    'ip_7' :  500,
    'ip_8' :  50
}

data1 = {key : value for key , value in data.items() if value > 100}

ips = {   
            'ip_2' ,
            'ip_4' ,
            'ip_8' ,
        }

data2 = {key : value for key , value in data.items() if key in ips}

for key , value in data2.items():
    print(f"Key --> {key}: Value --> {value}")