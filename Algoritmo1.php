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
				<form action = "base.php" method = "post">
					<label class="form-group">
						<input type="text" class="form-control1 " id = "sec1" name = "sec1" type = "text" required>
						<span>Secuencia 1</span>
						<span class="border"></span>
					</label>
					<label class="form-group">
						<input type="text" class="form-control1" id="sec2" name="sec2" type="text" required>
						<span for="">Secuencia 2</span>
						<span class="border"></span>
					</label>

                    <label class="form-group">
						<input type="text" class="form-control1" id="cost" name="cost" type="text" required>
						<span for="">COSTO</span>
						<span class="border"></span>
					</label>

					<label class="form-group">
					Algoritmo de Distancia
					<br>
					<input  type="radio" name="dist" value="ag1"> Jukes-cantor
					<input type="radio" name="dist" value="ag2"> Kimura
					</label>

					<label class="form-group">
					Arbol Filogenetico
					<br>
					<input  type="radio" name="tree" value="tree1"> UPGMA
					<input type="radio" name="tree" value="tree2"> Neighbor
					</label>

					<button type="Submit" >Alinear 
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


<div>
<img src="v4.png" alt="">
</div>

			

    
</div>

<footer> </footer>
</body>
</html>