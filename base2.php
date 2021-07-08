<?php
		$param1 = $_POST['sec1'];
		$param2 = $_POST['sec2'];
		$param3 = $_POST['cost'];
		$param4 = $_POST['dist'];
		$param5 = $_POST['tree'];


		$command = escapeshellcmd('python /xampp/htdocs/Bioapp/Alineamiento2.py '.$param1 .' '.$param2.' '.$param3.' '.$param4.' '.$param5);
		$output = shell_exec($command);
		#echo $output;

		$url="http://localhost/Bioapp/Algoritmo2.php";
		echo "<SCRIPT>window.location='$url';</SCRIPT>";
?>