<?php

global $dbconn;

class DB {
  var $_dbConn = 0;
  var $_queryResource = 0;

  // connect DB
  function connect_db() {
  	$dbconn = pg_connect('dbname=DBOO_v1')
  		or die('Could not connect: ' . pg_last_error());
  }

  // free result
  function resultfree() {
  	pg_free_result($result);
  }

  // close DB
  function closeDB() {
  	pg_close($dbconn);
  }

  /* 呼叫資料庫連結 */
  // function connect_db($host, $user, $pwd, $dbname) {
  //   $dbConn = mysql_connect($host, $user, $pwd);
  //   if (!$dbConn) {
  //     echo "db connect error!";
  //   }
  //   mysql_query("SET NAMES 'UTF8'");
  //   if (!mysql_select_db($dbname, $dbConn)) {
  //      echo "mysql_select_db error!";
  //   }
  //   $this->_dbConn = $dbConn;
  //   return true;
  // }

  /* 執行SQL QUERY */
  function runQuery($sql) {
    if (!$queryResource = mysql_query($sql, $this->_dbConn)) {
      echo "mysql_query error!";
    }
    $this->_queryResource = $queryResource;
    return $queryResource;
  }

  /* Fetch Array */
  function fetch_array() {
    return mysql_fetch_array($this->_queryResource, MYSQL_ASSOC);
  }

  /* 執行SQL INSERT */
  function runInsert($sql) {
    if (!$queryResource = mysql_query($sql, $this->_dbConn)) {
      echo "mysql insert error!"; 
    }
  }

  /* 執行SQL UPDATE */
  function runUpdate($sql) {
    if (!$queryResource = mysql_query($sql, $this->_dbConn)) {
      echo "mysql update error!"; 
    }
  }

  /* 執行SQL DELETE */
  function runDelete($sql) {
    if (!$queryResource = mysql_query($sql, $this->_dbConn)) {
      echo "mysql delete error!"; 
    }
  }
}

?>