<?php

$nama2121 = $_GET['id'];

free($nama2121);

function free($vd){


	$ch = curl_init();
    $mkctvCH = basename($vd); 


	curl_setopt($ch, CURLOPT_URL, 'https://www.vidio.com/live/'.$vd.'/tokens');

	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
	curl_setopt($ch, CURLOPT_POST, 1);
        
	curl_setopt($ch, CURLOPT_ENCODING, 'gzip, deflate');



	$headers = array();

	$headers[] = 'Authority: www.vidio.com';

	$headers[] = 'Content-Length: 0';

	$headers[] = 'Origin: https://www.vidio.com';

	$headers[] = 'User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36';

	$headers[] = 'Dnt: 1';

	$headers[] = 'Accept: /';

	$headers[] = 'Sec-Fetch-Site: same-origin';

	$headers[] = 'Sec-Fetch-Mode: cors';

	$headers[] = 'Referer: https://m.vidio.com/live/'.$vd;

	$headers[] = 'Accept-Encoding: gzip, deflate, br';

	$headers[] = 'Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7';
	
	//$headers[] = 'cookie: masukan cookie disini;';

	curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);


	$result = curl_exec($ch);

	if (curl_errno($ch)) {

		echo 'Error:' . curl_error($ch);

	}

	curl_close($ch);

	$result = json_decode($result, true);

	$token= $result['token'];

    $link = "https://app-etslive-2.vidio.com/live/$vd/master.m3u8?$token";

    echo $link1 = file_get_contents($link);





}
