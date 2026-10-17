<?php
class User
{
    public $name;
    public $isLoggedIn;
}
$user = new User();
$user->name = "Nhom09";
$user->isLoggedIn = true;
echo serialize($user);
echo "\n";
?>
