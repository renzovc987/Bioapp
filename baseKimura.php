<?php
		$param1 = $_POST['sec1'];
		$param2 = $_POST['sec2'];

		$command = escapeshellcmd('C:\Users\USUARIO\AppData\Local\Programs\Python\Python36\python /xampp/htdocs/Bioapp/kimura.py '.$param1.' '.$param2);
		$output = shell_exec($command);
		echo $output;
?>