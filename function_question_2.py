def sweet_count(n, *packet):
    print(n)
    print(packet)
    min_packet = packet[0]

    for i in packet:
        if min_packet < i:
            min_packet = i


sweet_count(5,15,20,18,23,21 )

