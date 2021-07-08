<?php
		$param1 = $_POST['archivo'];

		$command = escapeshellcmd('python /xampp/htdocs/Bioapp/muscle.py '.$param1);
		$output = shell_exec($command);
		//echo $output;
		$url="http://localhost/Bioapp/Algoritmo5.php";
		echo "<SCRIPT>window.location='$url';</SCRIPT>";
?>