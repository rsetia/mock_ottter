# mock_ottter

Mocks the response of services running the IFTTT API based on the path alone. 

## run: 

install flask

`FLASP_APP=ottter.py flask run` 

## examples: 

curl localhost:5000/facebook/ifttt/v1/webhooks/connnection/enabled

curl localhost:5000/facebook/ifttt/v1/triggers/new_status_message_by_you
