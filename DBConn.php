<?php

global $dbconn;

class DB {
	var $result;

	function dbConn() {
		$dbconn = pg_connect("dbname=DBOO_test") or die('Could not connect: ' . pg_last_error());
		return $dbconn;
	}

	function freeResult($result) {
		pg_free_result($result);
	}

	function dbClose($dbconn) {
		pg_close($dbconn);
	}

	function runQuery($query) {
		$result = pg_query($query) or die('Query failed: ' . pg_last_error());
		return $result;
	}
}

?>