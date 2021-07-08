<!DOCTYPE html>
<html>
<head>
	<title>BioApp</title>
	<link rel="stylesheet" type="text/css" href="estilosxd.css">
	<meta charset="utf-8">
</head>
<body>
<header>
	<h1>Algoritmos de Bioinformática</h1>
</header>
<nav id="navegacion"> 
<ul>
  <li><a href="Algoritmo1.php">Needleman–Wunsch</a></li>
  <li><a href="Algoritmo2.php">Smith-waterman</a></li>
  <li><a href="Algoritmo3.php">BLAST</a></li>
  <li><a href="alineamientoMultiple.php">Alineamiento multiple</a></li>
  <li><a href="jukes.php">Jukes-cantor model</a></li>
  <li><a href="kimura.php">Kimura model</a></li>
  <li><a href="UPGMAP.php">UPGMA</a></li>
  <li><a href="neigh.php">Neighbor Joining</a></li>
  <li><a href="muscle.php">Muscle</a></li>
</ul>
</nav>
<header><h2>Alineamiento multiple</h2></header>
<section> 
	<form action = "base3.php" method = "post">
		<label>Base de Datos</label>
		<br>
		<input id = "archivo" name = "archivo" type = "file">
		<br>
		<br>
		<label>Consulta</label>
		<br>
		<input id="query" name="query" type="text">
		<input type="submit" name="submit" value="Alinear" />
	</form>
</section>

<footer> </footer>
</body>
</html>