<?php #header("Content-type: text/html; charset=utf-8");
#//include_once('config.php');
		# $f=fopen(".\air\status.txt",r);
        	#$string=fgets($f);
   		# printf("status:" $string); # 
		#fclose($f);
		$file=file('./air/status.txt');
		echo ("status:".$file[0]);




printf(" 
<script type='text/javascript'>
//здесь текст скрипта, например: 
//alert('hello,world!'); 
setTimeout('window.location.reload()', 2000);
</script>
"); 

?>


