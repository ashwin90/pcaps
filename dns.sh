#!/bin/sh

content=`ls $1`
for file in $content
do
    base="${file%.*}.tcp2"
    path="$1/$file"
    tshark -R "http" -T fields -e tcp.stream -e tcp.srcport -e tcp.dstport -e ip.src_host -e ip.dst_host -e frame.time_relative -e http.content_length -e http.host -e tcp.reassembled.length -e tcp.analysis.retransmission -E header=y -r $path > $base
    #tshark -R "dns" -r $path -T fields -e frame.number -e frame.len -e dns.id -e frame.time_relative -e ip.src_host -e ip.dst_host -e dns.time -E header=y > $base
    #tshark -R "dns.response_to" -r $path -T fields -e dns.id -e dns.time -E header=y > $base
done
