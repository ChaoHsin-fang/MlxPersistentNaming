import os
import subprocess
from jinja2 import Environment, FileSystemLoader

current_dir = os.path.dirname(os.path.abspath(__file__))
temp_dir = os.path.join(current_dir, 'templates')


def computing_net_busid():
    command = "lspci -vt | grep -i 'Mellanox.*ConnectX-7' | grep -oP '\\[\\K[0-9a-f]+(?=\\]----00\\.0)' | sort"
    output = subprocess.check_output(command, shell=True, text=True)
    busid_list = output.strip().split('\n')
    print(busid_list)
    env = Environment(loader=FileSystemLoader(temp_dir))
    template = env.get_template('70-persistent-net.rules')
    output = template.render(
                            busid_0=busid_list[0],
                            busid_1=busid_list[1],
                            busid_2=busid_list[2],
                            busid_3=busid_list[3],
                            busid_4=busid_list[4],
                            busid_5=busid_list[5],
                            busid_6=busid_list[6],
                            busid_7=busid_list[7],                            
                            )
    print(output)
if __name__ == '__main__':    
    computing_net_busid()