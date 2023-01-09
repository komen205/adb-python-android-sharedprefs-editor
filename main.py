from ppadb.client import Client as AdbClient
client = AdbClient(host="127.0.0.1", port=5037)
devices = client.devices()

if(len(devices) > 1):
    print("You have more than one device")
    exit;
device = devices[0]

print('Enter the package name:')
package_name = input()

print('Enter the shared preferences file:')
xml_file = input()
print(f"cp /data/data/{package_name}/shared_prefs/{xml_file} /storage/emulated/0/temp.xml")
device.shell(f"su -c cp /data/data/{package_name}/shared_prefs/{xml_file} /storage/emulated/0/temp.xml")
device.pull(f"/storage/emulated/0/temp.xml", "temp.xml")

print(f"location /data/data/{package_name}/shared_prefs/{xml_file}")
print("What is the value you want to change?")
parameter = input()

print("What is the value you want to go?")
parameter_fix = input()

file = open("temp.xml", "rt")
data = file.read()
print(data)
data = data.replace(parameter, parameter_fix)
print(data)
file.close()
file = open("temp.xml", "wt")
file.write(data)
file.close()

device.push("temp.xml", "/storage/emulated/0/temp.xml")
device.shell(f"su -c cp /storage/emulated/0/temp.xml /data/data/{package_name}/shared_prefs/{xml_file}")