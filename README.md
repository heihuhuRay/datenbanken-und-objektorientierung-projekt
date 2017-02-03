README v0.0 / 03 February 2017
# Datenbanken und Objektorientierung Projekt

## Introduction

The library is aimed to offer a CRUD (create, read, update and delete) features, using PostgreSQL as database.

## Usage

Put "DBConn.php" into the work file. To initiate the application, simply create a new contructor of it. 

```php
	$database = new DB;						// create a new contructor
	$DB -> dbConn();							// connect to the database
	$DB -> runQuery($query);			// execute query and return the result
	$DB -> freeResult($result);		// free result memory
	$DB -> dbClose();							// close the connection
```

## Contributing

If one wants to contribute to the project, one can easily clone the repository from [here] (https://github.com/yiweihsu/datenbanken-und-objektorientierung-projekt)

## Help

If there's any question or bug related to the project, please feel free to contact us: yi-wei.hsu[at]s2015.tu-chemnitz.de or juncheng.hu[at]s2015.tu-chemnitz.de

## Installation

### Requirements

The project is web-based, using PHP as server programming language. To run the application, one needs the related development environment to run the program.

### Installation

1. Fork this repository on Github.

2. Clone your forked repository (not our original one) to your hard drive with git clone https://github.com/YOURUSERNAME/datenbanken-und-objektorientierung-projekt.git

3. ```cd datenbanken-und-objektorientierung-projekt```

4. Set the configuration such as "hostname", "port", "databse username", "database password" in DBConn.php file.

5. Now you can play arund the application on valid server localhost://YOURSERVERPORT

### Configuration

Set "database name", "username", and "password" on the file DBConn.php

## Credits

Authors: Yi-Wei Hsu, Juncheng Hu
