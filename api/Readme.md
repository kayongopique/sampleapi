# send_it; Challenge 3
## Project Overview
simpleapi is a workorder service that helps in assigning work orders to the workers in the organization.<br>


### Main features
1. User create an account for a worker and log them in.
2. workers can be allocated maximum of 5 work orders.
3. the same work order can noy be assigned twice to a particular worker.
4. User can delete a worker.
5. User can delete a work order.

### Quick Setup
a) Open your terminal.<br>
c) You can now write `cd simpleapi` to enter into directory. <br>
d) Download the virtual environment with `pip install virtual env`
d) Create a virtual environment and then `pip install -r requirements.txt` <br>
e) Now run the app using `python run.py runserver` <br>

### API Features:

|URL Endpoint	|HTTP Method	|Description|
|-------------|-------------|-----------|
|`/orders`	|`GET`|	Fetch all orders|
|`/workers/orders`|	`GET`|Fetch all orders by a specific worker|
|`/orders<orderId>/delete`|`DELETE`|delete the specific work order|
|`/orders`|	`POST`|	Create a work order|
|`/auth/signup`|`POST`|Register a worker|
|`/auth/login`|`POST `|Login a worker|
|`/workers/<workerId>/delete`|`delete `|delete a worker |

# Authors
David Kayongo
