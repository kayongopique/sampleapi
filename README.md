# sampleapi
## Project Overview
simpleapi is a work order service that helps in assigning worker ordes to the workers in the organization.<br>


### Main features
1. workers can create an account and log in.
4. workers can be allocated maximum of 5 work orders.
5. A worker can be deleted 
6. Users can delete work order.

### Quick Setup
a) Email me your username on Github so as grant you access to the repo as a collaborator.<br>
b) Open your terminal.<br>
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
|`/orders<orderId>/delete`|`DELETE`|Cancel the specific parcel delivery order|
|`/orders`|	`POST`|	Create an order|
|`/auth/signup`|`POST`|Register a worker|
|`/auth/login`|`POST `|Login a worker|
|`/workers/<workerId>/delete`|`delete `|delete a user |

# Authors
David Kayongo
