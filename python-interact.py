from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

current_server = "pqyskgolvynaygwqcvwxcd63ig98gjx31.oast.fun"
interactions = [
    {"caller_ip": "162.158.109.9", "timestamp": "2024-02-23 03:35:48"},
    {"caller_ip": "162.158.109.9", "timestamp": "2024-02-23 03:35:48"},
    {"caller_ip": "162.158.109.196", "timestamp": "2024-02-23 03:35:48"},
    {"caller_ip": "104.28.193.172", "timestamp": "2024-02-23 03:35:49"},
    {"caller_ip": "104.28.193.172", "timestamp": "2024-02-23 03:36:05"},
    {"caller_ip": "104.28.225.172", "timestamp": "2024-02-23 03:38:42"},
    {"caller_ip": "104.28.225.172", "timestamp": "2024-02-23 03:38:47"},
    {"caller_ip": "104.28.193.166", "timestamp": "2024-02-23 03:48:24"},
    {"caller_ip": "104.28.193.166", "timestamp": "2024-02-23 03:48:27"},
    {"caller_ip": "104.28.193.166", "timestamp": "2024-02-23 03:49:48"},
    {"caller_ip": "104.28.193.166", "timestamp": "2024-02-23 03:49:52"},
]

@app.route('/api/getURL', methods=['GET'])
def get_url():
    return jsonify({"url": current_server})

@app.route('/api/getInteractions', methods=['GET', 'POST'])



@app.route('/api/getInteractions', methods=['GET', 'POST'])
def get_interactions():
    if request.method == 'POST':
        req_data = request.get_json()
        url = req_data.get('url')
        start_timestamp = req_data.get('start_timestamp')
        end_timestamp = req_data.get('end_timestamp')
    else:
        url = request.args.get('url')
        start_timestamp = request.args.get('start_timestamp')
        end_timestamp = request.args.get('end_timestamp')

    if url == current_server:
        if start_timestamp and end_timestamp:
            start_datetime = datetime.fromisoformat(start_timestamp)
            end_datetime = datetime.fromisoformat(end_timestamp)
            filtered_interactions = [interaction for interaction in interactions if
                                     start_datetime <= datetime.fromisoformat(interaction['timestamp']) <= end_datetime]
            return jsonify({"interactions": filtered_interactions})
        else:
            return jsonify({"interactions": interactions})
    else:
        return jsonify({"error": "Invalid URL"})


if __name__ == '__main__':
    app.run(debug=True)



    
'''
first run 'interactsh-client' through this in one of the terminal
then run 'interactsh-client -server' oast.pro
go to the URL that will be given below once you run both these
then go to https://app.interactsh.com/#/   
here run your server URL that you got through running in the terminal
our client will be connected to server, now we can fetch all the timestamps and caller_ip..


go to windows terminal and run this
$body = @{
    url = "pqyskgolvynaygwqcvwxcd63ig98gjx31.oast.fun"  (change this URL to the one you get in interactsh web client)
    start_timestamp = "2024-02-23 03:35:00"
    end_timestamp = "2024-02-23 03:38:00"
} | ConvertTo-Json

to see the ip run and the timestamps these commands needs to be run...here we are giving timestamps to collect between certain timestamps
$response = Invoke-RestMethod -Uri "http://127.0.0.1:5000/api/getInteractions" -Method Post -Body $body -ContentType "application/json"
$response.interactions


'''