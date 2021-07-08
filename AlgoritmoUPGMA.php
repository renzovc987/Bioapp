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
  <li><a>Alineamiento multiple</a></li>
  <li><a href="Jukes.php">Jukes-cantor model</a></li>
  <li><a href="kimura.php">Kimura model</a></li>
  <li><a href="AlgoritmoUPGMA.php">UPGMA</a></li>
  <li><a>Neighbor Joining</a></li>
</ul>
</nav>
<section> 
	<form action = "base4.php" method = "post">
		<label>Matriz</label>
		<br>
		<input id = "file" name = "file" type = "file">
		<br>
		<input type="submit" name="submit" value="Alinear"/>
	</form>
</section>

<footer> </footer>
</body>
</html>