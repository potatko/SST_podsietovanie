import ipaddress, math,os
default_ip = input("Zadaj adresu siete: ")

def next_power_of_2(n):  
    return int(math.pow(2, math.ceil(math.log2(n+2))))


n = int(input("Zadaj pocet podsieti: "))

podsiete = []
newip = default_ip
for i in range(n):
    podsiete.append(int(input(f"Zadaj pocet pocitacov v {i+1} podsieti: ")))

podsiete.sort(reverse=True)
os.system('cls')
for i in podsiete:
    next2 = next_power_of_2(i)
    alokacia = next2 - 2
    temp = int(math.log2(next2))
    prefix = 32 - temp
    IP_Addr = ipaddress.ip_interface((str(newip)+"/"+str(prefix)))
    
    Net_Addr = IP_Addr.network
    Mask = IP_Addr.with_netmask
    broadcast_address = Net_Addr.broadcast_address
    print('Nazov podsiete: ', str(i))
    print('Alokacia : ', str(alokacia))
    print('Adresa siete : ', str(Net_Addr).split('/')[0])
    print('Maska : ', Mask.split('/')[1])
    print('1. pouzitelna IP : ' , list(Net_Addr.hosts())[0])
    print('Posledna pouzitelna IP : ' , list(Net_Addr.hosts())[-1])
    print('Broadcast Address : ' , broadcast_address)
    print("------------------------------------------")
    newip = broadcast_address+1
    
input("Stlac akukolvek klavesu na pokracovanie")



