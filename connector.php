<?php
$dsn = "mysql:host=5.75.182.107;dbname=esalim_db";
$dbusername = "esalim";
$dbpassword = "hbaQjp";


try {
    $pdo = new PDO($dsn, $dbusername, $dbpassword) ;
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTİON)
} catch (PDOException $e) {
    echo "Connection failed: " . $e->getMessage();
}
