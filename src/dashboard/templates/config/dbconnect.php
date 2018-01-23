<?php 
/* Connection */
$conn_string = "host=localhost port=5432 dbname=afyabora user=afyaone password=afyabora123";
$conn = pg_connect($conn_string);

/* If connection fails*/
if (!$conn) {
	die("Database connection failed");
}

?>

