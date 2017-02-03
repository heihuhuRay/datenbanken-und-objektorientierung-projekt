<?php

// JOIN Multiple Tables
$query = '
SELECT brand.*, version.*, screen.*, cpu.*, ram.* 
FROM brand 
	JOIN version 
		ON brand.phone_id = version.phone_id
	JOIN screen
		ON version.phone_id = screen.phone_id
	JOIN cpu
		ON screen.phone_id = cpu.phone_id
	JOIN ram
		ON cpu.phone_id = ram.phone_id
';

?>