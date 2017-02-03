README v0.0 / 03 February 2017
# Datenbanken und Objektorientierung Projekt

## Introduction

The library - "Datenbanken und Objektorientierung Projekt" offers a complete CRUD systems based on relational database management system, which can let users to implement "create", "read", "update" and "delete" actions easily.

## Spec

* Client (UI) Programming Languages: HTML/CSS/JavaScript
* Server Programming Language: PHP 5.6.25 (cli)
* Database: PostgreSQL 9.6.1

## Usage

Put "DBConn.php" into your work file. To initiate the application, simply create a new contructor. 

```php
	/* init */
	$database = new DB;	// create a new contructor
	$DB -> dbConn();	// connect to the database

	/* query example */

	// insert action
	$query = "
		INSERT INTO order_items(prod_id, ser_id, ret_id) 
		VALUES (
			'" . $_POST['product'] . "',
			'". $_POST['service'] ."',
			'". $_POST['retail'] ."'
	);";

  // join action
  $query = '
  SELECT order_items.o_id, order_items.o_num, product.prod_name, product.cpu_model, product.scr_size, product.prod_price, service.ser_name, retailer.ret_name
  FROM product
 	  JOIN order_items
 		  ON product.prod_id = order_items.prod_id
 	  JOIN service
 		  ON order_items.ser_id = service.ser_id
 	  JOIN retailer
 		  ON order_items.ret_id = retailer.ret_id
  ';

  // combine multiple tables with condition statement
	$query = '
	  SELECT order_items.o_id, order_items.o_num, product.prod_name, product.cpu_model, product.scr_size, product.prod_price, service.ser_name, retailer.ret_name
		FROM product, order_items, service, retailer
		WHERE order_items.prod_id = product.prod_id 
		AND order_items.ser_id = service.ser_id
		AND order_items.ret_id = retailer.ret_id
	';

  // fetch the array from databse
  while ($arr = pg_fetch_array($result, null, PGSQL_ASSOC)) {
    echo '<tr>';
    echo '<td>' . $arr['o_id'] . '</td>';
    echo '<td>' . $arr['o_num'] . '</td>'; 
    echo '<td>' . $arr['prod_name'] . '</td>'; 
    echo '<td>' . $arr['cpu_model'] . '</td>'; 
    echo '<td>' . $arr['scr_size'] . '</td>'; 
    echo '<td>' . $arr['prod_price'] . '</td>'; 
    echo '<td>' . $arr['ser_name'] . '</td>'; 
    echo '<td>' . $arr['ret_name'] . '</td>'; 
    echo '<td>' . '<a class="btn btn-success btn-sm" href="modify.php?id=' . $arr['o_id']. '">modify</a>' . '<td>';
    echo '<td>' . '<a class="btn btn-danger btn-sm" href="delete.php?id=' . $arr['o_id'] . '">delete</a>' . '<td>';
    echo '</tr>';
  }

  // run query
  $DB -> runQuery($query);

  /* close database */
  $DB -> freeResult($result);	// free result memory
	$DB -> dbClose();	// close the connection
```

## Contributing

Anyone who wants to contribute to this project can simply fork/clone the repository from [here]. (https://github.com/yiweihsu/datenbanken-und-objektorientierung-projekt)

## Help

If there are any questions or bugs you found while using the application, please feel free to contact our team.

- yi-wei.hsu[at]s2015.tu-chemnitz.de 
- juncheng.hu[at]s2015.tu-chemnitz.de

## Installation

### Requirements

The application is complete web-based. As a user, the only requirement is to install a browser, such as Chrome, Safari, Firefox.......

As a developer, you need to set up the server to develop the application, such as Apache or Nginx. Feel free to try any kind of tools that you feel comfortable with.

### Installation

1. Fork this repository on Github.

2. Clone your forked repository (not our original one) to your hard drive with git clone https://github.com/YOURUSERNAME/datenbanken-und-objektorientierung-projekt.git

3. ```cd datenbanken-und-objektorientierung-projekt```

4. Set the configuration: "hostname", "port", "databse username", "database password" need to be filled in DBConn.php file.

5. Now you can play arund the application by visiting ```localhost://YOURSERVERPORT```

### Configuration

Set up a valid "database name", "username", and "password" on the file DBConn.php to access the database. 

More details about PostgreSQL configuration please visit the [website]. (https://www.postgresql.org/)

## Credits

Authors: Yi-Wei Hsu, Juncheng Hu
