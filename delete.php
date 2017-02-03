<?php

include 'DBConn.php';

$DB = new DB;
$DB -> dbConn();

$query = "
DELETE FROM order_items WHERE order_items.o_id = '" . $_GET['id'] . "'";

pg_query($query); 

// // not working 
// // $DB -> runQuery($query);

$DB -> dbClose();

header('Location: index.php');
exit;

?>