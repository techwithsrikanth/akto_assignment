First run 'interactsh-client' through this in one of the terminal

Then run 'interactsh-client -server' oast.pro

Go to the URL that will be given below once you run both these
Then go to https://app.interactsh.com/#/   
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



