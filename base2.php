<?php
		$param1 = $_POST['sec1'];
		$param2 = $_POST['sec2'];
		$param3 = $_POST['cost'];
		$command = escapeshellcmd('python /xampp/htdocs/Bioapp/Alineamiento2.py '.$param1 .' '.$param2.' '.$param3);
		$output = shell_exec($command);
		echo $output;
?>