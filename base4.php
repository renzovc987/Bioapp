<?php
		$param = $_POST['file'];
		$command = escapeshellcmd('python /xampp/htdocs/Bioapp/UPGMA.py '.$param);
		$output = shell_exec($command);
		//echo $output;
		$url="http://localhost/Bioapp/Algoritmo4.php";
		echo "<SCRIPT>window.location='$url';</SCRIPT>";
?>