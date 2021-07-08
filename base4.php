<?php
		$param = $_POST['file'];
		$command = escapeshellcmd('python /xampp/htdocs/Bioapp/UPGMA.py '.$param.".txt");
		$output = shell_exec($command);
		echo $output;
?>