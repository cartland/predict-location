cat LocationHistory.json | grep "^    \"timestampMs\" : " > timestampMs.txt
cat LocationHistory.json | grep "^    \"latitudeE7\" : " > latitudeE7.txt
cat LocationHistory.json | grep "^    \"longitudeE7\" : " > longitudeE7.txt
