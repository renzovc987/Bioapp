<?php
		$param1 = $_POST['sec1'];
		$param2 = $_POST['sec2'];
		$command = escapeshellcmd('python /xampp/htdocs/Bioapp/JC.py '.$param1 .' '.$param2);
		$output = shell_exec($command);
		echo $output;
?>