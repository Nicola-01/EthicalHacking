<?php
// Function to create a sql connection.
function getDB() {
  $dbhost="10.9.0.6";
  $dbuser="seed";
  $dbpass="dees";
  $dbname="sqllab_users";

  // Create a DB connection
  $conn = new mysqli($dbhost, $dbuser, $dbpass, $dbname);
  if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error . "\n");
  }
  return $conn;
}

$input_uname = $_GET['username'];
$input_pwd = $_GET['Password'];
$hashed_pwd = sha1($input_pwd);

// create a connection
$conn = getDB();

// do the query
// $result = $conn->query("SELECT id, name, eid, salary, ssn
//                         FROM credential
//                         WHERE name= '$input_uname' and Password= '$hashed_pwd'");


$stmt = $conn->prepare("SELECT id, name, eid, salary, ssn
                        FROM credential
                        WHERE name= ? and Password= ? ");
// Bind parameters to the query
$stmt->bind_param("ss", $input_uname, $hashed_pwd);
$stmt->execute();
$stmt->bind_result($bund_id, $bund_name, $bund_eid, $bund_salary, $bund_ssn);

if ($stmt->fetch()) {
  // only take the first row 
  // $firstrow = $result->fetch_assoc();
  $id     = $bund_id;
  $name   = $bund_name;
  $eid    = $bund_eid;
  $salary = $bund_salary;
  $ssn    = $bund_ssn;
}

// close the sql connection
$conn->close();
?>
