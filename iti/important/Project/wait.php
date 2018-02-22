<?php
session_start();
if (isset($_SESSION["username"])) {


    $pagetitle = "Home";



    include "ini.php";


    echo "<div class=\"container\"><div class='col-sm-offset-2 col-sm-8  col-md-offset-3 col-md-6  col-lg-offset-3 col-lg-6 alert alert-danger succ'>"
        . "Wiating for Admin</div> </div>" ;

?>
    <a href="Logout.php" class="btn btn-primary" style=" background-color: #363b59;  margin-left: 310px;width:100px "><i class="fa fa-sign-out" style="margin-right: 3px"></i>Logout</a>

<?php
} else{
    header("Location: index.php");
}

include $temp . "footer.php";
?>
