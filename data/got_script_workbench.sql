USE got;

SELECT * FROM got_script;

ALTER TABLE got_script 
	RENAME COLUMN MyUnknownColumn TO ID;