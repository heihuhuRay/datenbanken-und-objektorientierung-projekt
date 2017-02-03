<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Create New Entity</title>
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
<div class="container center_div">
  <div class="text-center">
    <h1>Create New Entity</h1>  
  </div>
  <hr>
  <form action="create_exe.php" method="POST">
  <div class="form-group">
    <select class="form-control" name="product" id="">
    <option value="" disabled selected>Select Product</option>
    <option value="1">iPhone 5</option>
    <option value="2">iPhone 5c</option>
    <option value="3">iPhone 5s</option>
    <option value="4">iPhone 6</option>
    <option value="5">iPhone 6s</option>
    <option value="6">Samsung Note3</option>
    <option value="7">Samsung Note4</option>
    <option value="8">Samsung S7</option>
    <option value="9">Samsung Note 7</option>
  </select>
  </div>
  <div class="form-group">
    <select class="form-control" name="service" id="">
    <option value="" disabled selected>Select Service</option>
    <option value="1">iTunes</option>
    <option value="2">iCloud</option>
    <option value="3">Samsung Cloud</option>
    <option value="4">Samsung Music</option>
  </select>
  </div>
  <div class="form-group">
  <select name="retail" class="form-control" id="">
    <option value="" disabled selected>Select Retailer</option>
    <option value="1">Ebay</option>
    <option value="2">Amazon</option>
  </select>
  </div>
  <div class="text-center"> 
    <button id="singlebutton" name="singlebutton" class="btn btn-primary">Submit</button> 
  </div>
  </form>
</div>
</body>
</html>