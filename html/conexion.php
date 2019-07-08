 <?php
$servername = "localhost";
$username = "pepe";
$password = "pepemolinero";
$db="kiosko";
// Create connection
$conn = new mysqli($servername, $username, $password,$db);
mysqli_set_charset($conn,"utf8");
// Check connection
if ($conn->connect_error) {
    die("Conexión falla " . $conn->connect_error);
}
//echo "Conexión exitosa";


?> 
