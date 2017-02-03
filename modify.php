<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Modify Entity</title>
	<!-- bootstrap -->
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
	<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
	<!-- bootstrap -->
<style>
.center_div {
  width: 30%;
}
</style>
</head>
<body>
<?php
// echo $_GET['id'];
require 'DBConn.php';
$DB = new DB;
$DB -> dbConn();
$query = 'SELECT * FROM order_items WHERE o_id = ' . $_GET['id'] .';';

// select order items >> save into array >> get product_id, product_id, ret_id

$result = $DB -> runQuery($query);
$arr = pg_fetch_array($result, null, PGSQL_ASSOC);

// echo $arr['prod_id'];
// echo $arr['ser_id'];
// echo $arr['ret_id'];

// $query = "
// SELECT product.prod_id, product.prod_name, service.ser_name, retailer.ret_name 
// FROM product, service, retailer 
// WHERE product.prod_id = {$arr['prod_id']}
// AND service.ser_id = {$arr['ser_id']}
// AND retailer.ret_id = {$arr['ret_id']}
// ";

// $result = $DB -> runQuery($query);
// $arr = pg_fetch_array($result, null, PGSQL_ASSOC);
// echo $arr['prod_name'];
// echo $arr['ser_name'];
// echo $arr['ret_name'];

?>
<div class="container center_div">
  <div class="text-center">
    <h1>Update Entity</h1>
  </div>
  <hr>
  <form action="modify_exe.php" method="POST">
  <div class="form-group">
  	<input type="hidden" name="id" value="<?php echo $_GET['id']?>">
    <select class="form-control" name="product" id="">
    <option value="" disabled selected>Select Product</option>
    <option value="1" <?php echo($arr['prod_id']=='1')?'selected = "selected"':''?>>iPhone 5</option>
    <option value="2" <?php echo($arr['prod_id']=='2')?'selected = "selected"':''?>>iPhone 5c</option>
    <option value="3" <?php echo($arr['prod_id']=='3')?'selected = "selected"':''?>>iPhone 5s</option>
    <option value="4" <?php echo($arr['prod_id']=='4')?'selected = "selected"':''?>>iPhone 6</option>
    <option value="5" <?php echo($arr['prod_id']=='5')?'selected = "selected"':''?>>iPhone 6s</option>
    <option value="6" <?php echo($arr['prod_id']=='6')?'selected = "selected"':''?>>Samsung Note3</option>
    <option value="7" <?php echo($arr['prod_id']=='7')?'selected = "selected"':''?>>Samsung Note4</option>
    <option value="8" <?php echo($arr['prod_id']=='8')?'selected = "selected"':''?>>Samsung S7</option>
    <option value="9" <?php echo($arr['prod_id']=='9')?'selected = "selected"':''?>>Samsung Note 7</option>
  </select>
  </div>
  <div class="form-group">
    <select class="form-control" name="service" id="">
    <option value="" disabled selected>Select Service</option>
    <option value="1" <?php echo($arr['ser_id']=='1')?'selected = "selected"':''?>>iTunes</option>
    <option value="2" <?php echo($arr['ser_id']=='2')?'selected = "selected"':''?>>iCloud</option>
    <option value="3" <?php echo($arr['ser_id']=='3')?'selected = "selected"':''?>>Samsung Cloud</option>
    <option value="4" <?php echo($arr['ser_id']=='4')?'selected = "selected"':''?>>Samsung Music</option>
  </select>
  </div>
  <div class="form-group">
  <select name="retail" class="form-control" id="">
    <option value="" disabled selected>Select Retailer</option>
    <option value="1" <?php echo($arr['ret_id']=='1')?'selected = "selected"':''?>>Ebay</option>
    <option value="2" <?php echo($arr['ret_id']=='2')?'selected = "selected"':''?>>Amazon</option>
  </select>
  </div>
  <div class="text-center"> 
    <button id="singlebutton" name="singlebutton" class="btn btn-primary">Submit</button> 
  </div>
  </form>
</div>
</body>
</html>