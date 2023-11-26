from scapy.all import rdpcap, PacketList
from datetime import datetime, timedelta

# 读取 PCAP 文件
packets = rdpcap('files/part2.pcap')

# 定义超时设置
timeouts = [1, 10, 60, 120, 1800]  # 单位为秒

# 创建一个字典来存储不同超时设置下的流数量
flows_for_timeouts = {}

for timeout in timeouts:
    # 初始化流列表和当前流的数据包列表
    flows = []
    current_flow_packets = []
    last_packet_time = None

    for packet in packets:
        if 'IP' in packet and 'TCP' in packet:
            # 获取当前数据包的时间戳
            current_packet_time = datetime.fromtimestamp(float(packet.time))

            # 检查是否是流的第一个数据包或者当前数据包与上一个数据包的时间差是否超过了超时设置
            if last_packet_time is None or (current_packet_time - last_packet_time).total_seconds() > timeout:
                # 如果是新的流，先保存当前流，然后开始一个新的流
                if current_flow_packets:
                    flows.append(PacketList(current_flow_packets))
                current_flow_packets = [packet]
            else:
                # 否则，将数据包添加到当前流中
                current_flow_packets.append(packet)

            # 更新最后一个数据包的时间
            last_packet_time = current_packet_time

    # 保存最后一个流
    if current_flow_packets:
        flows.append(PacketList(current_flow_packets))

    # 记录当前超时设置下的流数量
    flows_for_timeouts[timeout] = len(flows)

for timeout, count in flows_for_timeouts.items():
    print(f"Timeout: {timeout} seconds, Flow Count: {count}")
