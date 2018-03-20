# pysiri2validator

This provides a simple validator for the SIRI 2.0 specification written in Python 3.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

It is recommended that you use pipenv. 
```
$ pipenv install
```
will install the dependencies (lxml and requests).

## Usage

### Validate xml files
````
python main.py example_request/exs_stopMonitoring_response_simple.xml
````

### Validate HTTP/HTTPS endpoints (GET requests only)

````
$ python main.py https://raw.githubusercontent.com/laidig/siri-20-java/master/examples/siri_exm_CM/exc_connectionMonitoringDistributor_response.xml
````

## Built With

* [Pipenv](https://docs.pipenv.org)
* [lxml](http://lxml.de)
* [requests](http://python-requests.org)


## Authors

* **Tony Laidig** - [Github](https://github.com/laidig)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* see code comments for shoutouts!
