from netmiko import ConnectHandler

def CreateConnection():
    connection = ConnectHandler(
    device_type="cisco_ios",
    host="10.10.1.2",
    username="Cisco",
    password="Class",
    secret="Class",
    global_delay_factor = 2)    
    connection.enable()
    return connection   