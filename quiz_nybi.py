# quiz_1_api
#
# input
# Network ID
# Subnets Required
#
# Return
# Subnet Mask
# 1st Available Host Address of Subnet 1
# Max # of hosts/subnet
#
# quiz_2_api
#
# input
# IP Address
#
# Return
# Network Address
# Broadcast Address
# Subnet Mask


def get_ip_list(ip):
    return ip.strip().split('.')


def get_str_ip(ip_list):
    return f'{ip_list[0]}.{ip_list[1]}.{ip_list[2]}.{ip_list[3]}'


def check_ip(ip):
    ip = get_ip_list(ip)
    if len(ip) != 4:
        return False
    for octet in ip:
        if not octet.isdigit():
            return False
        if int(octet) > 255:
            return False
    return True


def check_subnet(slash):
    if not slash.isdigit():
        return False
    if int(slash) < 8 or int(slash) > 31:
        return False
    return True


def check_full_ip(full_ip):
    ip_address, slash = full_ip.strip().split(' /')
    if check_ip(ip_address) and check_subnet(slash):
        return True
    return False


def get_bin_subnet_mask(slash):
    return '1' * int(slash) + '0' * (32 - int(slash))


def get_subnet_mask(slash):
    bin_mask = get_bin_subnet_mask(slash)
    subnet_mask = [bin_mask[:8], bin_mask[8:16], bin_mask[16:24], bin_mask[24:]]
    for i, octet in enumerate(subnet_mask):
        subnet_mask[i] = int(octet, 2)
    return get_str_ip(subnet_mask)


def get_host_num(slash):
    return 2 ** (32 - int(slash)) - 2


def get_slash(net_ip, subnet_num):
    ip = get_ip_list(net_ip)
    zero = ip.count('0')
    delta_slash = 0
    if bin(int(subnet_num)).split('b')[1] not in ['0', '1']:
        delta_slash = len(bin(int(subnet_num) - 1).split('b')[1])
    return str(8 * (4 - zero) + delta_slash)


def get_second_subnet_first_host_ip(net_ip, slash):
    net_ip = get_ip_list(net_ip)
    for i in range(4):
        if net_ip[i] == '0':
            net_ip[i] = str(256 // 2 ** (int(slash) % 8))
            break
    net_ip[-1] = str(int(net_ip[-1]) + 1)
    return get_str_ip(net_ip)


def get_network_address(ip, slash):
    ip_list = get_ip_list(ip)
    subnet_mask = get_ip_list(get_subnet_mask(slash))
    network_address = []
    for i, octet in enumerate(subnet_mask):
        if octet == '255':
            network_address.append(ip_list[i])
        elif octet == '0':
            network_address.append('0')
        else:
            network_address.append(str((int(ip_list[i]) // (256 - int(octet))) * (256 - int(octet))))
    return get_str_ip(network_address)


def get_broadcast_address(ip, slash):
    ip_list = get_ip_list(ip)
    subnet_mask = get_ip_list(get_subnet_mask(slash))
    network_address = []
    for i, octet in enumerate(subnet_mask):
        if octet == '255':
            network_address.append(ip_list[i])
        elif octet == '0':
            network_address.append('255')
        else:
            network_address.append(str((((int(ip_list[i]) // (256 - int(octet))) + 1) * (256 - int(octet))) - 1))
    return get_str_ip(network_address)


def quiz_1_api(net_ip, subnet_required):
    if check_ip(net_ip):
        net_slash = get_slash(net_ip, subnet_required)
        return get_subnet_mask(net_slash), get_second_subnet_first_host_ip(net_ip, net_slash), get_host_num(net_slash)


def quiz_2_api(full_ip):
    if check_full_ip(full_ip):
        ip_address, slash = full_ip.strip().split(' /')
        return get_network_address(ip_address, slash), get_broadcast_address(ip_address, slash), get_subnet_mask(slash)
