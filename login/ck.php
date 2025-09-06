  <?php
extract($_REQUEST);

$fp=fopen("det.txt","r");
$vv=fread($fp,filesize("det.txt"));
fclose($fp);

$ss=explode("|",$vv);

?>
<html>
<head>
<title>Login</title>
<style type="text/css">
<!--
.style1 {color: #FF0000}
-->
</style>
</head>

<body>
<p>&nbsp;</p>
<p>&nbsp;</p>
<table border="0" align="center">
<tr>
<td>
<div align="center" style="width:300px; height:400px; border:1px solid #003366">
						<h3 align="center" class="style1">Unautorized Access your Login!</h3>
						<h4 align="center">Mac: <?php echo $ss[0]; ?></h4>
						<h4 align="center">Date / Time: <?php echo $ss[1]; ?></h4>
						
						<div align="center">
						<img src="upload/<?php echo $bc; ?>.png" />
						</div>
						
	</div>					
</td>
</tr>
</table>						
					
</body>

</html>