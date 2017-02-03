<?php
	$database_name = 'DBOO_v1';
	$host = 'localhost';
	$username = 'yiwei';
	$password = '1234';
	require 'PostgresDb.php';
	$DB = new PostgresDb($database_name, $host, $username, $password);
	$DB -> pdo();
	$result = $DB -> get('brand');
	echo $result[0]['brand'];
	echo $result[1]['brand'];
	
?>


<?php


// // Connecting, selecting database
// $dbconn = pg_connect("dbname=DBOO_v1")
//     or die('Could not connect: ' . pg_last_error());

// // Performing SQL query
// $query = 'SELECT * FROM version';
// $result = pg_query($query) or die('Query failed: ' . pg_last_error());

// // Printing results in HTML
// echo "<table>\n";
// while ($line = pg_fetch_array($result, null, PGSQL_ASSOC)) {
//     echo "\t<tr>\n";
//     foreach ($line as $col_value) {
//         echo "\t\t<td>$col_value</td>\n";
//     }
//     echo "\t</tr>\n";
// }
// echo "</table>\n";

// // Free resultset
// pg_free_result($result);

// // Closing connection
// pg_close($dbconn);
?>