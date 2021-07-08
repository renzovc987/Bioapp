<?php
		$param1 = $_POST['archivo'];
		echo $param1;
		$command = escapeshellcmd('C:/Users/USUARIO/AppData/Local/Programs/Python/Python36/python.exe C:/xampp/htdocs/Bioapp/muscle.py '.$param1);
		echo $command;
		$output = shell_exec($command);
		echo $output;
?>