# words = ["devil", "wolf", "lamina", "flow", "peek", "retool",
#          "lived", "keep", "panel", "animal", "looter", "lizard"]

# for word in range(0, len(words)-2):
#     for secondWord in range(word+1, len(words)-1):
#         if words[word][::-1] == words[secondWord]:
#             print(words[word] +" Is the same as " + words[secondWord]+ " reversed!")

# import re


# linjer = ["Hvad hedder du?",
# "Sikke et vejr vi har!",
# "Hvad har du nu gjort?",
# "Pyt med det.",
# "Tror du, det er rigtigt?"]


# for sentence in linjer:
#     words = sentence.split()
#     print("number of words:",len(words))
#     print("Number of characters:", len(re.sub('[^A-Za-z0-9]+', '', sentence)))
#     print(re.sub('[^A-Za-z0-9]+', '', words[-1]))

class InterFaceObj():
    
    def __init__(self, name, ipAdd,status,proto):
        self.name = name
        self.ipAdd = ipAdd
        self.status = status
        self.proto = proto



from netmiko import ConnectHandler
from netmiko import NetMikoAuthenticationException
from netmiko import NetMikoTimeoutException 



connection = ConnectHandler(
    device_type="cisco_ios",
    host="10.10.1.2",
    username="Cisco",
    password="Class",
    secret="Class")

comm = "show ip int brief"
interfaces = []

try:
    output = connection.send_command(comm, use_textfsm=True)
    for interface in output:
        inter = InterFaceObj(interface["intf"],interface["ipaddr"],interface["status"],interface["proto"])
        interfaces.append(inter)
except NetMikoTimeoutException:
    print("Bad stuff happened")
except NetMikoAuthenticationException:
    print("Check if vty lines are full")
finally:
    connection.disconnect()
    for inter in interfaces:
        print(inter.name)


# output = connection.send_command_timing("enable", strip_prompt=False, strip_command=False)
# output += connection.send_command_timing("Class", strip_prompt=False, strip_command=False)

# output += connection.send_command_timing(command, strip_prompt=False, strip_command=False )

# if "startup-config" in output:
#     output += connection.send_command_timing(
#         command_string="\n",
#         strip_prompt=False,
#         strip_command=False
#     )
    
# connection.disconnect()

# print(output)