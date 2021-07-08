<!DOCTYPE html>
<html>
<head>
	<title>BioApp</title>
    <meta charset="utf-8">

    <link rel="stylesheet" type="text/css" href="bootstrap/css/bootstrap.min.css">

    <link rel="stylesheet" href="css/style.css">

</head>
<body>
<?php include('nav/nav.php'); ?>

<div class="container" >

<div class="column1" >

            <div class="inner">
				<form action = "base5.php" method = "post">
					<label class="form-group">
						<input class="form-control1" id = "archivo" name = "archivo" type = "file">
						
					</label>


					<button type="Submit" >Alineamiento Global 
						<i class="zmdi zmdi-arrow-right"></i>
					</button>
				</form>
			</div>

</div>
<div class="column2" >
<?php
        $fp=fopen('leer.txt','r');
        echo '<p class="p12">';
            while (!feof($fp)){
                echo '<p class="p12">';
                $cont=fgets($fp);
                echo $cont;
                echo '</p>';           
            }
        echo '</p>';
        fclose($fp); 
         ?>
</div>

   
</div>

<footer> </footer>
</body>
</html>