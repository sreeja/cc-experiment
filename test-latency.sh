curl "http://localhost:6001/"
curl "http://localhost:6002/"
curl "http://localhost:6003/"
curl "http://localhost:6004/"
curl "http://localhost:6005/"

./latency.sh
# ./latency-cent.sh
# ./latency-clust.sh
# ./latency-dist.sh

curl "http://localhost:6001/"
curl "http://localhost:6002/"
curl "http://localhost:6003/"
curl "http://localhost:6004/"
curl "http://localhost:6005/"