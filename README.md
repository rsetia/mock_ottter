# mock_ottter

Mocks the response of services running the IFTTT API based on the query path alone. 

## run: 

docker build -t mock-ottter .

docker run -it --rm --name mock-ottter -p 5000:5000  mock-ottter

## examples: 

curl localhost:5000/facebook/ifttt/v1/webhooks/connnection/enabled

curl localhost:5000/facebook/ifttt/v1/triggers/new_status_message_by_you
