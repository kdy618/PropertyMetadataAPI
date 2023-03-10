# Septic Sewer API 

API package leveraging [HouseCanary API Client](https://github.com/housecanary/hc-api-python) to retrieve home data; specifically to determine whether a property has a septic as its sewer system by passing in address and zipcode. Currently, this only supports a single property per request. 

##  Quickstart

This app can be run `Docker` and `docker-compose`.  


## 1. Create .env 

Copy **.env.example** into **.env** and setup the correct values.
See email for HouseCanary API key amd secret. 

## 2. Build and Start

To run the development version of the app: 

```bash
docker-compose up flask-dev
```

## 3. Visit Api Route

Go to [http://localhost:8080/api/v1/property/sewer/septic?address=7904+Verde+Springs+Dr&zip_code=89128&api_key=10987654321](http://localhost:8080/api/v1/property/sewer/septic?address=7904+Verde+Springs+Dr&zip_code=89128&api_key=10987654321). 

The url constructed above contains a valid test address that would return a boolean value that denotes whether the property has a septic system. 

Since this api is leveraging HouseCanary Property API client, to mimic property data results, leverage the test addresses provided [here](https://github.com/housecanary/hc-api-python/blob/master/notebooks/using-test-credentials.ipynb). 

To view full property data for the test address, use the url [http://localhost:8080/api/v1/property/sewer/septic/debug](http://localhost:8080/api/v1/property/sewer/septic/debug) to inspect and debug other property attributes. To change the address, go to [debug_septic_sewer_system()](https://github.com/kdy618/PropertyMetadataAPI/blob/main/hometapapi/api/v1/views.py#L39) and update the string values passed with the other test addresses listed from [here](https://github.com/housecanary/hc-api-python/blob/master/notebooks/using-test-credentials.ipynb). 

## 4. Run tests 

To run tests:

```bash
docker-compose run --rm manage test
```

# Architecture Diagram
![SewerApi drawio](https://user-images.githubusercontent.com/8558956/215924684-d619e2ca-f621-48b9-9bf7-89891bbdc3ca.png)

