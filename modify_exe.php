<?php

include 'DBConn.php';

$DB = new DB;
$DB -> dbConn();

$query = "
UPDATE order_items 
SET prod_id = {$_POST['product']}, ser_id = {$_POST['service']}, ret_id = {$_POST['retail']}
WHERE o_id = {$_POST['id']}; ";


// echo $query;
// echo $_POST['id'];

pg_query($query); 

// not working 
// $DB -> runQuery($query);

$DB -> dbClose();

header('Location: main.php');
exit;

?>