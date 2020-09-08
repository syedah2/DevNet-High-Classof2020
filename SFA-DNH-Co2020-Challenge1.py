"""DevNet High - Class of 2020 - Challenge 1"""

import random
import ipaddress

# TODO: Write a print statement that displays both the type and value of 'ip'
ip = "10.1.1.200"
print(type(ip))
print("IP : ", ip)

# TODO: Write a conditional to print out if `iosversion` is less than or greater than 14
i = random.randint(12, 17)
print('i is {}'.format(i))
if  i < 14:
    print("i is less than 14")
else:
    print("i is greater than 14")

# TODO: Write a conditional that prints the serial number of the device
devices = ({'CAT9300':'XVNM1245ERGC'}, {'ISR4331':'VNMM8742THBX'}, {'NGFW2120':'EAQP4900RTJO'})
device = random.sample(devices, 1) [0]
device = list(device.values())[0]
for item in devices:
 #   print(item.values())
    print("Here is the serial number of the device {}. ".format(item.values()))

# Function for converting CIDR notation into 32-bit netmask (nothing to do here)
def cidr_to_netmask(ip_str):
    ip = ipaddress.IPv4Network(ip_str)
    return ip.with_netmask

'''
TODO: Call the function above few times to so that the input of IP network with CIDR displays the IP network with 32-bit netmask
Example:
Input would be '10.1.1.0/24' and when printed out the output would be '10.1.1.0/255.255.255.0'
'''
cidr1 = "192.168.1.0/24"
cidr1_output = cidr_to_netmask(cidr1)
print(cidr1_output)

cidr2 = "172.16.0.0/16"
cidr2_output = cidr_to_netmask(cidr2)
print(cidr2_output)

cidr3 = "10.0.0.0/8"
cidr3_output = cidr_to_netmask(cidr3)
print(cidr3_output)

print()
