# https://www.codingame.com/training/easy/blowing-fuse


def solution():
    num_devices, num_clicks, main_fuse_capacity = map(int, input().split())
    device_capacities = [0] + list(map(int, input().split()))
    device_state = [False] * (num_devices + 1)
    max_consumption = 0
    current_consumption = 0

    for device in map(int, input().split()):
        device_state[device] = not device_state[device]
        if device_state[device]:
            current_consumption += device_capacities[device]
        else:
            current_consumption -= device_capacities[device]

        if current_consumption > main_fuse_capacity:
            print('Fuse was blown.')
            return

        max_consumption = max(max_consumption, current_consumption)

    print('Fuse was not blown.')
    print('Maximal consumed current was {} A.'.format(max_consumption))


solution()
