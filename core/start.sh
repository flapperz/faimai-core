echo starting faimai-core
export UUID=node-1
node ./alfred/app.js
exec python3 -u sender.py &
exec python3 -u receiver.py