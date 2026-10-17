<?php
include 'classes.php';
$a = new DangerousClass();
file_put_contents('serial_Nhom09', serialize($a));
?>
