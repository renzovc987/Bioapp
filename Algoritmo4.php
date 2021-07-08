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
				<form action = "base4.php" method = "post">
					<label class="form-group">
						<input class="form-control1" id = "archivo" name = "archivo" type = "file">
						
					</label>


					<button type="Submit" >Generar Arbol UPGMA 
						<i class="zmdi zmdi-arrow-right"></i>
					</button>
				</form>
			</div>

</div>
<div class="column2" >
    <img src="v44.png" alt="">
</div>

   
</div>

<footer> </footer>
</body>
</html>
