<?php
class DangerousClass {
    function __construct() {
        $this->cmd = "ls";
    }
    function __destruct() {
        echo passthru($this->cmd);
    }
}

class NormalClass {
    function __construct() {
        $this->name = "Nhom09";
    }
    function __destruct() {
        echo $this->name;
    }
}
?>