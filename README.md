# sampleapi
## Project Overview
simpleapi is a work order service that helps in assigning worker ordes to the workers in the organization.<br>


### Main features
1. User create an account for a worker and log them in.
2. Workers can be allocated maximum of 5 work orders.
3. The same work order can noy be assigned twice to a particular worker.
4. User can delete a worker.
5. User can delete a work order.

### Quick Setup
#### First option 
1) use the following URL https://git.heroku.com/flask-sampleapi.git to access the api either in postman or any application of your choice.<br>
2) If this fails please see option 2 below.
#### Second option
a) Email me your username on Github so as grant you access to the repo as a collaborator.<br>
b) Then Open your terminal.<br>
c) Type in the command git clone and paste in this link https://github.com/kayongopique/sampleapi.git.
<br>
d) You can now write `cd simpleapi` to enter into directory. <br>
e) Create a virtual environment and then `pip install -r requirements.txt` <br>
f) Now run the app using `python run.py runserver` <br>

### API Features:

|URL Endpoint	|HTTP Method	|Description|
|-------------|-------------|-----------|
|`/orders`	|`GET`|	Fetch all orders|
|`/orders`	|`POST`| Assign an order to a worker|
|`/workers/orders`|	`GET`|Fetch all orders by a specific worker|
|`/orders<orderId>/delete`|`DELETE`|delete the specific work order|
|`/orders`|	`POST`|	Create a work order|
|`/auth/signup`|`POST`|Register a worker|
|`/auth/login`|`POST `|Login a worker|
|`/workers/<workerId>/delete`|`delete `|delete a worker |

# Authors
David Kayongo
