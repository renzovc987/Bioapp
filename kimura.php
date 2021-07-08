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
<nav class="navegacion" id="navegacion"> 
<ul>
  <li><a href="Algoritmo1.php">Needleman–Wunsch</a></li>
  <li><a href="Algoritmo2.php">Smith-waterman</a></li>
  <li><a href="Algoritmo3.php">BLAST</a></li>
  <li><a>Alineamiento multiple</a></li>
  <li><a href="Jukes.php">Jukes-cantor model</a></li>
  <li><a href="kimura.php">Kimura model</a></li>
  <li><a href="AlgoritmoUPGMA.php">UPGMA</a></li>
  <li><a>Neighbor Joining</a></li>
</ul>
</nav>
<section> 
	<form id="form" action = "base6.php" method = "post">
		<label>Secuencia 1</label>
		<br>
		<input id = "sec1" name = "sec1" type = "text">
		<br>
		<br>
		<label>Secuencia 2</label>
		<br>
		<input id="sec2" name="sec2" type="text">
		<br>
		<input type="submit" name="submit" value="Alinear" />
	</form>
</section>

<footer> </footer>
</body>
</html>