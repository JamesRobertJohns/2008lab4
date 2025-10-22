import numpy
import pandas as pd

from const import CSV_HEADERS, IP_TO_ORG

df = pd.read_csv("data/data_2.csv", header=None)
df.columns = CSV_HEADERS
print(df.head())
print(df.shape)
print()

print(80 * "=")
print("Exercise 4A")
print(80 * "=")
print("Top 5 Talkers\n")
top_5_talkers = (
    df.groupby("src_IP")["packet_size"]
    .size()
    .reset_index(name="num_packets")
    .sort_values(by="num_packets", ascending=False)
    .head(5)
)
print(top_5_talkers)
print(80 * "-")
print("Top 5 Listeners\n")
top_5_listeners = (
    df.groupby("dst_IP")["packet_size"]
    .size()
    .reset_index(name="num_packets")
    .sort_values(by="num_packets", ascending=False)
    .head(5)
)
print(top_5_listeners)
print(80 * "-")
print()


print(80 * "=")
print("Exercise 4B")
print(80 * "=")
print("Protocol Distribution\n")

protocol_distr = (
    df.groupby("ip_protocol")["packet_size"]
    .size()
    .reset_index(name="num_packets")
    .sort_values(by="num_packets", ascending=False)
)

total_packets = protocol_distr["num_packets"].sum()
print(f"Total number of packets is {total_packets}")
protocol_distr["pct_packets"] = (protocol_distr["num_packets"] / total_packets) * 100
protocol_distr["pct_packets"] = protocol_distr["pct_packets"].round(4)
print(protocol_distr)

print(80 * "-")
print()


print(80 * "=")
print("Exercise 4C")
print(80 * "=")

print("Top 5 application protocol\n")
top_5_app_1 = (
    df.groupby("x_dst_port")["packet_size"]
    .size()
    .reset_index(name="num_packets")
    .sort_values(by="num_packets", ascending=False)
    .head(5)
)
print(top_5_app_1)
print(80 * "-")
print()

df_well_known = df[df["x_dst_port"] <= 1023]
df_well_known = df_well_known[df_well_known["x_dst_port"] >= 1]

print("Top 5 application protocol [alternative answer]\n")
top_5_app = (
    df_well_known.groupby("x_dst_port")["packet_size"]
    .size()
    .reset_index(name="num_packets")
    .sort_values(by="num_packets", ascending=False)
    .head(5)
)
print(top_5_app)
print(80 * "-")
print()


print(80 * "=")
print("Exercise 4D")
print(80 * "=")
SAMPLING_RATE = 2048
total_size = df["ip_size"].sum() * SAMPLING_RATE
print(f"total traffic is {total_size/1e6} MB")
print()
print(80 * "-")
print()


print(80 * "=")
print("Exercise 4E")
print(80 * "=")
print("Top 5 Communication Pairs\n")
top_5_pair = (
    df.groupby(["src_IP", "dst_IP"])["packet_size"]
    .size()
    .reset_index(name="num_packets")
    .sort_values(by="num_packets", ascending=False)
    .head(5)
)
top_5_pair["src_org"] = top_5_pair["src_IP"].map(IP_TO_ORG)
top_5_pair["dst_org"] = top_5_pair["dst_IP"].map(IP_TO_ORG)
top_5_pair["is_top5_talker"] = top_5_pair["src_IP"].isin(top_5_talkers["src_IP"])
top_5_pair["is_top5_listener"] = top_5_pair["dst_IP"].isin(top_5_listeners["dst_IP"])
print(top_5_pair)
print(80 * "-")
print()
