# sampleapi
## Project Overview
simpleapi is a work order service that helps in assigning worker orders to the workers in the organization. The administrator can also monitor and track work orders assigned to specific works. The workers can create their accounts with the system and view only details pertaining orders assigned to them and their personal data.<br>


### Main features
1. User (superuser ) can create an account for a worker and log them in.
2. Worker can create his own account and login also
3. Workers can be allocated maximum of 5 work orders.
4. The same work order can not be assigned twice.
5. Worker can only view orders assigned to him/her not others
6. Only User( superuser ) has got permission to assign orders but a worker doesn't.
7. Only User( superuser) has got permision to delete a worker and a worker order

### Quick Setup
#### First option 
1) use the following URL https://git.heroku.com/flask-sampleapi.git to access the api either in postman or any application of your choice.<br>
2) If this fails please see option 2 below.
#### Second option
a) Then Open your terminal.<br>
b) Type in the command git clone and paste in this link https://github.com/kayongopique/sampleapi.git.
<br>
d) You can now write `cd simpleapi` to enter into directory. <br>
e) Create a virtual environment and then `pip install -r requirements.txt` <br>
f) set FLASK_APP=run.py, if using bash export FLASK_APP=run.py<br>
h) Now run the app using `flask run`<br>
i) For details how to set up and run app and tests check `/sampleapi/docs/config.yml` file

### API Features:
NOTE: For details on how to use below routes visit the docs `/sampleapi/docs`

|URL Endpoint	|HTTP Method	|Description|
|-------------|-------------|-----------|
|`/orders`	|`GET`|	Fetch all orders|
|`/orders`	|`POST`| Assign an order to a worker|
|`/orders/worker/<workerId>`|	`GET`|Fetch all orders by a specific worker|
|`/orders<orderId>/delete`|`DELETE`|delete the specific work order|
|`/orders`|	`POST`|	Create a work order|
|`/auth/signup`|`POST`|Register a worker |
|`/auth/login`|`POST `|Login a worker |
|`/workers/<workerId>/delete`|`delete `|delete a worker |

# Authors
David Kayongo
