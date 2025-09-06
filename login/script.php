<?php
extract($_REQUEST);
	// requires php5
	define('UPLOAD_DIR', 'upload/');
	
$filename = $bc.'.png';

$vv=$mac."|".$dt;
$fp=fopen("det.txt","w");
fwrite($fp,$vv);
fclose($fp);

	$img = $_POST['imgBase64'];
	$img = str_replace('data:image/png;base64,', '', $img);
	$img = str_replace(' ', '+', $img);
	$data = base64_decode($img);
	$file = UPLOAD_DIR . $filename; //uniqid() . '.png';
	$success = file_put_contents($file, $data);
	print $success ? $file : 'Unable to save the file.';
?>