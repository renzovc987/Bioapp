<?php
		$param1 = $_POST['archivo'];
		$param2 = $_POST['query'];
		$command = escapeshellcmd('python /xampp/htdocs/Bioapp/blast.py '.$param1 .' '.$param2);
		$output = shell_exec($command);
		echo $output;
?>