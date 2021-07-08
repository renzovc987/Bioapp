<?php
		$param1 = $_POST['sec1'];
		$param2 = $_POST['sec2'];
		$param3 = $_POST['cost'];
		$param4 = $_POST['dist'];
		$param5 = $_POST['tree'];


		
		$command = escapeshellcmd('python /xampp/htdocs/Bioapp/Alineamiento.py '.$param1 .' '.$param2.' '.$param3.' '.$param4.' '.$param5);
		$output = shell_exec($command);

		$command = escapeshellcmd('python /xampp/htdocs/Bioapp/UPGMA2.py ');
		$output = shell_exec($command);
		//echo $output;
		$url="http://localhost/Bioapp/Algoritmo1.php";
		echo "<SCRIPT>window.location='$url';</SCRIPT>";
?>