<?php

include 'DBConn.php';

$DB = new DB;
$DB -> dbConn();

$query = "
INSERT INTO order_items(prod_id, ser_id, ret_id) 
VALUES (
	'" . $_POST['product'] . "',
	'". $_POST['service'] ."',
	'". $_POST['retail'] ."'
);";

pg_query($query); 

// not working 
// $DB -> runQuery($query);

$DB -> dbClose();

header('Location: index.php');
exit;

?>