"""
@Authors:
	Jeremy Peters (jsp7075)
	Randall Weber (rjw9659)
	Julian Mato-Hernandez (jmm5458)
"""

from filter_packets import *
from packet_parser import *
from compute_metrics import *
import csv

def main():
    inputNodes = ["Node1.txt",
                  "Node2.txt",
                  "Node3.txt",
                  "Node4.txt"]

    outputNodes = ["Node1_filtered.txt",
                   "Node2_filtered.txt",
                   "Node3_filtered.txt",
                   "Node4_filtered.txt"]

    ipNodes = ["192.168.100.1",
               "192.168.100.2",
               "192.168.200.1",
               "192.168.200.2"]

    headerNodes = []

    computedNodes = []

    for i in range(len(inputNodes)):
        filter(inputNodes[i], 'ICMP', outputNodes[i])
    for temp in outputNodes:
        headerNodes.append(parse(temp))
    for i in range(len(headerNodes)):
        computedNodes.append(run(headerNodes[i], ipNodes[i]))

    reformattedResults = []
    for temp_1 in computedNodes:
        temp_2 = []
        for temp_3 in temp_1:
            if type([]) == type(temp_3):
                for temp_4 in temp_3:
                    temp_2.append(temp_4)
            else:
                temp_2.append(temp_3)
        reformattedResults.append(temp_2)

    adjustedResults = []
    for temp_1 in reformattedResults:
        temp_2 = []
        temp_2.append(str(abs(float(temp_1[0]))))                                #ICMP requests sent                    @index 0
        temp_2.append(str(float(temp_1[1]) + float(temp_1[4])))                  #Totall bytes sent in frame            @index 1
        temp_2.append(str(float(temp_1[2]) + float(temp_1[5])))                  #Totall bytes sent in ICMP message     @index 2
        temp_2.append(str(abs(float(temp_1[3]))))                                #ICMP replies sent                     @index 3
        temp_2.append(str(abs(float(temp_1[6]))))                                #ICMP requests recieved                @index 4
        temp_2.append(str(float(temp_1[7]) + float(temp_1[10])))                 #Totall bytes Recieved in frame        @index 5
        temp_2.append(str(float(temp_1[8]) + float(temp_1[11])))                 #Totall bytes Recieved in ICMP message @index 6
        temp_2.append(str(abs(float(temp_1[9]))))                                #number of icmp Reply Recieved         @index 7
        temp_2.append(str(abs(float(temp_1[12]))))                               #Round trip time                       @index 8
        temp_2.append(str(abs(float(temp_1[13]))))                               #Echo request throughput               @index 9
        temp_2.append(str(abs(float(temp_1[14]))))                               #Echo request goodput                  @index 10
        temp_2.append(str(abs(float(temp_1[15]))))                               #average reply delay                   @index 11
        temp_2.append(str(abs(float(temp_1[16]))))                               #hop average                           @index 12
        adjustedResults.append(temp_2)


    with open('MiniProject2Output.csv', 'w', newline='') as file:
        nodeNum = 1
        for node in  adjustedResults:
            nodeStr = str("Node" + str(nodeNum))
            metricResults = node
            writer = csv.writer(file)
            writer.writerow([nodeStr])
            writer.writerow([""])
            # Emtpy Line

            writer.writerow(["Echo Requests Sent", "Echo Requests Received", "Echo Replies Sent", "Echo Replies Received"])
            writer.writerow([metricResults[0], metricResults[4], metricResults[3], metricResults[7]])
            writer.writerow(["Echo Requests Bytes Sent (bytes)", "Echo Requests Data Sent (bytes)"])
            writer.writerow([metricResults[1], metricResults[2]])
            writer.writerow(["Echo Requests Bytes Received (bytes)", "Echo Requests Data Received (bytes)"])
            writer.writerow([metricResults[5], metricResults[6]])
            writer.writerow([""])
            # Emtpy Line

            # Last block of metrics commented for now
            writer.writerow(["Average RTT",  metricResults[8]])
            writer.writerow(["Echo Request Throughput (kB/sec)",  metricResults[9]])
            writer.writerow(["Echo Request Goodput (kB/sec)",  metricResults[10]])
            writer.writerow(["Average Reply Delay (microseconds)",  metricResults[11]])
            writer.writerow(["Average Echo Request Hop Count",  metricResults[12]])
            writer.writerow([""])
            # Emtpy Line
            nodeNum += 1
	


if __name__ == '__main__':
    main()
