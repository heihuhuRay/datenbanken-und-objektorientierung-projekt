<?php
	require 'DBConn.php';
?>

<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>DBOO Project</title>

	<!-- bootstrap -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
	<!-- bootstrap -->

</head>
<body>

<div class="container">
	<h1>
	<span>Order Management System</span>	
	<a class="btn btn-info btn-lg pull-right" href="create.php" role="button">Create New Entity</a>
	</h1>
	<hr>
	<table class="table">
		<thead>
			<tr>
				<th>Order ID</th>
				<th>Order Number</th>
				<th>Product</th>
				<th>CPU Model</th>
				<th>Screen Size</th>
				<th>Product Price</th>
				<th>Service</th>
				<th>Retailer</th>
			</tr>
		</thead>
		<tbody>
<?php

$DB = new DB;
$DB -> dbConn();

// $query = '
// SELECT order_items.o_id, order_items.o_num, product.prod_name, product.cpu_model, product.scr_size, product.prod_price, service.ser_name, retailer.ret_name
// FROM product
// 	JOIN order_items
// 		ON product.prod_id = order_items.prod_id
// 	JOIN service
// 		ON order_items.ser_id = service.ser_id
// 	JOIN retailer
// 		ON order_items.ret_id = retailer.ret_id
// ';

$query = '
SELECT order_items.o_id, order_items.o_num, product.prod_name, product.cpu_model, product.scr_size, product.prod_price, service.ser_name, retailer.ret_name
FROM product, order_items, service, retailer
WHERE order_items.prod_id = product.prod_id 
AND order_items.ser_id = service.ser_id
AND order_items.ret_id = retailer.ret_id
';

$result = $DB -> runQuery($query);
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
$DB -> freeResult($result);
$DB -> dbClose($dbconn);
?>
		</tbody>
	</table>
</div>
</body>
</html>