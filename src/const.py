CSV_HEADERS = [
    "type",
    "agent_IP_addr",
    "inputPort",
    "outputPort",
    "src_MAC",
    "dst_MAC",
    "ethernet_type",
    "in_vlan",
    "out_vlan",
    "src_IP",
    "dst_IP",
    "ip_protocol",
    "ip_tos",
    "ip_ttl",
    "x_src_port",
    "x_dst_port",
    "tcp_flag",
    "packet_size",
    "ip_size",
    "sampling_rate",
]

PORT_TO_SERVICE = {}

IP_TO_ORG = {
    "13.107.4.50": "Microsoft Corporation (MSFT)",
    "130.14.250.7": "National Library of Medicine (NLM-Z)",
    "155.69.160.38": "Nanyang Technological University (ORG-NTU2-AP)",
    "171.67.77.19": "Stanford University (STANFO-Z)",
    "155.69.199.255": "Nanyang Technological University (ORG-NTU2-AP)",
    "137.132.228.33": "National University of Singapore (ORG-NUOS1-AP)",
    "192.122.131.36": "A*STAR (ORG-AA1-AP)",
    "202.51.247.133": "NUS Gigapop (ORG-NG2-AP)",
    "137.132.228.29": "National University of Singapore (ORG-NUOS1-AP)",
    "103.37.198.100": "A*STAR (ORG-AA1-AP)",
    "129.99.230.54": "National Aeronautics and Space Administration (NASA-Z)",
    "137.132.22.74": "National University of Singapore (ORG-NUOS1-AP)",
    "137.132.228.42": "National University of Singapore (ORG-NUOS1-AP)",
    "137.131.17.212": "Oracle Corporation (ORACLE-4)",
    "155.69.252.133": "Nanyang Technological University (ORG-NTU2-AP)",
    "138.75.242.36": "M1 LIMITED (ORG-ML7-AP)",
}

def main():
    for i, v in enumerate(CSV_HEADERS):
        print(i, ": ", v)


if __name__ == "__main__":
    main()
