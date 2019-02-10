<?php
if(isset($_POST['des'])){
    $url="https://jobs.github.com/positions.json?";
   $url=$url."description=".$_POST['des']."&location=".$_POST['loc'];
   $url = preg_replace('/\s+/', '+', $url);
$string = file_get_contents($url);
$json = json_decode($string, true);


foreach ($json as $key => $value) {
    if (!is_array($value)) {
        echo $key . '=>' . $value . '<br />';
    } else {
        foreach ($value as $key => $val) {
            echo $key . '=>' . $val . '<br />';
        }
    }
}

}
?>

<form action="rest2.php" method="post">
Location: <input type="text" name="loc"><br>
Description: <input type="text" name="des"><br>
<input type="submit">
</form>

