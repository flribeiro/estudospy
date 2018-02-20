def validateIpAddress(ip):
    try:
        octets = ip.split('.')
        if(len(octets) == 4 and all(0 <= int(octet) < 256 for octet in octets)):
            print("Valid IP Address")
            return True
        else:
            print("Invalid IP Address")
            return False
    except:
        print("Invalid input")
        return False


# ip1 = "192.168.1.8"
# ip2 = "xyz"
# ip3 = "189.678.999.0"

# validateIpAddress(ip1)
# validateIpAddress(ip2)
# validateIpAddress(ip3)

ip = input("Digite um IP para validar: ")
validateIpAddress(ip)
